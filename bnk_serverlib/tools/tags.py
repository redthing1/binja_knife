from __future__ import annotations

from typing import Any, Dict, List, Optional

from .util import enum_name, hex_addr, parse_int, resolve_function


def _tag_type_name(tag: Any) -> str:
    tt = getattr(tag, "type", None)
    return (getattr(tt, "name", "") or "").strip()


def _tag_unique_key(
    tag: Any, *, address: Optional[int] = None
) -> tuple[Optional[int], str]:
    tid = getattr(tag, "id", None)
    tid_str = "" if tid is None else str(tid)
    if not tid_str:
        tid_str = repr(tag)
    return (address, tid_str)


def _tags_union(
    user_items: list[tuple[Any, Any]],
    auto_items: list[tuple[Any, Any]],
) -> list[tuple[Any, Any]]:
    seen: set[tuple[Optional[int], str]] = set()
    out: list[tuple[Any, Any]] = []
    for addr, tag in list(user_items) + list(auto_items):
        addr_int: Optional[int]
        try:
            addr_int = int(addr)
        except Exception:
            addr_int = None
        key = _tag_unique_key(tag, address=addr_int)
        if key in seen:
            continue
        seen.add(key)
        out.append((addr, tag))
    return out


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
    if auto is None:
        items = _tags_union(
            list(bv.get_tags(auto=False) or []),
            list(bv.get_tags(auto=True) or []),
        )
    else:
        items = list(bv.get_tags(auto=auto) or [])

    for addr, tag in items:
        if type_filter:
            if _tag_type_name(tag).lower() != type_filter:
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
    limit: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    addr_int = parse_int(addr)
    if addr_int is None:
        raise ValueError("addr must be an int or int-like string")

    results: List[Dict[str, Any]] = []
    if auto is None:
        tags = list(bv.get_tags_at(addr_int, auto=False) or []) + list(
            bv.get_tags_at(addr_int, auto=True) or []
        )
        # Best-effort de-dupe; addr is constant here.
        seen: set[tuple[Optional[int], str]] = set()
        uniq: list[Any] = []
        for tag in tags:
            key = _tag_unique_key(tag, address=addr_int)
            if key in seen:
                continue
            seen.add(key)
            uniq.append(tag)
        tags = uniq
    else:
        tags = list(bv.get_tags_at(addr_int, auto=auto) or [])

    for tag in tags:
        results.append(_tag_dict(tag, address=addr_int))
        if limit is not None and len(results) >= limit:
            break
    return results


def tags_function(
    *,
    bv: Any,
    name_or_addr: Any,
    auto: Optional[bool] = None,
    tag_type: Optional[str] = None,
    limit: Optional[int] = None,
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    type_filter = (tag_type or "").strip().lower() or None

    # Prefer doing filtering ourselves: BN APIs have varied over time wrt tag_type type.
    if auto is None:
        tags = list(func.get_function_tags(auto=False) or []) + list(
            func.get_function_tags(auto=True) or []
        )
        seen: set[tuple[Optional[int], str]] = set()
        uniq: list[Any] = []
        for tag in tags:
            key = _tag_unique_key(tag)
            if key in seen:
                continue
            seen.add(key)
            uniq.append(tag)
        tags = uniq
    else:
        tags = list(func.get_function_tags(auto=auto) or [])

    out_tags: List[Dict[str, Any]] = []
    for tag in tags:
        if type_filter and _tag_type_name(tag).lower() != type_filter:
            continue
        out_tags.append(_tag_dict(tag))
        if limit is not None and len(out_tags) >= limit:
            break

    start = int(getattr(func, "start", 0) or 0)
    return {
        "function": getattr(func, "name", "") or "",
        "address": start,
        "address_hex": hex_addr(start),
        "tags": out_tags,
    }
