from __future__ import annotations

import ctypes
import importlib
import io
import json
import sys
import threading
import time
import traceback
from dataclasses import dataclass
from contextlib import contextmanager
from contextlib import redirect_stderr, redirect_stdout
from typing import Any, Callable, Dict, List, Optional

import binaryninja  # type: ignore

try:
    import rpyc  # type: ignore
except Exception as _exc:  # pragma: no cover - Binary Ninja will have deps installed
    rpyc = None
    _RPYC_IMPORT_ERROR = _exc
else:
    _RPYC_IMPORT_ERROR = None

from .locks import BN_LOCK, ROOT_LOCK
from .constants import PLUGIN_NAME, SETTINGS_GROUP
from .log import dbg
from .root_state import reset_root_globals, root_bv, root_globals, set_root_bv
from .sessions import Session, SessionManager
from .views import find_shared_view, shared_view_inventory


SESSIONS = SessionManager()

_ServiceBase = getattr(rpyc, "Service", object) if rpyc is not None else object
_ACTIVE_REQUEST_LOCK = threading.RLock()
_ACTIVE_REQUESTS: Dict[int, "ActiveRequest"] = {}
_ACTIVE_REQUEST_NEXT_ID = 0


@dataclass(frozen=True)
class ActiveRequest:
    id: int
    name: str
    thread_id: int
    started_monotonic: float
    session: Optional[str] = None

    def snapshot(self) -> Dict[str, Any]:
        out: Dict[str, Any] = {
            "id": self.id,
            "name": self.name,
            "thread_id": self.thread_id,
            "elapsed_s": max(0.0, time.monotonic() - self.started_monotonic),
        }
        if self.session:
            out["session"] = self.session
        return out


def _ensure_rpyc() -> None:
    if rpyc is None:
        raise RuntimeError(f"rpyc import failed: {_RPYC_IMPORT_ERROR}")


def _next_request_id() -> int:
    global _ACTIVE_REQUEST_NEXT_ID
    with _ACTIVE_REQUEST_LOCK:
        _ACTIVE_REQUEST_NEXT_ID += 1
        return _ACTIVE_REQUEST_NEXT_ID


def _select_active_requests(
    session: Optional[str] = None,
) -> List[ActiveRequest]:
    with _ACTIVE_REQUEST_LOCK:
        requests = [
            request
            for request in _ACTIVE_REQUESTS.values()
            if session is None or request.session == session
        ]
    requests.sort(
        key=lambda request: (request.started_monotonic, request.id)
    )
    return requests


def _request_response(
    request: ActiveRequest,
    *,
    active: bool,
    count: int = 1,
    requests: Optional[List[ActiveRequest]] = None,
    ok: Optional[bool] = None,
    interrupted: Optional[bool] = None,
    error: Optional[str] = None,
) -> Dict[str, Any]:
    out = request.snapshot()
    out["active"] = active
    out["count"] = count
    if ok is not None:
        out["ok"] = ok
    if interrupted is not None:
        out["interrupted"] = interrupted
    if error:
        out["error"] = error
    if requests is not None and len(requests) > 1:
        out["requests"] = [item.snapshot() for item in requests]
    return out


def _active_request_snapshot(session: Optional[str] = None) -> Optional[Dict[str, Any]]:
    requests = _select_active_requests(session=session)
    if not requests:
        return None

    return _request_response(
        requests[0],
        active=True,
        count=len(requests),
        requests=requests,
    )


def _busy_sessions() -> set[str]:
    return {
        request.session
        for request in _select_active_requests()
        if request.session is not None
    }


@contextmanager
def _track_active_request(name: str, *, session: Optional[str] = None):
    token = _next_request_id()
    with _ACTIVE_REQUEST_LOCK:
        _ACTIVE_REQUESTS[token] = ActiveRequest(
            id=token,
            name=name,
            session=session,
            thread_id=threading.get_ident(),
            started_monotonic=time.monotonic(),
        )
    try:
        yield token
    finally:
        with _ACTIVE_REQUEST_LOCK:
            _ACTIVE_REQUESTS.pop(token, None)


