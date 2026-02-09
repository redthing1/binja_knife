from __future__ import annotations

import threading
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


@dataclass
class Session:
    name: str
    lock: threading.RLock = field(default_factory=threading.RLock)
    bv: Optional[Any] = None
    globals: Dict[str, Any] = field(default_factory=dict)
    # cached results from the most recent view listing: list of (binaryview, info dict)
    views_cache: List[Tuple[Any, Dict[str, Any]]] = field(default_factory=list)
    views_cache_include_unnamed: bool = False

    def __post_init__(self) -> None:
        self.globals = _new_globals(self.bv)
        self.globals["__session_name__"] = self.name

    def set_bv(self, bv: Optional[Any]) -> None:
        self.bv = bv
        self.globals["bv"] = bv

    def reset(self, keep_bv: bool = True) -> None:
        bv = self.bv if keep_bv else None
        self.bv = bv
        self.globals = _new_globals(bv)
        self.globals["__session_name__"] = self.name


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
