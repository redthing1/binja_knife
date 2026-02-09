from __future__ import annotations

import importlib
import io
import json
import sys
import traceback
from contextlib import redirect_stderr, redirect_stdout
from typing import Any, Dict, Optional

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
from .sessions import SessionManager
from .views import collect_gui_bvs, match_views, view_info_full


SESSIONS = SessionManager()

_ServiceBase = getattr(rpyc, "Service", object) if rpyc is not None else object


def _ensure_rpyc() -> None:
    if rpyc is None:
        raise RuntimeError(f"rpyc import failed: {_RPYC_IMPORT_ERROR}")


def _run_file(
    path: str, g: Dict[str, Any], argv=None, capture_output: bool = True
) -> Dict[str, Any]:
    argv = argv or []
    g["__file__"] = path
    g["__name__"] = "__main__"
    g["__package__"] = None

    stdout = io.StringIO()
    stderr = io.StringIO()
    old_argv = sys.argv
    sys.argv = [path] + list(argv)
    try:
        with open(path, "r", encoding="utf-8") as fh:
            source = fh.read()
        compiled = compile(source, path, "exec")
        if capture_output:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                exec(compiled, g, g)
        else:
            exec(compiled, g, g)
        return {
            "ok": True,
            "stdout": stdout.getvalue(),
            "stderr": stderr.getvalue(),
            "result": g.get("__result__"),
        }
    except SystemExit as exc:
        code = exc.code
        ok = code in (0, None)
        payload = {
            "ok": ok,
            "stdout": stdout.getvalue(),
            "stderr": stderr.getvalue(),
            "result": g.get("__result__"),
            "exit_code": code,
        }
        if not ok:
            payload["error"] = f"SystemExit({code})"
        return payload
    except Exception:
        return {
            "ok": False,
            "stdout": stdout.getvalue(),
            "stderr": stderr.getvalue(),
            "error": traceback.format_exc(),
        }
    finally:
        sys.argv = old_argv


def _run_code(
    code: str, g: Dict[str, Any], argv=None, capture_output: bool = True
) -> Dict[str, Any]:
    argv = argv or []
    g["__file__"] = None
    g["__name__"] = "__main__"
    g["__package__"] = None

    stdout = io.StringIO()
    stderr = io.StringIO()
    old_argv = sys.argv
    sys.argv = ["<knife_server>"] + list(argv)
    try:
        compiled = compile(code, "<knife_server>", "exec")
        if capture_output:
            with redirect_stdout(stdout), redirect_stderr(stderr):
                exec(compiled, g, g)
        else:
            exec(compiled, g, g)
        return {
            "ok": True,
            "stdout": stdout.getvalue(),
            "stderr": stderr.getvalue(),
            "result": g.get("__result__"),
        }
    except SystemExit as exc:
        code = exc.code
        ok = code in (0, None)
        payload = {
            "ok": ok,
            "stdout": stdout.getvalue(),
            "stderr": stderr.getvalue(),
            "result": g.get("__result__"),
            "exit_code": code,
        }
        if not ok:
            payload["error"] = f"SystemExit({code})"
        return payload
    except Exception:
        return {
            "ok": False,
            "stdout": stdout.getvalue(),
            "stderr": stderr.getvalue(),
            "error": traceback.format_exc(),
        }
    finally:
        sys.argv = old_argv


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

    def exposed_bv(self):
        return root_bv()

    def exposed_eval(self, cmd: str):
        with ROOT_LOCK, BN_LOCK:
            return eval(cmd, root_globals())

    def exposed_exec(self, cmd: str):
        with ROOT_LOCK, BN_LOCK:
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
        with ROOT_LOCK, BN_LOCK:
            return _run_file(
                path, root_globals(), argv=argv, capture_output=capture_output
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
            return binaryninja.load(
                source, update_analysis=update_analysis, options=options
            )

    def exposed_session_open(self, name: str) -> str:
        SESSIONS.open(name)
        return name

    def exposed_session_list(self):
        return SESSIONS.list_names()

    def exposed_session_close(self, name: str) -> bool:
        return SESSIONS.close(name)

    def exposed_session_reset(self, name: str, keep_bv: bool = True) -> bool:
        sess = SESSIONS.get(name)
        with sess.lock:
            sess.reset(keep_bv=keep_bv)
        return True

    def exposed_view_list(
        self, name: str, include_unnamed: bool = False, full: bool = False
    ):
        sess = SESSIONS.get(name)
        with sess.lock, BN_LOCK:
            entries = collect_gui_bvs()
            if not include_unnamed:
                entries = [
                    (bv, info)
                    for bv, info in entries
                    if (info.get("filename") or "").strip()
                ]
            sess.views_cache = entries
            sess.views_cache_include_unnamed = include_unnamed

            views = []
            for idx, (_bv, info) in enumerate(entries):
                out = dict(info)
                out["index"] = idx
                if full:
                    try:
                        out.update(view_info_full(_bv))
                    except Exception:
                        pass
                views.append(out)
            return views

    def exposed_view_attach(
        self,
        name: str,
        index: Optional[int] = None,
        match: Optional[str] = None,
        include_unnamed: bool = False,
    ):
        sess = SESSIONS.get(name)
        with sess.lock, BN_LOCK:
            # if cache is empty (or missing unnamed views), refresh the listing
            if not sess.views_cache or (
                include_unnamed and not sess.views_cache_include_unnamed
            ):
                entries = collect_gui_bvs()
                if not include_unnamed:
                    entries = [
                        (bv, info)
                        for bv, info in entries
                        if (info.get("filename") or "").strip()
                    ]
                sess.views_cache = entries
                sess.views_cache_include_unnamed = include_unnamed

            views = [info for _bv, info in sess.views_cache]

            chosen_index: Optional[int] = None
            if index is not None:
                if not isinstance(index, int):
                    raise ValueError("index must be an int")
                chosen_index = index
            elif match:
                matches = match_views(views, match)
                if not matches:
                    raise ValueError(f"no views match {match!r}")
                if len(matches) > 1:
                    raise ValueError(f"multiple views match {match!r}: {matches}")
                chosen_index = matches[0]
            else:
                raise ValueError("attach requires index or match")

            if chosen_index < 0 or chosen_index >= len(sess.views_cache):
                raise IndexError(f"index out of range: {chosen_index}")

            bv, info = sess.views_cache[chosen_index]
            sess.set_bv(bv)
            out = view_info_full(bv)
            out["index"] = chosen_index
            out["source"] = info.get("source", "")
            return out

    def exposed_view_status(self, name: str):
        sess = SESSIONS.get(name)
        with sess.lock, BN_LOCK:
            if sess.bv is None:
                return {"attached": False}
            out = view_info_full(sess.bv)
            out["attached"] = True
            return out

    def exposed_view_load(
        self,
        name: str,
        path: str,
        update_analysis: bool = True,
        options_json: Optional[str] = None,
    ):
        options = {}
        if options_json is not None:
            options = json.loads(options_json)
        sess = SESSIONS.get(name)
        with sess.lock, BN_LOCK:
            bv = binaryninja.load(
                path, update_analysis=update_analysis, options=options
            )
            sess.set_bv(bv)
            out = view_info_full(bv)
            out["attached"] = True
            out["source"] = "load"
            return out

    def exposed_run_code(
        self, name: str, code: str, argv=None, capture_output: bool = True
    ):
        sess = SESSIONS.get(name)
        with sess.lock, BN_LOCK:
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