def _async_raise(thread_id: int, exc_type: type[BaseException]) -> bool:
    # CPython delivers this only when the target thread returns to Python
    # bytecode. C-level blocking calls (for example time.sleep or socket I/O)
    # will not stop until they yield back into the interpreter.
    try:
        set_async_exc = ctypes.pythonapi.PyThreadState_SetAsyncExc
    except Exception:
        return False

    try:
        result = set_async_exc(ctypes.c_ulong(thread_id), ctypes.py_object(exc_type))
    except Exception:
        return False

    if result == 1:
        return True

    if result > 1:
        try:
            set_async_exc(ctypes.c_ulong(thread_id), None)
        except Exception:
            pass
    return False


def _interrupt_active_request(session: Optional[str] = None) -> Dict[str, Any]:
    requests = _select_active_requests(session=session)
    if not requests:
        return {"ok": True, "interrupted": False, "active": False}

    caller_thread_id = threading.get_ident()
    target = next(
        (request for request in requests if request.thread_id != caller_thread_id),
        None,
    )
    if target is None:
        return _request_response(
            requests[0],
            active=True,
            count=len(requests),
            requests=requests,
            ok=False,
            interrupted=False,
            error="cannot interrupt current request thread",
        )

    interrupted = _async_raise(target.thread_id, KeyboardInterrupt)
    dbg(
        f"interrupt request id={target.id} name={target.name} thread={target.thread_id} interrupted={interrupted}"
    )
    return _request_response(
        target,
        active=True,
        count=len(requests),
        requests=requests,
        ok=interrupted,
        interrupted=interrupted,
        error=None if interrupted else "failed to inject KeyboardInterrupt",
    )


def _run_exec(
    make_compiled: Callable[[], Any],
    g: Dict[str, Any],
    *,
    argv0: str,
    argv=None,
    capture_output: bool = True,
) -> Dict[str, Any]:
    argv = argv or []

    stdout = io.StringIO()
    stderr = io.StringIO()
    old_argv = sys.argv
    sys.argv = [argv0] + list(argv)
    try:
        compiled = make_compiled()
        if capture_output:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                exec(compiled, g, g)
        else:
            exec(compiled, g, g)

        payload: Dict[str, Any] = {
            "ok": True,
            "stdout": stdout.getvalue(),
            "stderr": stderr.getvalue(),
        }
    except KeyboardInterrupt:
        payload = {
            "ok": False,
            "stdout": stdout.getvalue(),
            "stderr": stderr.getvalue(),
            "error": "KeyboardInterrupt",
        }
    except SystemExit as exc:
        code = exc.code
        ok = code in (0, None)
        payload = {
            "ok": ok,
            "stdout": stdout.getvalue(),
            "stderr": stderr.getvalue(),
            "exit_code": code,
        }
        if not ok:
            payload["error"] = f"SystemExit({code})"
    except Exception:
        payload = {
            "ok": False,
            "stdout": stdout.getvalue(),
            "stderr": stderr.getvalue(),
            "error": traceback.format_exc(),
        }
    finally:
        sys.argv = old_argv

    if "__result__" in g:
        payload["result"] = g["__result__"]
    return payload


def _run_file(
    path: str, g: Dict[str, Any], argv=None, capture_output: bool = True
) -> Dict[str, Any]:
    g.pop("__result__", None)
    g["__file__"] = path
    g["__name__"] = "__main__"
    g["__package__"] = None

    def make_compiled():
        with open(path, "r", encoding="utf-8") as fh:
            source = fh.read()
        return compile(source, path, "exec")

    return _run_exec(
        make_compiled,
        g,
        argv0=path,
        argv=argv,
        capture_output=capture_output,
    )


def _run_code(
    code: str, g: Dict[str, Any], argv=None, capture_output: bool = True
) -> Dict[str, Any]:
    g.pop("__result__", None)
    g["__file__"] = None
    g["__name__"] = "__main__"
    g["__package__"] = None

    def make_compiled():
        return compile(code, "<knife_server>", "exec")

    return _run_exec(
        make_compiled,
        g,
        argv0="<knife_server>",
        argv=argv,
        capture_output=capture_output,
    )


def _session_snapshot(name: str) -> Dict[str, Any]:
    sess = SESSIONS.get(name)
    return _snapshot_session(sess, busy=name in _busy_sessions())


def _session_snapshots() -> List[Dict[str, Any]]:
    busy = _busy_sessions()
    out: List[Dict[str, Any]] = []
    for name in SESSIONS.list_names():
        try:
            sess = SESSIONS.get(name)
        except KeyError:
            continue
        out.append(_snapshot_session(sess, busy=name in busy))
    return out


