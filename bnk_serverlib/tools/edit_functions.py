from __future__ import annotations

from typing import Any, Dict, Optional

from .edit_common import analysis_update
from .util import resolve_function


def fn_rename(
    *,
    bv: Any,
    name_or_addr: Any,
    new_name: str,
    analysis: str = "none",
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")
    if not new_name:
        raise ValueError("new_name is required")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    old_name = getattr(func, "name", "") or ""
    func.name = new_name

    analysis_update(bv, analysis)

    start = int(getattr(func, "start", 0) or 0)
    return {
        "address": start,
        "address_hex": hex(start),
        "old_name": old_name,
        "new_name": new_name,
    }


def _inject_name(proto: str, name: str) -> Optional[str]:
    if not proto or not name:
        return None
    if name in proto:
        return None
    if "(" not in proto:
        return None
    i = proto.find("(")
    if i <= 0:
        return None
    before = proto[:i].rstrip()
    after = proto[i:]
    if not before:
        return None
    return f"{before} {name}{after}"


def fn_set_type(
    *,
    bv: Any,
    name_or_addr: Any,
    proto: str,
    analysis: str = "update",
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")
    if proto is None:
        raise ValueError("proto is required")
    proto = str(proto).strip()
    if not proto:
        raise ValueError("proto is required")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    old_type = str(getattr(func, "type", ""))

    used_proto = proto
    try:
        func.set_user_type(proto)
    except Exception:
        injected = _inject_name(proto, getattr(func, "name", "") or "")
        if not injected:
            raise
        func.set_user_type(injected)
        used_proto = injected

    analysis_update(bv, analysis)

    new_type = str(getattr(func, "type", ""))
    start = int(getattr(func, "start", 0) or 0)
    return {
        "address": start,
        "address_hex": hex(start),
        "function": getattr(func, "name", "") or "",
        "old_type": old_type,
        "new_type": new_type,
        "proto_used": used_proto,
        "has_user_type": bool(getattr(func, "has_user_type", False)),
    }
