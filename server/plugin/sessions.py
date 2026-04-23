from __future__ import annotations

import threading
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any, Dict, Optional

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


def _safe_getattr(obj: Any, name: str, default: Any = "") -> Any:
    try:
        return getattr(obj, name)
    except Exception:
        return default


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


def canonical_session_path(path: str) -> str:
    raw = str(path or "").strip()
    if not raw:
        return ""
    try:
        return str(Path(raw).expanduser().resolve(strict=False))
    except Exception:
        return raw


@dataclass
class Session:
    name: str
    lock: threading.RLock = field(default_factory=threading.RLock)
    bv: Optional[Any] = None
    owns_bv: bool = False
    owned_path: str = ""
    globals: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self) -> None:
        self.globals = _new_globals(self.bv)
        self.globals["__session_name__"] = self.name

    def set_bv(
        self,
        bv: Optional[Any],
        *,
        owned: bool = False,
        owned_path: str = "",
    ) -> Dict[str, Any]:
        prev_bv = self.bv
        prev_owned = self.owns_bv
        prev_owned_path = self.owned_path
        replaced = prev_bv is not None and prev_bv is not bv
        previous_closed = False

        # Close previously loaded views to avoid leaked references / locked DB handles.
        if replaced and prev_owned:
            previous_closed = _safe_close_bv(prev_bv)

        self.bv = bv
        self.owns_bv = bool(owned and bv is not None)
        self.owned_path = str(owned_path or "") if self.owns_bv else ""
        self.globals["bv"] = bv
        return {
            "replaced": replaced,
            "previous_owned_path": prev_owned_path,
            "previous_closed": previous_closed,
        }

    def snapshot(self, *, busy: bool = False) -> Dict[str, Any]:
        if self.bv is None:
            return {
                "name": self.name,
                "mode": "empty",
                "target": "",
                "busy": bool(busy),
            }

        info: Dict[str, Any] = {
            "name": self.name,
            "mode": "load" if self.owns_bv else "attach",
            "target": _safe_filename(self.bv),
            "busy": bool(busy),
        }
        arch = _safe_getattr(self.bv, "arch", None)
        analysis_state = _safe_getattr(self.bv, "analysis_state", None)
        info.update(
            {
                "view_type": _safe_getattr(self.bv, "view_type", "") or "",
                "arch": _safe_getattr(arch, "name", "") or str(arch or ""),
                "analysis_state": _safe_getattr(analysis_state, "name", "")
                or str(analysis_state or ""),
            }
        )
        return info

    def detach_bv(self, *, close_owned: bool = True) -> Dict[str, Any]:
        prev_bv = self.bv
        prev_owned = self.owns_bv
        prev_owned_path = self.owned_path
        had_attached = prev_bv is not None
        closed = False
        if had_attached and close_owned and prev_owned:
            closed = _safe_close_bv(prev_bv)

        self.bv = None
        self.owns_bv = False
        self.owned_path = ""
        self.globals["bv"] = None
        return {
            "had_attached": had_attached,
            "previous_owned_path": prev_owned_path,
            "closed": closed,
        }

    def reset(self, keep_bv: bool = True) -> Dict[str, Any]:
        out: Dict[str, Any] = {"keep_bv": bool(keep_bv), "previous_owned_path": ""}
        if not keep_bv:
            out = self.detach_bv(close_owned=True)

        bv = self.bv if keep_bv else None
        owns_bv = self.owns_bv if keep_bv else False
        owned_path = self.owned_path if keep_bv else ""
        self.bv = bv
        self.owns_bv = owns_bv
        self.owned_path = owned_path
        self.globals = _new_globals(bv)
        self.globals["__session_name__"] = self.name
        return out


class SessionManager:
    def __init__(self) -> None:
        self._lock = threading.RLock()
        self._sessions: Dict[str, Session] = {}
        self._owned_path_claims: Dict[str, str] = {}

    def open(self, name: str) -> Session:
        sess, _created = self.open_with_created(name)
        return sess

    def open_with_created(self, name: str) -> tuple[Session, bool]:
        if not name or not isinstance(name, str):
            raise ValueError("session name must be a non-empty string")
        with self._lock:
            sess = self._sessions.get(name)
            if sess is None:
                sess = Session(name=name)
                self._sessions[name] = sess
                return sess, True
            return sess, False

    def get(self, name: str) -> Session:
        with self._lock:
            sess = self._sessions.get(name)
            if sess is None:
                raise KeyError(f"unknown session: {name}")
            return sess

    def get_optional(self, name: str) -> Optional[Session]:
        with self._lock:
            return self._sessions.get(name)

    def list_names(self) -> list[str]:
        with self._lock:
            return sorted(self._sessions.keys())

    def close(self, name: str) -> bool:
        with self._lock:
            return self._sessions.pop(name, None) is not None

    def claim_owned_path(self, session_name: str, path: str) -> str:
        canonical = canonical_session_path(path)
        if not canonical:
            return ""
        with self._lock:
            owner = self._owned_path_claims.get(canonical)
            if owner is not None and owner != session_name:
                raise ValueError(
                    f"path is already loaded by session {owner!r}: {canonical}"
                )
            self._owned_path_claims[canonical] = session_name
        return canonical

    def release_owned_path(self, session_name: str, path: str) -> None:
        canonical = canonical_session_path(path)
        if not canonical:
            return
        with self._lock:
            if self._owned_path_claims.get(canonical) == session_name:
                self._owned_path_claims.pop(canonical, None)
