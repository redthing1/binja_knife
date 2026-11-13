from __future__ import annotations

import json
import os
import re
import shlex
import shutil
import subprocess
import tempfile
import time
from dataclasses import asdict, dataclass, field
from pathlib import Path

from bnk.client import BnkError, request
from bnk.endpoint import Endpoint
from bnk.runtime.native import library_path
from bnk.runtime.paths import cache_dir


def run(args: list[str], *, env: dict[str, str] | None = None) -> str:
    result = subprocess.run(args, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        raise BnkError(f"{args[0]} failed: {result.stderr.strip() or result.stdout.strip()}", kind="runtime")
    return result.stdout.strip()


@dataclass
class PluginSpec:
    repo: str
    ref: str = "main"
    deps: list[str] = field(default_factory=list)
    build: str = "python"

    @property
    def name(self) -> str:
        name = self.repo.rstrip("/").rsplit("/", 1)[-1].removesuffix(".git")
        if not re.fullmatch(r"[A-Za-z0-9_][A-Za-z0-9_.-]*", name):
            raise ValueError(f"invalid plugin name: {name}")
        return name

    def __post_init__(self) -> None:
        if self.build not in {"python", "cmake"}:
            raise ValueError("plugin build must be python or cmake")
        if self.build == "cmake" and self.deps:
            raise ValueError("Python dependencies apply to Python plugins")
        if not self.repo or not self.ref:
            raise ValueError("plugin repository and ref must be non-empty")
        local = Path(self.repo).expanduser()
        if local.exists():
            self.repo = str(local.resolve())


def plugin_spec(line: str) -> PluginSpec:
    tokens = shlex.split(line)
    if not tokens:
        raise ValueError("expected <repo> [ref] [deps=a,b] [build=python|cmake]")
    repo, *rest = tokens
    ref = rest.pop(0) if rest and "=" not in rest[0] else "main"
    options = {}
    for token in rest:
        key, sep, value = token.partition("=")
        if not sep or key not in {"deps", "build"} or key in options or not value:
            raise ValueError(f"invalid plugin option: {token}")
        options[key] = value
    deps = options["deps"].split(",") if "deps" in options else []
    return PluginSpec(repo, ref, deps, options.get("build", "python"))


def _checkout(repo: str, ref: str, destination: Path) -> str:
    run(["git", "clone", "--quiet", "--no-checkout", "--", repo, str(destination)])
    command = ["git", "-C", str(destination), "rev-parse", "--verify", "--end-of-options"]
    try:
        commit = run([*command, ref + "^{commit}"])
    except BnkError:
        commit = run([*command, "refs/remotes/origin/" + ref + "^{commit}"])
    run(["git", "-C", str(destination), "checkout", "--quiet", "--detach", commit])
    run(["git", "-C", str(destination), "submodule", "update", "--init", "--recursive"])
    return commit


def _sdk(runtime: Path) -> tuple[Path, str]:
    revision = (runtime / "binaryninja/api_REVISION.txt").read_text().splitlines()[-1].strip()
    if not re.fullmatch(r"[0-9a-f]{40}", revision):
        raise ValueError("invalid Binary Ninja API revision")
    root = cache_dir() / "binaryninja-api"
    destination = root / revision
    if not destination.exists():
        root.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix=".sdk-", dir=root) as directory:
            checkout = Path(directory) / "repo"
            _checkout("https://github.com/Vector35/binaryninja-api.git", revision, checkout)
            checkout.rename(destination)
    return destination, revision


