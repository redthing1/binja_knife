from __future__ import annotations

from typing import Any, Dict

from .util import parse_int, resolve_function


def comment_view_set(*, bv: Any, addr: Any, comment: str) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    a = parse_int(addr)
    if a is None:
        raise ValueError("addr must be an int or int-like string")

    text = "" if comment is None else str(comment)
    bv.set_comment_at(a, text)
    return {"address": a, "address_hex": hex(a), "comment": text}


def comment_func_set(
    *,
    bv: Any,
    name_or_addr: Any,
    addr: Any,
    comment: str,
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    a = parse_int(addr)
    if a is None:
        raise ValueError("addr must be an int or int-like string")

    text = "" if comment is None else str(comment)
    func.set_comment_at(a, text)

    start = int(getattr(func, "start", 0) or 0)
    return {
        "function": getattr(func, "name", "") or "",
        "function_addr": start,
        "function_addr_hex": hex(start),
        "address": a,
        "address_hex": hex(a),
        "comment": text,
    }
