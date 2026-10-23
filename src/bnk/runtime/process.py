from __future__ import annotations

import contextlib
import json
import os
import select
import signal
import subprocess
import sys
import time
from pathlib import Path
from xml.sax.saxutils import escape

from bnk.client import BnkError, request
from bnk.endpoint import Endpoint
from bnk.protocol import API_VERSION
from bnk.runtime.native import library_path
from bnk.runtime.paths import runtime_dir, state_dir

PORT = 18812


@contextlib.contextmanager
def lock(state: Path):
    import fcntl

    state.mkdir(parents=True, exist_ok=True, mode=0o700)
    with (state / "control.lock").open("a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX)
        yield


def supervisor_pid(state: Path) -> int | None:
    """Check both the lifetime lock and Linux process identity, not just a PID."""
    import fcntl

    try:
        with (state / "supervisor.lock").open("r") as handle:
            try:
                fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
                return None
            except BlockingIOError:
                record = json.loads((state / "process.json").read_text())
                pid = record["pid"]
                if _identity(pid) == record["identity"]:
                    return pid
    except (OSError, ValueError, KeyError):
        pass
    return None


def _identity(pid: int) -> str:
    # comm can contain spaces and parentheses; starttime is field 22.
    return Path(f"/proc/{pid}/stat").read_text().rsplit(")", 1)[1].split()[19]


def probe(port: int = PORT) -> dict | None:
    try:
        value = request(Endpoint("127.0.0.1", port), "status",
                        connect_timeout=0.3, response_timeout=0.5)
    except BnkError:
        return None
    if isinstance(value, dict) and value.get("api") == API_VERSION and value.get("compatible"):
        return value
    return None


def ensure_started() -> None:
    runtime, state = runtime_dir(), state_dir()
    with lock(state):
        if not (runtime / "runtime.json").is_file():
            raise BnkError("no local runtime; use bnk runtime install ARCHIVE", kind="runtime")
        if supervisor_pid(state) is None:
            print("Starting local Binary Ninja...", file=sys.stderr)
        start(runtime, state)


def start(runtime: Path, state: Path, port: int = PORT) -> None:
    """Caller holds the control lock. Also used to validate staged installations."""
    if probe(port) is not None:
        if supervisor_pid(state) is not None:
            return
        raise BnkError(f"port {port} already has a server; stop it before starting this runtime",
                       kind="runtime")
    state.mkdir(parents=True, exist_ok=True, mode=0o700)
    child = None
    if supervisor_pid(state) is None:
        with (state / "runtime.log").open("ab") as output:
            child = subprocess.Popen(
                [sys.executable, "-m", "bnk.runtime.process", str(runtime), str(state), str(port)],
                stdin=subprocess.DEVNULL, stdout=output, stderr=subprocess.STDOUT,
                start_new_session=True,
            )
    deadline = time.monotonic() + 60
    while time.monotonic() < deadline:
        if probe(port) is not None and supervisor_pid(state) is not None:
            return
        if child is not None and child.poll() is not None:
            break
        time.sleep(0.1)
    if child is not None:
        stop(state)
        if child.poll() is None:
            child.terminate()
            child.wait(timeout=10)
    raise BnkError(f"runtime did not become ready; see {state / 'runtime.log'}", kind="runtime")


def stop(state: Path | None = None) -> bool:
    state = state or state_dir()
    pid = supervisor_pid(state)
    if pid is None:
        return False
    try:
        os.kill(pid, signal.SIGTERM)
    except ProcessLookupError:
        return False
    deadline = time.monotonic() + 15
    while time.monotonic() < deadline:
        if supervisor_pid(state) != pid:
            return True
        time.sleep(0.1)
    raise BnkError(f"runtime is still stopping; see {state / 'runtime.log'}", kind="runtime")


def environment(runtime: Path, state: Path, port: int) -> dict[str, str]:
    profile = state / "profile"
    profile.mkdir(parents=True, exist_ok=True, mode=0o700)
    metadata = json.loads((runtime / "runtime.json").read_text())
    for name, target in (("plugins", runtime / "plugins"),
                         (f"python{metadata['python']}", runtime / "python")):
        link = profile / name
        if link.is_symlink():
            link.unlink()
        if not link.exists():
            link.symlink_to(target, target_is_directory=True)
    settings = {
        "ui.log.minLevel": "DebugLog", "knife_server.autostart": True,
        "knife_server.host": "127.0.0.1", "knife_server.port": port,
        "network.enableReleaseNotes": False, "network.enableUpdateChannelList": False,
        "network.enableUpdates": False,
        "python.interpreter": str(runtime / metadata["python_library"]),
        "python.binaryOverride": str(runtime / metadata["python_binary"]),
    }
    (profile / "settings.json").write_text(json.dumps(settings))
    env = os.environ.copy()
    env.update({
        "BN_USER_DIRECTORY": str(profile), "BN_QSETTINGS_POSTFIX": "-knife-runtime",
        "LD_LIBRARY_PATH": library_path(runtime), "QT_QPA_PLATFORM": "xcb",
        "QT_XCB_GL_INTEGRATION": "none",
        "QT_PLUGIN_PATH": str(runtime / "binaryninja/qt"),
        "XKB_CONFIG_ROOT": str(runtime / "native/usr/share/X11/xkb"),
        "XLOCALEDIR": str(runtime / "native/usr/share/X11/locale"),
        "FONTCONFIG_FILE": str(state / "fonts.conf"),
    })
    # Respect caller-provided licensing; otherwise use the supplied archive's license.
    license_file = runtime / "binaryninja/license.dat"
    if license_file.is_file() and "BN_LICENSE" not in env:
        env["BN_LICENSE"] = license_file.read_text().strip()
    for name in ("PYTHONHOME", "PYTHONPATH", "QT_QPA_PLATFORM_PLUGIN_PATH",
                 "BN_DISABLE_USER_PLUGINS", "BN_DISABLE_USER_SETTINGS"):
        env.pop(name, None)
    env["PYTHONHOME"] = str((runtime / metadata["python_binary"]).parent.parent)
    (state / "fonts.conf").write_text(
        "<?xml version='1.0'?><!DOCTYPE fontconfig SYSTEM 'urn:fontconfig:fonts.dtd'>"
        f"<fontconfig><dir>{escape(str(runtime / 'native/usr/share/fonts'))}</dir>"
        f"<cachedir>{escape(str(state / 'font-cache'))}</cachedir></fontconfig>"
    )
    return env


def _terminate(child: subprocess.Popen | None) -> None:
    if child is None:
        return
    try:
        os.killpg(child.pid, signal.SIGTERM)
        child.wait(timeout=5)
    except ProcessLookupError:
        pass
    except subprocess.TimeoutExpired:
        os.killpg(child.pid, signal.SIGKILL)
        child.wait()


def _start_display(runtime: Path, env: dict[str, str]) -> tuple[subprocess.Popen, str]:
    read_fd, write_fd = os.pipe()
    child = None
    try:
        child = subprocess.Popen(
            [str(runtime / "native/usr/bin/Xvfb"), "-displayfd", str(write_fd),
             "-screen", "0", "1024x768x24", "-ac", "-nolisten", "tcp",
             "-xkbdir", str(runtime / "native/usr/share/X11/xkb")],
            cwd=runtime / "native/usr/bin", env=env,
            pass_fds=(write_fd,), start_new_session=True,
        )
        os.close(write_fd)
        write_fd = -1
        if not select.select([read_fd], [], [], 10)[0]:
            raise RuntimeError("Xvfb did not allocate a display")
        display = os.read(read_fd, 32).decode().strip()
        if not display.isdecimal():
            raise RuntimeError(f"Xvfb exited before allocating a display (exit {child.poll()})")
        return child, display
    except BaseException:
        _terminate(child)
        raise
    finally:
        os.close(read_fd)
        if write_fd != -1:
            os.close(write_fd)


def supervise(runtime: Path, state: Path, port: int) -> None:
    import fcntl

    state.mkdir(parents=True, exist_ok=True, mode=0o700)
    with (state / "supervisor.lock").open("a") as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            return
        record = {"pid": os.getpid(), "identity": _identity(os.getpid())}
        (state / "process.json").write_text(json.dumps(record))
        stopping = False

        def on_signal(signum, frame):
            nonlocal stopping
            stopping = True

        signal.signal(signal.SIGTERM, on_signal)
        signal.signal(signal.SIGINT, on_signal)
        attempts = 0
        try:
            env = environment(runtime, state, port)
            while not stopping:
                xvfb = bn = None
                started = time.monotonic()
                try:
                    xvfb, display = _start_display(runtime, env)
                    if stopping:
                        break
                    print(f"Starting Binary Ninja on :{display}", flush=True)
                    bn = subprocess.Popen(
                        [str(runtime / "binaryninja/binaryninja"), "--debug", "-e"],
                        env={**env, "DISPLAY": f":{display}"}, cwd=runtime / "binaryninja",
                        start_new_session=True,
                    )
                    while not stopping and bn.poll() is None and xvfb.poll() is None:
                        time.sleep(0.1)
                    if stopping or bn.poll() == 0:
                        break
                    print(f"Runtime exited (Binja={bn.poll()}, Xvfb={xvfb.poll()})", flush=True)
                except Exception as error:
                    print(f"Runtime failed: {error}", flush=True)
                finally:
                    _terminate(bn)
                    _terminate(xvfb)
                attempts = 0 if time.monotonic() - started > 60 else attempts + 1
                if attempts >= 5:
                    print("Runtime stopped after five startup failures", flush=True)
                    break
                delay = min(2 ** attempts, 30)
                print(f"Restarting in {delay}s; in-memory sessions were lost", flush=True)
                until = time.monotonic() + delay
                while not stopping and time.monotonic() < until:
                    time.sleep(0.1)
        finally:
            (state / "process.json").unlink(missing_ok=True)


if __name__ == "__main__":
    supervise(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), int(sys.argv[3]))
