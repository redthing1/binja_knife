from __future__ import annotations

import json
import os
import shlex
import shutil
import socket
import stat
import subprocess
import tarfile
import tempfile
import zipfile
from collections.abc import Callable
from pathlib import Path

from bnk.client import BnkError
from bnk.runtime.native import DEFAULTS, check_platform, install_libraries, library_path
from bnk.runtime.paths import data_dir, runtime_dir, state_dir
from bnk.runtime.process import lock, start, stop, supervisor_pid


def run(args: list[str], *, env: dict[str, str] | None = None) -> str:
    result = subprocess.run(args, env=env, text=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if result.returncode:
        # Never include the environment, which may contain BN_LICENSE.
        raise BnkError(f"{args[0]} failed: {result.stderr.strip() or result.stdout.strip()}", kind="runtime")
    return result.stdout.strip()


def unpack(source: Path, destination: Path) -> None:
    if zipfile.is_zipfile(source):
        with zipfile.ZipFile(source) as archive:
            for item in archive.infolist():
                path = destination / item.filename
                if not path.resolve().is_relative_to(destination.resolve()):
                    raise ValueError("archive contains a path outside its destination")
                mode = item.external_attr >> 16
                if stat.S_ISLNK(mode):
                    target = archive.read(item).decode()
                    if Path(target).is_absolute() or not (path.parent / target).resolve().is_relative_to(destination.resolve()):
                        raise ValueError("archive contains a link outside its destination")
                    path.parent.mkdir(parents=True, exist_ok=True)
                    path.symlink_to(target)
                    continue
                archive.extract(item, destination)
                if mode & 0o111 and path.is_file():
                    path.chmod(0o755)
        return
    with source.open("rb") as handle:
        is_zstd = handle.read(4) == b"\x28\xb5\x2f\xfd"
    if is_zstd:
        if not shutil.which("zstd"):
            raise BnkError("zstd is needed to read this archive", kind="runtime")
        with subprocess.Popen(["zstd", "-dc", "--", str(source)], stdout=subprocess.PIPE,
                              stderr=subprocess.DEVNULL) as child:
            try:
                with tarfile.open(fileobj=child.stdout, mode="r|") as archive:
                    archive.extractall(destination, filter="data")
            except BaseException:
                child.terminate()
                raise
            finally:
                child.stdout.close()
            if child.wait():
                raise ValueError("could not decompress archive")
    else:
        with tarfile.open(source) as archive:
            archive.extractall(destination, filter="data")


def plugin_spec(line: str) -> tuple[str, str, list[str]]:
    tokens = shlex.split(line)
    if not 1 <= len(tokens) <= 3:
        raise ValueError("expected <repo_url> [ref] [deps=a,b]")
    repo, ref, deps = tokens[0], "main", []
    rest = tokens[1:]
    if rest and not rest[0].startswith("deps="):
        ref = rest.pop(0)
    if rest:
        if len(rest) != 1 or not rest[0].startswith("deps="):
            raise ValueError("expected a single deps=a,b field")
        deps = [dep.strip() for dep in rest[0][5:].split(",") if dep.strip()]
    return repo, ref, deps


def provision_plugins(
    runtime: Path, manifest: Path, python: Path, report: Callable[[str], None]
) -> list[dict[str, str]]:
    plugins = runtime / "plugins"
    plugins.mkdir()
    site = runtime / "python/site-packages"
    site.mkdir(parents=True)
    specs = [(os.environ.get("KNIFE_REPO", "https://github.com/redthing1/binja_knife"), "main", [], "knife_server")]
    for number, line in enumerate(manifest.read_text().splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        try:
            repo, ref, deps = plugin_spec(line)
        except ValueError as error:
            raise ValueError(f"invalid plugin manifest line {number}: {error}") from error
        name = repo.rstrip("/").rsplit("/", 1)[-1].removesuffix(".git")
        if name in {"", ".", "..", "knife_server"} or name in [item[3] for item in specs]:
            raise ValueError(f"invalid or duplicate plugin name: {name}")
        specs.append((repo, ref, deps, name))
    resolved = []
    env = {**os.environ, "LD_LIBRARY_PATH": library_path(runtime)}
    for repo, ref, deps, name in specs:
        report(f"Preparing {name} ({ref})")
        with tempfile.TemporaryDirectory(prefix="bnk-plugin-") as directory:
            checkout = Path(directory) / "repo"
            run(["git", "clone", "--quiet", "--", repo, str(checkout)])
            run(["git", "-C", str(checkout), "checkout", "--quiet", ref])
            commit = run(["git", "-C", str(checkout), "rev-parse", "HEAD"])
            requirements = checkout / "requirements.txt"
            install_args = [*deps]
            if requirements.is_file() and name != "knife_server":
                install_args.extend(["-r", str(requirements)])
            if install_args:
                run(["uv", "pip", "install", "--python", str(python), "--target", str(site),
                     *install_args], env=env)
            shutil.rmtree(checkout / ".git")
            shutil.copytree(checkout / "plugin" if name == "knife_server" else checkout, plugins / name)
            resolved.append({"name": name, "repo": repo, "ref": ref, "commit": commit})
    return resolved


def _prepare_python(runtime: Path) -> tuple[Path, Path, str]:
    prefix = runtime / "binaryninja/plugins/python"
    python = prefix / "bin/python3"
    if not python.is_file():
        python = next((p for p in sorted((prefix / "bin").glob("python3.*")) if p.is_file()), python)
    if not python.is_file():
        raise ValueError("this runtime requires a Binja archive with bundled Python")

    # Relative links join Binja's split Python layout for isolated uv queries
    # and remain valid when the installation moves.
    bundled = prefix / "bundled-python3"
    if (bundled / "lib").is_dir():
        for entry in (bundled / "lib").iterdir():
            link = prefix / "lib" / entry.name
            if not link.exists():
                link.symlink_to(os.path.relpath(entry, link.parent), target_is_directory=entry.is_dir())
        if not (prefix / "include").exists():
            (prefix / "include").symlink_to("bundled-python3/include", target_is_directory=True)

    libraries = sorted((prefix / "lib").glob("libpython3.*.so.1.0"))
    if not libraries:
        raise ValueError("archive has no bundled libpython")
    version = run(
        [str(python), "-c", "import sys; print(f'{sys.version_info.major}{sys.version_info.minor}')"],
        env={**os.environ, "LD_LIBRARY_PATH": library_path(runtime)},
    )
    return python, libraries[0], version


def install(source: Path, *, plugins: Path | None = None, license_file: Path | None = None,
            report: Callable[[str], None] = print) -> Path:
    check_platform()
    source = source.expanduser().resolve()
    if not source.is_file():
        raise BnkError(f"archive not found: {source}", kind="runtime")
    runtime, state = runtime_dir(), state_dir()
    data_dir().mkdir(parents=True, exist_ok=True, mode=0o700)
    with lock(state):
        if supervisor_pid(state) is not None:
            raise BnkError("runtime is running; use bnk runtime stop before replacing it", kind="runtime")
        with tempfile.TemporaryDirectory(prefix=".install-", dir=data_dir()) as directory:
            work = Path(directory)
            extracted = work / "archive"
            extracted.mkdir()
            report("Extracting archive")
            unpack(source, extracted)
            roots = [extracted, *[p for p in extracted.iterdir() if p.is_dir()]]
            prepared = next((p for p in roots if (p / "runtime.json").is_file()), None)
            staged = work / "runtime"
            if prepared is not None:
                if plugins is not None:
                    raise ValueError("--plugins applies to original Binja archives, not prepared bundles")
                prepared.rename(staged)
                metadata = json.loads((staged / "runtime.json").read_text())
                if metadata.get("format") != 1:
                    raise ValueError("unsupported runtime bundle format")
            else:
                bn_root = next((p for p in roots if (p / "binaryninja").is_file()), None)
                if bn_root is None:
                    raise ValueError("archive contains neither a Binary Ninja installation nor a runtime bundle")
                for command in ("git", "uv", "zstd"):
                    if not shutil.which(command):
                        raise BnkError(f"{command} is needed to prepare a runtime", kind="runtime")
                staged.mkdir()
                bn_root.rename(staged / "binaryninja")
                install_libraries(staged / "native", report)
                python, library, version = _prepare_python(staged)
                resolved = provision_plugins(staged, plugins or DEFAULTS / "plugins.manifest", python, report)
                metadata = {"format": 1, "python": version,
                            "python_binary": str(python.relative_to(staged)),
                            "python_library": str(library.relative_to(staged)), "plugins": resolved}
                (staged / "runtime.json").write_text(json.dumps(metadata, indent=2) + "\n")
            if license_file is not None:
                shutil.copyfile(license_file.expanduser(), staged / "binaryninja/license.dat")
                (staged / "binaryninja/license.dat").chmod(0o600)
            report("Checking Binary Ninja and Knife startup")
            validation = work / "validation"
            with socket.socket() as sock:
                sock.bind(("127.0.0.1", 0))
                port = sock.getsockname()[1]
            try:
                start(staged, validation, port)
            except BnkError as error:
                target = state / "install.log"
                if (validation / "runtime.log").exists():
                    shutil.copyfile(validation / "runtime.log", target)
                raise BnkError(f"installation startup check failed; see {target}", kind="runtime") from error
            finally:
                stop(validation)
            previous = work / "previous"
            if runtime.exists():
                runtime.rename(previous)
            try:
                staged.rename(runtime)
                start(runtime, state)
            except BaseException:
                stop(state)
                if runtime.exists():
                    shutil.rmtree(runtime)
                if previous.exists():
                    previous.rename(runtime)
                raise
    return runtime


def pack(destination: Path) -> None:
    if not shutil.which("zstd"):
        raise BnkError("zstd is needed to create a runtime bundle", kind="runtime")
    destination = destination.expanduser().resolve()
    with lock(state_dir()):
        if not (runtime_dir() / "runtime.json").is_file():
            raise BnkError("no local runtime installed", kind="runtime")
        if destination.is_relative_to(runtime_dir()):
            raise ValueError("bundle destination must be outside the runtime directory")
        if destination.exists():
            raise ValueError(f"destination already exists: {destination}")
        with tempfile.NamedTemporaryFile(dir=destination.parent, prefix=".bnk-pack-", delete=False) as output:
            temporary = Path(output.name)
            try:
                with subprocess.Popen(["zstd", "-T0", "-3", "-c"], stdin=subprocess.PIPE,
                                      stdout=output, stderr=subprocess.DEVNULL) as child:
                    try:
                        with tarfile.open(fileobj=child.stdin, mode="w|") as archive:
                            archive.add(runtime_dir(), arcname="runtime")
                    finally:
                        child.stdin.close()
                    if child.wait():
                        raise ValueError("bundle compression failed")
                os.link(temporary, destination)
            finally:
                temporary.unlink(missing_ok=True)
