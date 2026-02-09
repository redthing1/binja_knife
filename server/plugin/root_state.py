from __future__ import annotations

import sys
from typing import Any, Dict, Optional

import binaryninja  # type: ignore

from .log import info


_root_globals: Dict[str, Any] = {}
_root_bv: Optional[Any] = None


def root_bv() -> Optional[Any]:
    return _root_bv


def set_root_bv(bv: Optional[Any]) -> None:
    global _root_bv
    _root_bv = bv

    # keep any existing globals dict in sync
    try:
        _root_globals["bv"] = bv
    except Exception:
        pass

    if bv is None:
        info("root bv cleared")
        return

    filename = ""
    try:
        filename = getattr(getattr(bv, "file", None), "filename", None) or ""
    except Exception:
        filename = ""
    info(f"root bv set: {filename or repr(bv)}")


def root_globals() -> Dict[str, Any]:
    return _root_globals


def reset_root_globals() -> None:
    global _root_globals
    _root_globals = {
        "__name__": "__knife_server__",
        "__file__": None,
        "__package__": None,
        "binaryninja": binaryninja,
        "bn": binaryninja,
        "bv": _root_bv,
        "sys": sys,
    }


# initialize on import
reset_root_globals()
