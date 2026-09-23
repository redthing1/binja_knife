#!/usr/bin/env -S uv run --script
# /// script
# requires-python = ">=3.10"
# dependencies = [
#   "beautifulsoup4>=4.12",
#   "markdownify>=0.13",
#   "requests>=2.31",
# ]
# ///

import argparse
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path
from urllib.parse import urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify


DOCS_DIR = Path(__file__).resolve().parent
MANIFEST = DOCS_DIR / ".binja-docs.json"
DEFAULT_BASE_URL = "https://api.binary.ninja/"


def load_manifest() -> dict:
    if not MANIFEST.exists():
        return {}
    return json.loads(MANIFEST.read_text(encoding="utf-8"))


def fetch(session: requests.Session, url: str, timeout: float) -> str:
    response = session.get(url, timeout=timeout)
    response.raise_for_status()
    return response.content.decode("utf-8", errors="replace")


def detect_version(session: requests.Session, base_url: str, timeout: float) -> str:
    inv_url = urljoin(base_url, "objects.inv")
    try:
        inventory = fetch(session, inv_url, timeout)
        match = re.search(r"^# Version:\s*(\S+)", inventory, re.MULTILINE)
        if match:
            return match.group(1)
    except requests.RequestException:
        pass

    root_html = fetch(session, base_url, timeout)
    soup = BeautifulSoup(root_html, "html.parser")
    title = soup.title.string if soup.title else ""
    match = re.search(r"Documentation v([^\s<]+)", title)
    if not match:
        raise RuntimeError("could not detect Binary Ninja API docs version")
    return match.group(1)


def module_pages(root_html: str, base_url: str) -> list[tuple[str, str]]:
    soup = BeautifulSoup(root_html, "html.parser")
    pages: list[tuple[str, str]] = []
    seen: set[str] = set()

    for link in soup.select(".wy-menu a.reference.internal[href]"):
        href = link.get("href", "")
        match = re.fullmatch(r"binaryninja\.([A-Za-z0-9_]+)-module\.html", href)
        if not match:
            continue
        module = match.group(1)
        if module in seen:
            continue
        seen.add(module)
        pages.append((module, urljoin(base_url, href)))

    if not pages:
        raise RuntimeError("could not find any module pages in docs sidebar")
    return pages


def localize_links(article: BeautifulSoup, page_url: str, base_url: str) -> None:
    for link in article.select("a.headerlink"):
        link.decompose()

    for link in article.find_all("a", href=True):
        href = link["href"]
        if href.startswith("#"):
            continue

        parsed = urlparse(href)
        if parsed.scheme or parsed.netloc:
            continue

        path, fragment = (href.split("#", 1) + [""])[:2] if "#" in href else (href, "")
        match = re.fullmatch(r"binaryninja\.([A-Za-z0-9_]+)-module\.html", path)
        if match:
            local = f"{match.group(1)}.md"
            link["href"] = f"{local}#{fragment}" if fragment else local
        else:
            link["href"] = urljoin(page_url if path.startswith("_") else base_url, href)


def clean_markdown(text: str) -> str:
    text = text.replace("\u00a0", " ")
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip() + "\n"


def page_to_markdown(html: str, page_url: str, base_url: str) -> str:
    soup = BeautifulSoup(html, "html.parser")
    article = soup.select_one('div[itemprop="articleBody"]')
    if article is None:
        raise RuntimeError(f"could not find article body in {page_url}")

    localize_links(article, page_url, base_url)
    rendered = markdownify(
        str(article),
        heading_style="ATX",
        bullets="-",
        escape_asterisks=False,
        escape_underscores=False,
        wrap=True,
        wrap_width=88,
    )
    return clean_markdown(rendered)


def write_index(out_dir: Path, base_url: str, version: str, pages: list[tuple[str, str]]) -> str:
    module_list = "\n".join(f"- `{name}.md`" for name, _ in pages)
    text = f"""# Binary Ninja Python API Docs (v{version})

Source: {base_url}

These files are the Binary Ninja Python API module docs, converted to Markdown.
The version and module list are recorded in `.binja-docs.json` alongside this file.

## Modules

{module_list}
"""
    (out_dir / "INDEX.md").write_text(text, encoding="utf-8")
    return text


def replace_docs(tmp_dir: Path, files: list[str]) -> None:
    for old_file in DOCS_DIR.glob("*.md"):
        old_file.unlink()
    for name in files:
        shutil.move(str(tmp_dir / name), DOCS_DIR / name)


def main() -> int:
    manifest = load_manifest()
    parser = argparse.ArgumentParser(description="Sync vendored Binary Ninja Python API docs.")
    parser.add_argument("--base-url", default=manifest.get("base_url", DEFAULT_BASE_URL))
    version_group = parser.add_mutually_exclusive_group(required=True)
    version_group.add_argument("--version", help="expected docs version, for example: 5.3")
    version_group.add_argument(
        "--update-version",
        action="store_true",
        help="accept the version reported by the live docs",
    )
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    base_url = args.base_url.rstrip("/") + "/"
    session = requests.Session()
    session.headers["User-Agent"] = "binaryninja-knife-doc-sync/1"

    detected_version = detect_version(session, base_url, args.timeout)
    if args.version and detected_version != args.version:
        print(
            f"refusing to sync v{detected_version}; expected v{args.version}. "
            "Pass --update-version to accept the detected version.",
            file=sys.stderr,
        )
        return 2

    version = detected_version if args.update_version else args.version
    root_html = fetch(session, base_url, args.timeout)
    pages = module_pages(root_html, base_url)

    previous_files = {path.name for path in DOCS_DIR.glob("*.md") if path.name != "INDEX.md"}
    with tempfile.TemporaryDirectory(prefix="binja-docs-") as tmp:
        tmp_dir = Path(tmp)
        files: list[str] = []

        write_index(tmp_dir, base_url, version, pages)
        files.append("INDEX.md")

        for module, url in pages:
            name = f"{module}.md"
            markdown = page_to_markdown(fetch(session, url, args.timeout), url, base_url)
            (tmp_dir / name).write_text(markdown, encoding="utf-8")
            files.append(name)

        current_files = set(files[1:])
        generated = {
            "base_url": base_url,
            "version": version,
            "files": files[1:],
        }
        manifest_text = json.dumps(generated, indent=2, sort_keys=True) + "\n"
        (tmp_dir / ".binja-docs.json").write_text(manifest_text, encoding="utf-8")
        files.append(".binja-docs.json")

        if args.dry_run:
            print(
                f"would sync {len(files) - 2} module files for Binary Ninja API v{version}",
                file=sys.stderr,
            )
            added = sorted(current_files - previous_files)
            removed = sorted(previous_files - current_files)
            if added:
                print("added: " + ", ".join(added), file=sys.stderr)
            if removed:
                print("removed: " + ", ".join(removed), file=sys.stderr)
            return 0

        replace_docs(tmp_dir, files)

    print(f"synced {len(pages)} module files for Binary Ninja API v{version}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
