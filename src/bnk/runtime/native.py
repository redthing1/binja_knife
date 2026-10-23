from __future__ import annotations

import hashlib
import io
import json
import os
import platform
import shutil
import subprocess
import tarfile
import urllib.request
from collections.abc import Callable
from pathlib import Path

from bnk.client import BnkError
from bnk.runtime.paths import cache_dir

DEFAULTS = Path(__file__).with_name("defaults")


def check_platform() -> None:
    if platform.system() != "Linux" or platform.machine() != "x86_64":
        raise BnkError("local runtimes require Linux x86-64", kind="runtime")
    libc, version = platform.libc_ver()
    if libc != "glibc" or tuple(map(int, version.split(".")[:2])) < (2, 39):
        raise BnkError("local runtimes require glibc 2.39 or newer", kind="runtime")


def extract_deb(content: bytes, destination: Path) -> None:
    """Read the data tarball from a Debian ar archive; never run package scripts."""
    if not content.startswith(b"!<arch>\n"):
        raise ValueError("invalid Debian package")
    offset = 8
    while offset + 60 <= len(content):
        header = content[offset:offset + 60]
        size = int(header[48:58])
        name = header[:16].decode().strip().rstrip("/")
        payload = content[offset + 60:offset + 60 + size]
        if name.startswith("data.tar"):
            if name.endswith(".zst"):
                payload = subprocess.run(["zstd", "-dc"], input=payload, stdout=subprocess.PIPE,
                                         stderr=subprocess.PIPE, check=True).stdout
            with tarfile.open(fileobj=io.BytesIO(payload)) as archive:
                for member in archive:
                    # Debian packages sometimes use absolute links within their root.
                    if member.issym() and member.linkname.startswith("/"):
                        target = destination / member.linkname.lstrip("/")
                        parent = (destination / member.name).parent
                        member.linkname = os.path.relpath(target, parent)
                    archive.extract(member, destination, filter="data")
            return
        offset += 60 + size + size % 2
    raise ValueError("Debian package has no data archive")


def install_libraries(destination: Path, report: Callable[[str], None]) -> None:
    manifest = json.loads((DEFAULTS / "libraries.json").read_text())
    cache = cache_dir() / "packages"
    cache.mkdir(parents=True, exist_ok=True)
    destination.mkdir(parents=True)
    report("Preparing native runtime libraries")
    for package in manifest["packages"]:
        cached = cache / package["sha256"]
        content = cached.read_bytes() if cached.exists() else b""
        if hashlib.sha256(content).hexdigest() != package["sha256"]:
            with urllib.request.urlopen(package["url"], timeout=120) as response:
                content = response.read()
            if hashlib.sha256(content).hexdigest() != package["sha256"]:
                raise ValueError(f"checksum mismatch for {package['name']}")
            cached.write_bytes(content)
        extract_deb(content, destination)
    # Xvfb's compiled xkbcomp directory has no command-line override. Make the
    # locked binary use its working directory (native/usr/bin) instead of /usr/bin.
    # Keep ELF offsets unchanged; fail closed if a package update changes the layout.
    xvfb = destination / "usr/bin/Xvfb"
    content = xvfb.read_bytes()
    old = b"\0/usr/bin\0"
    if content.count(old) != 1:
        raise ValueError("unexpected Xvfb layout: cannot relocate xkbcomp")
    xvfb.write_bytes(content.replace(old, b"\0.\0".ljust(len(old), b"\0")))
    shutil.copy2(DEFAULTS / "libraries.json", destination / "libraries.json")


def library_path(runtime: Path) -> str:
    return ":".join(str(path) for path in (
        runtime / "binaryninja", runtime / "native/usr/lib/x86_64-linux-gnu",
        runtime / "native/lib/x86_64-linux-gnu",
    ))