def _snapshot_session(sess: Session, *, busy: bool) -> Dict[str, Any]:
    locked = sess.lock.acquire(blocking=False)
    try:
        snap = sess.snapshot(busy=busy or not locked)
    finally:
        if locked:
            sess.lock.release()
    return snap


def _release_owned_path(session_name: str, path: str) -> None:
    if path:
        SESSIONS.release_owned_path(session_name, path)


def _release_previous_owned_path(
    session_name: str,
    out: Dict[str, Any],
    *,
    keep_path: str = "",
) -> None:
    previous_owned_path = str(out.get("previous_owned_path", "") or "")
    if previous_owned_path and previous_owned_path != keep_path:
        _release_owned_path(session_name, previous_owned_path)


class KnifeServerService(_ServiceBase):  # instantiated by rpyc in server threads
    """RPyC service exposing root and session primitives."""

    ALIASES = ["binja", SETTINGS_GROUP, PLUGIN_NAME]

    def __init__(self):
        _ensure_rpyc()

    def on_connect(self, conn):
        dbg(f"connect open: {conn}")

    def on_disconnect(self, conn):
        dbg(f"connection closed: {conn}")

    exposed_binaryninja = binaryninja

    def exposed_request_status(self, session: Optional[str] = None):
        snap = _active_request_snapshot(session=session)
        if snap is None:
            return {"active": False}
        snap["active"] = True
        return snap

    def exposed_request_interrupt(self, session: Optional[str] = None):
        return _interrupt_active_request(session=session)

    def exposed_bv(self):
        return root_bv()

    def exposed_eval(self, cmd: str):
        with ROOT_LOCK:
            with _track_active_request("root.eval"):
                return eval(cmd, root_globals())

    def exposed_exec(self, cmd: str):
        with ROOT_LOCK:
            with _track_active_request("root.exec"):
                exec(cmd, root_globals())
        return True

    def exposed_import_module(self, mod: str):
        return importlib.import_module(mod)

    def exposed_add_to_syspath(self, path: str):
        return sys.path.append(path)

    def exposed_reset_globals(self):
        with ROOT_LOCK:
            reset_root_globals()
        return True

    def exposed_run_file(self, path: str, argv=None, capture_output: bool = True):
        with ROOT_LOCK:
            with _track_active_request("root.run_file"):
                return _run_file(
                    path, root_globals(), argv=argv, capture_output=capture_output
                )

    def exposed_session_run_file(
        self, name: str, path: str, argv=None, capture_output: bool = True
    ):
        sess = SESSIONS.get(name)
        with sess.lock:
            with _track_active_request(f"session.{name}.run_file", session=name):
                sess.globals["bv"] = sess.bv
                return _run_file(
                    path, sess.globals, argv=argv, capture_output=capture_output
                )

    def exposed_binaryview_load(
        self,
        source: Any,
        update_analysis: bool = True,
        options_json: Optional[str] = None,
    ) -> Any:
        options = {}
        if options_json is not None:
            options = json.loads(options_json)
        with BN_LOCK:
            with _track_active_request("root.binaryview_load"):
                return binaryninja.load(
                    source, update_analysis=update_analysis, options=options
                )

    def exposed_session_open(self, name: str):
        sess = SESSIONS.open(name)
        with sess.lock:
            return sess.snapshot(busy=False)

    def exposed_session_list(self):
        return _session_snapshots()

    def exposed_session_show(self, name: str):
        return _session_snapshot(name)

    def exposed_session_close(self, name: str) -> bool:
        try:
            sess = SESSIONS.get(name)
        except KeyError:
            return {"name": name, "closed": False}

        with sess.lock, BN_LOCK:
            with _track_active_request(f"session.{name}.session_close", session=name):
                out = sess.detach_bv(close_owned=True)
                _release_previous_owned_path(name, out)
        return {"name": name, "closed": SESSIONS.close(name)}

    def exposed_session_reset(self, name: str, keep_bv: bool = True):
        sess = SESSIONS.get(name)
        with sess.lock, BN_LOCK:
            with _track_active_request(f"session.{name}.session_reset", session=name):
                out = sess.reset(keep_bv=keep_bv)
                _release_previous_owned_path(name, out)
                snap = sess.snapshot(busy=False)
                snap["reset"] = True
                return snap

    def exposed_session_attach(
        self,
        name: str,
        view_id: str,
        include_unnamed: bool = False,
    ):
        with BN_LOCK:
            bv, info = find_shared_view(
                view_id,
                include_unnamed=include_unnamed,
            )

        sess = SESSIONS.open(name)
        with sess.lock, BN_LOCK:
            with _track_active_request(f"session.{name}.session_attach", session=name):
                replace_info = sess.set_bv(bv, owned=False)
                _release_previous_owned_path(name, replace_info)
                out = sess.snapshot(busy=False)
                out["id"] = info.get("id", "")
                if replace_info.get("replaced"):
                    out["replaced"] = True
                if replace_info.get("previous_closed"):
                    out["previous_closed"] = True
                return out

    def exposed_session_load(
        self,
        name: str,
        path: str,
        update_analysis: bool = True,
        options_json: Optional[str] = None,
    ):
        options = {}
        if options_json is not None:
            options = json.loads(options_json)

        sess = SESSIONS.get_optional(name)
        created_session = sess is None
        claimed_path = ""
        claimed_new_path = False
        if created_session:
            claimed_path = SESSIONS.claim_owned_path(name, path)
            claimed_new_path = bool(claimed_path)
            sess, created_session = SESSIONS.open_with_created(name)

        with sess.lock, BN_LOCK:
            previous_owned_path = sess.owned_path
            try:
                if not claimed_path:
                    claimed_path = SESSIONS.claim_owned_path(name, path)
                    claimed_new_path = bool(
                        claimed_path and claimed_path != previous_owned_path
                    )
                with _track_active_request(f"session.{name}.session_load", session=name):
                    bv = binaryninja.load(
                        path, update_analysis=update_analysis, options=options
                    )
                    if bv is None:
                        raise RuntimeError(f"failed to load view from {path!r}")

                    replace_info = sess.set_bv(bv, owned=True, owned_path=claimed_path)
                    _release_previous_owned_path(
                        name,
                        replace_info,
                        keep_path=claimed_path,
                    )
                    out = sess.snapshot(busy=False)
                    if replace_info.get("replaced"):
                        out["replaced"] = True
                    if replace_info.get("previous_closed"):
                        out["previous_closed"] = True
                    return out
            except Exception:
                if claimed_new_path:
                    _release_owned_path(name, claimed_path)
                if created_session:
                    out = sess.detach_bv(close_owned=True)
                    _release_previous_owned_path(name, out)
                    SESSIONS.close(name)
                raise

    def exposed_session_detach(self, name: str):
        sess = SESSIONS.get(name)
        with sess.lock, BN_LOCK:
            with _track_active_request(f"session.{name}.session_detach", session=name):
                out = sess.detach_bv(close_owned=True)
                _release_previous_owned_path(name, out)
                snap = sess.snapshot(busy=False)
                if out.get("had_attached"):
                    snap["detached"] = True
                if out.get("closed"):
                    snap["closed"] = True
                return snap

    def exposed_view_list(self, include_unnamed: bool = False, full: bool = False):
        with BN_LOCK:
            with _track_active_request("view_list"):
                views = []
                entries = shared_view_inventory(
                    include_unnamed=include_unnamed,
                    full=full,
                )
                for _bv_ref, info in entries:
                    views.append(dict(info))
                return views

    def exposed_run_code(
        self, name: str, code: str, argv=None, capture_output: bool = True
    ):
        sess = SESSIONS.get(name)
        with sess.lock:
            with _track_active_request(f"session.{name}.run_code", session=name):
                # A sleeping or network-bound script in one session must not hold
                # the global BN lock and starve unrelated sessions.
                # keep session globals in sync with attached bv
                sess.globals["bv"] = sess.bv
                return _run_code(
                    code, sess.globals, argv=argv, capture_output=capture_output
                )


def validate_service_imports() -> Optional[str]:
    try:
        _ensure_rpyc()
    except Exception as exc:
        return str(exc)
    return None


def set_root_view_for_start(bv: Any) -> None:
    with ROOT_LOCK:
        set_root_bv(bv)
        reset_root_globals()


def clear_root_view() -> None:
    with ROOT_LOCK:
        set_root_bv(None)
        reset_root_globals()
