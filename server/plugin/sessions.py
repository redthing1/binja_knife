from __future__ import annotations

import threading
import weakref
from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional, Tuple

import binaryninja  # type: ignore


def _new_globals(bv: Optional[Any]) -> Dict[str, Any]:
    g: Dict[str, Any] = {
        "__name__": "__bn_session__",
        "__file__": None,
        "__package__": None,
        "binaryninja": binaryninja,
        "bn": binaryninja,
        "bv": bv,
    }
    return g


def _safe_filename(bv: Optional[Any]) -> str:
    if bv is None:
        return ""
    try:
        file_obj = getattr(bv, "file", None)
        if file_obj is None:
            return ""
        return str(
            getattr(file_obj, "filename", "")
            or getattr(file_obj, "original_filename", "")
            or ""
        )
    except Exception:
        return ""


def _safe_close_bv(bv: Optional[Any]) -> bool:
    if bv is None:
        return False
    try:
        file_obj = getattr(bv, "file", None)
        if file_obj is None:
            return False
        close_fn = getattr(file_obj, "close", None)
        if not callable(close_fn):
            return False
        close_fn()
        return True
    except Exception:
        return False


@dataclass
class Session:
    name: str
    lock: threading.RLock = field(default_factory=threading.RLock)
    bv: Optional[Any] = None
    owns_bv: bool = False
    globals: Dict[str, Any] = field(default_factory=dict)
    # cached results from the most recent view listing: list of (weakref(binaryview), info dict)
    views_cache: List[Tuple[weakref.ReferenceType[Any], Dict[str, Any]]] = field(
        default_factory=list
    )
    views_cache_include_unnamed: bool = False

    def __post_init__(self) -> None:
        self.globals = _new_globals(self.bv)
        self.globals["__session_name__"] = self.name

    def clear_views_cache(self) -> None:
        self.views_cache = []
        self.views_cache_include_unnamed = False

    def set_bv(self, bv: Optional[Any], *, owned: bool = False) -> Dict[str, Any]:
        prev_bv = self.bv
        prev_owned = self.owns_bv
        prev_filename = _safe_filename(prev_bv)
        replaced = prev_bv is not None and prev_bv is not bv
        previous_closed = False

        # Close previously loaded views to avoid leaked references / locked DB handles.
        if replaced and prev_owned:
            previous_closed = _safe_close_bv(prev_bv)

        self.bv = bv
        self.owns_bv = bool(owned and bv is not None)
        self.globals["bv"] = bv
        return {
            "replaced": replaced,
            "previous_owned": prev_owned,
            "previous_closed": previous_closed,
            "previous_filename": prev_filename,
        }

    def detach_bv(
        self, *, close_owned: bool = True, force_close: bool = False
    ) -> Dict[str, Any]:
        prev_bv = self.bv
        prev_owned = self.owns_bv
        prev_filename = _safe_filename(prev_bv)
        had_attached = prev_bv is not None
        closed = False
        if had_attached and (force_close or (close_owned and prev_owned)):
            closed = _safe_close_bv(prev_bv)

        self.bv = None
        self.owns_bv = False
        self.globals["bv"] = None
        return {
            "had_attached": had_attached,
            "was_owned": prev_owned,
            "closed": closed,
            "filename": prev_filename,
            "forced": bool(force_close),
        }

    def reset(self, keep_bv: bool = True) -> None:
        if not keep_bv:
            self.detach_bv(close_owned=True, force_close=False)

        bv = self.bv if keep_bv else None
        owns_bv = self.owns_bv if keep_bv else False
        self.bv = bv
        self.owns_bv = owns_bv
        self.globals = _new_globals(bv)
        self.globals["__session_name__"] = self.name
        self.clear_views_cache()


class SessionManager:
    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._sessions: Dict[str, Session] = {}

    def open(self, name: str) -> Session:
        if not name or not isinstance(name, str):
            raise ValueError("session name must be a non-empty string")
        with self._lock:
            sess = self._sessions.get(name)
            if sess is None:
                sess = Session(name=name)
                self._sessions[name] = sess
            return sess

    def get(self, name: str) -> Session:
        with self._lock:
            sess = self._sessions.get(name)
            if sess is None:
                raise KeyError(f"unknown session: {name}")
            return sess

    def list_names(self) -> List[str]:
        with self._lock:
            return sorted(self._sessions.keys())

    def close(self, name: str) -> bool:
        with self._lock:
            return self._sessions.pop(name, None) is not None
