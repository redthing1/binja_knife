from __future__ import annotations

import json
import os
import shutil
import socket
import stat
import subprocess
import tarfile
import tempfile
import zipfile
from collections.abc import Callable
from dataclasses import asdict
from pathlib import Path

from bnk.client import BnkError, request
from bnk.endpoint import Endpoint
from bnk.runtime.native import DEFAULTS, check_platform, install_libraries, library_path
from bnk.runtime.paths import data_dir, runtime_dir, state_dir
from bnk.runtime.process import lock, start, stop, supervisor_pid
from bnk.runtime.plugins import PluginSpec, dependencies, prepare, provision, run, validate_plugins


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
                if metadata.get("format") != 2:
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
                metadata = {"format": 2, "python": version,
                            "python_binary": str(python.relative_to(staged)),
                            "python_library": str(library.relative_to(staged)), "plugins": []}
                (staged / "runtime.json").write_text(json.dumps(metadata, indent=2) + "\n")
                metadata["plugins"] = provision(staged, plugins or DEFAULTS / "plugins.manifest", report)
                (staged / "runtime.json").write_text(json.dumps(metadata, indent=2) + "\n")
            if license_file is not None:
                shutil.copyfile(license_file.expanduser(), staged / "binaryninja/license.dat")
                (staged / "binaryninja/license.dat").chmod(0o600)
            validate(staged, work / "validation", state, report)
            activate(staged, runtime, state)
    return runtime


def validate(staged: Path, validation: Path, state: Path, report=print) -> None:
    report("Checking Binary Ninja and plugin startup")
    with socket.socket() as sock:
        sock.bind(("127.0.0.1", 0))
        port = sock.getsockname()[1]
    try:
        start(staged, validation, port)
        validate_plugins(staged, port)
    except BnkError as error:
        target = state / "install.log"
        state.mkdir(parents=True, exist_ok=True)
        if (validation / "runtime.log").exists():
            shutil.copyfile(validation / "runtime.log", target)
        raise BnkError(f"plugin startup check failed: {error}; see {target}", kind="runtime") from error
    finally:
        stop(validation)


def activate(staged: Path, runtime: Path, state: Path) -> None:
    previous = runtime.with_name(runtime.name + ".previous")
    if previous.exists():
        raise BnkError(f"previous installation needs recovery: {previous}", kind="runtime")
    if runtime.exists():
        runtime.rename(previous)
    try:
        staged.rename(runtime)
        start(runtime, state)
        validate_plugins(runtime, 18812)
    except BaseException as error:
        try:
            stop(state)
            if runtime.exists():
                shutil.rmtree(runtime)
            if previous.exists():
                previous.rename(runtime)
        except Exception as recovery_error:
            backup = f"; previous installation retained at {previous}" if previous.exists() else ""
            raise BnkError(f"runtime recovery failed: {recovery_error}{backup}", kind="runtime") from error
        raise
    if previous.exists():
        shutil.rmtree(previous)


def change_plugins(*, spec: PluginSpec | None = None, name: str | None = None, report=print) -> None:
    runtime, state = runtime_dir(), state_dir()
    with lock(state):
        metadata = json.loads((runtime / "runtime.json").read_text())
        if metadata.get("format") != 2:
            raise ValueError("unsupported runtime format")
        receipts = metadata["plugins"]
        for item in receipts:
            for artifact in item["artifacts"]:
                parts = Path(artifact).parts
                if len(parts) != 2 or parts[0] != "plugins" or parts[1] in {".", ".."}:
                    raise ValueError(f"invalid plugin artifact: {artifact}")
        if spec is not None:
            name = spec.name
            if name == "knife_server" or any(item["name"] == name for item in receipts):
                raise ValueError(f"plugin already installed: {name}")
            selected = [{"name": name, **asdict(spec)}]
        else:
            selected = [item for item in receipts if name is None or item["name"] == name]
            if not selected:
                raise ValueError(f"plugin not installed: {name}")
        was_running = supervisor_pid(state) is not None
        if was_running:
            request(Endpoint("127.0.0.1", 18812), "maintenance")
        try:
            if was_running:
                stop(state)
            with tempfile.TemporaryDirectory(prefix=".plugins-", dir=data_dir()) as directory:
                work = Path(directory)
                staged = work / "runtime"
                shutil.copytree(runtime, staged, symlinks=True)
                for item in selected:
                    for artifact in item.get("artifacts", []):
                        path = staged / artifact
                        if path.is_dir() and not path.is_symlink():
                            shutil.rmtree(path)
                        else:
                            path.unlink(missing_ok=True)
                    desired = spec or PluginSpec(item["repo"], item["ref"], item["deps"], item["build"])
                    receipt = prepare(staged, desired, item["name"], report)
                    receipts = [r for r in receipts if r["name"] != item["name"]] + [receipt]
                if any(item["build"] == "python" for item in selected):
                    dependencies(staged, receipts)
                metadata["plugins"] = receipts
                (staged / "runtime.json").write_text(json.dumps(metadata, indent=2) + "\n")
                validate(staged, work / "validation", state, report)
                activate(staged, runtime, state)
        except BaseException:
            if runtime.with_name(runtime.name + ".previous").exists():
                raise
            if supervisor_pid(state) is not None:
                request(Endpoint("127.0.0.1", 18812), "maintenance", {"enabled": False})
            start(runtime, state)
            raise


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
