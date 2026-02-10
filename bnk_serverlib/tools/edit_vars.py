from __future__ import annotations

from typing import Any, Dict, List

from .edit_common import analysis_update, parse_type_string
from .util import enum_name, parse_int, resolve_function


def _var_dict(var: Any) -> Dict[str, Any]:
    ident = int(getattr(var, "identifier", 0) or 0)
    storage = getattr(var, "storage", None)
    index = getattr(var, "index", None)

    try:
        name = getattr(var, "name", "") or ""
    except Exception:
        name = ""
    last_seen_name = getattr(var, "last_seen_name", "") or ""

    ty_obj = getattr(var, "type", None)
    ty = "" if ty_obj is None else str(ty_obj)

    out: Dict[str, Any] = {
        "identifier": ident,
        "identifier_hex": hex(ident),
        "name": name,
        "last_seen_name": last_seen_name,
        "type": ty,
        "source_type": enum_name(getattr(var, "source_type", None)),
        "is_parameter": bool(getattr(var, "is_parameter_variable", False)),
    }
    if isinstance(storage, int):
        out["storage"] = storage
        out["storage_hex"] = hex(storage)
    if isinstance(index, int):
        out["index"] = index
    return out


def var_list(*, bv: Any, name_or_addr: Any) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    results: List[Dict[str, Any]] = []
    for var in getattr(func, "vars", []) or []:
        results.append(_var_dict(var))

    start = int(getattr(func, "start", 0) or 0)
    return {
        "function": getattr(func, "name", "") or "",
        "address": start,
        "address_hex": hex(start),
        "count": len(results),
        "vars": results,
    }


def _resolve_var(func: Any, var_spec: Any, by: str) -> Any:
    mode = (by or "auto").strip().lower()
    if mode not in {"auto", "ident", "name"}:
        raise ValueError("by must be one of: auto, ident, name")

    if mode in {"auto", "ident"}:
        ident = parse_int(var_spec)
        if ident is not None:
            from binaryninja.variable import Variable  # type: ignore

            return Variable.from_identifier(func, ident)
        if mode == "ident":
            raise ValueError("var must be an int or int-like string when --by ident")

    if mode in {"auto", "name"}:
        name = str(var_spec or "").strip()
        if not name:
            raise ValueError("var name is required")
        v = func.get_variable_by_name(name)
        if v is None:
            raise ValueError("variable not found")
        return v

    raise ValueError("variable not found")


def var_rename(
    *,
    bv: Any,
    name_or_addr: Any,
    var: Any,
    new_name: str,
    by: str = "auto",
    analysis: str = "update",
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")
    if not new_name:
        raise ValueError("new_name is required")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    v = _resolve_var(func, var, by)

    before = _var_dict(v)
    v.set_name_async(new_name)
    analysis_update(bv, analysis)
    after = _var_dict(v)

    start = int(getattr(func, "start", 0) or 0)
    return {
        "function": getattr(func, "name", "") or "",
        "address": start,
        "address_hex": hex(start),
        "before": before,
        "after": after,
    }


def var_set_type(
    *,
    bv: Any,
    name_or_addr: Any,
    var: Any,
    type: str,
    by: str = "auto",
    analysis: str = "update",
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    v = _resolve_var(func, var, by)

    ty, _name = parse_type_string(bv, type)

    before = _var_dict(v)
    v.set_type_async(ty)
    analysis_update(bv, analysis)
    after = _var_dict(v)

    start = int(getattr(func, "start", 0) or 0)
    return {
        "function": getattr(func, "name", "") or "",
        "address": start,
        "address_hex": hex(start),
        "type_input": str(type),
        "before": before,
        "after": after,
    }
