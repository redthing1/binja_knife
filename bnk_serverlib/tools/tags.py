from __future__ import annotations

from typing import Any, Dict, List, Optional

from .util import enum_name, hex_addr, parse_int, resolve_function


def tags_types(*, bv: Any) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")

    # bv.tag_types is documented as name -> TagType (but can inconsistently return lists)
    mapping = getattr(bv, "tag_types", {}) or {}

    types: List[Any] = []
    for value in mapping.values():
        if isinstance(value, list):
            types.extend(value)
        else:
            types.append(value)

    results: List[Dict[str, Any]] = []
    for tt in types:
        if tt is None:
            continue
        results.append(
            {
                "name": getattr(tt, "name", "") or "",
                "id": getattr(tt, "id", "") or "",
                "icon": getattr(tt, "icon", "") or "",
                "type": enum_name(getattr(tt, "type", None)),
                "visible": bool(getattr(tt, "visible", False)),
            }
        )
    return sorted(results, key=lambda r: (r.get("name") or "").lower())


def _tag_dict(tag: Any, *, address: Optional[int] = None) -> Dict[str, Any]:
    tt = getattr(tag, "type", None)
    out = {
        "tag_type": getattr(tt, "name", "") or "",
        "tag_icon": getattr(tt, "icon", "") or "",
        "tag_id": getattr(tag, "id", "") or "",
        "tag_data": getattr(tag, "data", "") or "",
        "tag_type_id": getattr(tt, "id", "") or "",
        "tag_type_type": enum_name(getattr(tt, "type", None)),
        "tag_type_visible": bool(getattr(tt, "visible", False)),
    }
    if address is not None:
        out["address"] = address
        out["address_hex"] = hex_addr(address)
    return out


def tags_list(
    *,
    bv: Any,
    auto: Optional[bool] = None,
    tag_type: Optional[str] = None,
    limit: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    type_filter = (tag_type or "").strip().lower() or None

    results: List[Dict[str, Any]] = []
    for addr, tag in bv.get_tags(auto=auto) or []:
        if type_filter:
            tt = getattr(tag, "type", None)
            name = (getattr(tt, "name", "") or "").strip().lower()
            if name != type_filter:
                continue
        addr_int: Optional[int]
        try:
            addr_int = int(addr)
        except Exception:
            addr_int = None
        results.append(_tag_dict(tag, address=addr_int))
        if limit is not None and len(results) >= limit:
            break
    return results


def tags_at(
    *,
    bv: Any,
    addr: Any,
    auto: Optional[bool] = None,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")

    addr_int = parse_int(addr)
    if addr_int is None:
        raise ValueError("addr must be an int or int-like string")

    results: List[Dict[str, Any]] = []
    for tag in bv.get_tags_at(addr_int, auto=auto) or []:
        results.append(_tag_dict(tag, address=addr_int))
    return results


def tags_function(
    *,
    bv: Any,
    name_or_addr: Any,
    auto: Optional[bool] = None,
    tag_type: Optional[str] = None,
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    tags = func.get_function_tags(auto=auto, tag_type=tag_type) or []
    out_tags: List[Dict[str, Any]] = []
    for tag in tags:
        out_tags.append(_tag_dict(tag))

    start = int(getattr(func, "start", 0) or 0)
    return {
        "function": getattr(func, "name", "") or "",
        "address": start,
        "address_hex": hex_addr(start),
        "tags": out_tags,
    }
