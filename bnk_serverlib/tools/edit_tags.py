from __future__ import annotations

from typing import Any, Dict, Optional

from .util import parse_int, resolve_function


def tag_data_add(
    *,
    bv: Any,
    addr: Any,
    tag_type: str,
    data: str,
    user: bool = True,
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    a = parse_int(addr)
    if a is None:
        raise ValueError("addr must be an int or int-like string")

    tag_type = (tag_type or "").strip()
    if not tag_type:
        raise ValueError("tag_type is required")

    text = "" if data is None else str(data)
    bv.add_tag(a, tag_type, text, user=bool(user))
    return {
        "address": a,
        "address_hex": hex(a),
        "tag_type": tag_type,
        "data": text,
        "user": bool(user),
    }


def tag_data_remove_type(
    *,
    bv: Any,
    addr: Any,
    tag_type: str,
    user: bool = True,
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    a = parse_int(addr)
    if a is None:
        raise ValueError("addr must be an int or int-like string")

    tag_type = (tag_type or "").strip()
    if not tag_type:
        raise ValueError("tag_type is required")

    if user:
        bv.remove_user_data_tags_of_type(a, tag_type)
    else:
        bv.remove_auto_data_tags_of_type(a, tag_type)
    return {
        "address": a,
        "address_hex": hex(a),
        "tag_type": tag_type,
        "user": bool(user),
    }


def tag_func_add(
    *,
    bv: Any,
    name_or_addr: Any,
    tag_type: str,
    data: str,
    addr: Optional[Any] = None,
    auto: bool = False,
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    tag_type = (tag_type or "").strip()
    if not tag_type:
        raise ValueError("tag_type is required")

    text = "" if data is None else str(data)
    addr_int: Optional[int] = None
    if addr is not None:
        addr_int = parse_int(addr)
        if addr_int is None:
            raise ValueError("addr must be an int or int-like string")

    func.add_tag(tag_type, text, addr=addr_int, auto=bool(auto))

    start = int(getattr(func, "start", 0) or 0)
    out = {
        "function": getattr(func, "name", "") or "",
        "function_addr": start,
        "function_addr_hex": hex(start),
        "tag_type": tag_type,
        "data": text,
        "auto": bool(auto),
    }
    if addr_int is not None:
        out["address"] = addr_int
        out["address_hex"] = hex(addr_int)
    return out


def tag_func_remove_type(
    *,
    bv: Any,
    name_or_addr: Any,
    tag_type: str,
    addr: Optional[Any] = None,
    auto: bool = False,
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    tag_type = (tag_type or "").strip()
    if not tag_type:
        raise ValueError("tag_type is required")

    addr_int: Optional[int] = None
    if addr is not None:
        addr_int = parse_int(addr)
        if addr_int is None:
            raise ValueError("addr must be an int or int-like string")

    if addr_int is None:
        if auto:
            func.remove_auto_function_tags_of_type(tag_type)
        else:
            func.remove_user_function_tags_of_type(tag_type)
    else:
        if auto:
            func.remove_auto_address_tags_of_type(addr_int, tag_type)
        else:
            func.remove_user_address_tags_of_type(addr_int, tag_type)

    start = int(getattr(func, "start", 0) or 0)
    out = {
        "function": getattr(func, "name", "") or "",
        "function_addr": start,
        "function_addr_hex": hex(start),
        "tag_type": tag_type,
        "auto": bool(auto),
    }
    if addr_int is not None:
        out["address"] = addr_int
        out["address_hex"] = hex(addr_int)
    return out