def _build_native(runtime: Path, checkout: Path, work: Path) -> dict:
    plugins = runtime / "plugins"
    sdk, revision = _sdk(runtime)
    build = work / "build"
    install_root = work / "install"
    payload = install_root / "plugins"
    run(["cmake", "-S", str(checkout), "-B", str(build), "-DCMAKE_BUILD_TYPE=Release",
         f"-DBN_API_PATH={sdk}", f"-DBN_INSTALL_DIR={runtime / 'binaryninja'}",
         "-DBN_USER_PLUGINS_DIR=/plugins"])
    run(["cmake", "--build", str(build), "--parallel", str(min(os.cpu_count() or 2, 8))])
    run(["cmake", "--install", str(build)], env={**os.environ, "DESTDIR": str(install_root)})
    installed = (build / "install_manifest.txt").read_text().splitlines()
    files = [(install_root / path.lstrip("/")).resolve() for path in installed]
    if not files or any(not path.is_relative_to(payload.resolve()) for path in files):
        raise ValueError("CMake must install plugin files under BN_USER_PLUGINS_DIR")
    artifacts = []
    for path in sorted(payload.iterdir()):
        destination = plugins / path.name
        if destination.exists() or destination.is_symlink():
            raise ValueError(f"plugin artifact already exists: {path.name}")
        shutil.move(path, destination)
        artifacts.append(str(destination.relative_to(runtime)))
    if not any(Path(path).suffix == ".so" for path in artifacts):
        raise ValueError("CMake did not install a native plugin library")
    return {"api_commit": revision, "artifacts": artifacts}


def prepare(runtime: Path, spec: PluginSpec, name: str, report=print) -> dict:
    report(f"Preparing {name} ({spec.ref}, {spec.build})")
    plugins = runtime / "plugins"
    plugins.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix="bnk-plugin-") as directory:
        work = Path(directory)
        checkout = work / "repo"
        commit = _checkout(spec.repo, spec.ref, checkout)
        receipt = {"name": name, **asdict(spec), "commit": commit}
        if spec.build == "python":
            source = checkout / "plugin" if name == "knife_server" else checkout
            shutil.copytree(source, plugins / name, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            receipt["artifacts"] = [f"plugins/{name}"]
        else:
            receipt.update(_build_native(runtime, checkout, work))
        return receipt


def dependencies(runtime: Path, receipts: list[dict]) -> None:
    site = runtime / "python/site-packages"
    shutil.rmtree(site, ignore_errors=True)
    site.mkdir(parents=True)
    requirements = []
    for item in receipts:
        if item["build"] != "python":
            continue
        requirements += item["deps"]
        path = runtime / "plugins" / item["name"] / "requirements.txt"
        if path.is_file() and item["name"] != "knife_server":
            requirements += ["-r", str(path)]
    if requirements:
        metadata = json.loads((runtime / "runtime.json").read_text())
        run(["uv", "pip", "install", "--python", str(runtime / metadata["python_binary"]),
             "--target", str(site), *requirements],
            env={**os.environ, "LD_LIBRARY_PATH": library_path(runtime)})


def provision(runtime: Path, manifest: Path, report=print) -> list[dict]:
    specs = [("knife_server", PluginSpec(os.environ.get("KNIFE_REPO", "https://github.com/redthing1/binja_knife")))]
    for line in manifest.read_text().splitlines():
        if line.strip() and not line.lstrip().startswith("#"):
            spec = plugin_spec(line)
            specs.append((spec.name, spec))
    if len({name for name, _ in specs}) != len(specs):
        raise ValueError("duplicate plugin name")
    receipts = [prepare(runtime, spec, name, report) for name, spec in specs]
    dependencies(runtime, receipts)
    return receipts


def health(port: int = 18812) -> dict[str, bool]:
    items = request(Endpoint("127.0.0.1", port), "plugins")["plugins"]
    return {Path(item["path"]).name: item["running"] for item in items}


def running(receipt: dict, loaded: dict[str, bool]) -> bool:
    artifacts = [Path(path).name for path in receipt["artifacts"]
                 if receipt["build"] == "python" or Path(path).suffix == ".so"]
    return bool(artifacts) and all(loaded.get(name, False) for name in artifacts)


def validate_plugins(runtime: Path, port: int) -> None:
    receipts = json.loads((runtime / "runtime.json").read_text()).get("plugins", [])
    until = time.monotonic() + 10
    while True:
        loaded = health(port)
        missing = [item["name"] for item in receipts if not running(item, loaded)]
        if not missing:
            return
        if time.monotonic() >= until:
            raise BnkError("plugins failed to load: " + ", ".join(missing), kind="runtime")
        time.sleep(0.1)

