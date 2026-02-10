from __future__ import annotations

from typing import Any, Dict, List, Optional

from .util import parse_int, resolve_function


def xref_data_add(*, bv: Any, from_addr: Any, to_addr: Any) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    a = parse_int(from_addr)
    b = parse_int(to_addr)
    if a is None or b is None:
        raise ValueError("from_addr and to_addr must be ints or int-like strings")

    bv.add_user_data_ref(a, b)
    return {"from": a, "from_hex": hex(a), "to": b, "to_hex": hex(b)}


def xref_data_remove(*, bv: Any, from_addr: Any, to_addr: Any) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    a = parse_int(from_addr)
    b = parse_int(to_addr)
    if a is None or b is None:
        raise ValueError("from_addr and to_addr must be ints or int-like strings")

    bv.remove_user_data_ref(a, b)
    return {"from": a, "from_hex": hex(a), "to": b, "to_hex": hex(b)}


def _resolve_code_xref_func(bv: Any, from_addr: int, function: Optional[Any]) -> Any:
    if function is not None:
        func = resolve_function(bv, function)
        if func is None:
            raise ValueError("function not found")
        return func

    funcs: List[Any] = bv.get_functions_containing(from_addr) or []
    if not funcs:
        raise ValueError("no function contains from_addr")
    if len(funcs) > 1:
        names = [getattr(f, "name", "") or "" for f in funcs]
        raise ValueError(f"multiple functions contain from_addr: {names}")
    return funcs[0]


def xref_code_add(
    *,
    bv: Any,
    from_addr: Any,
    to_addr: Any,
    function: Optional[Any] = None,
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    a = parse_int(from_addr)
    b = parse_int(to_addr)
    if a is None or b is None:
        raise ValueError("from_addr and to_addr must be ints or int-like strings")

    func = _resolve_code_xref_func(bv, a, function)
    func.add_user_code_ref(a, b)

    start = int(getattr(func, "start", 0) or 0)
    return {
        "function": getattr(func, "name", "") or "",
        "function_addr": start,
        "function_addr_hex": hex(start),
        "from": a,
        "from_hex": hex(a),
        "to": b,
        "to_hex": hex(b),
    }


def xref_code_remove(
    *,
    bv: Any,
    from_addr: Any,
    to_addr: Any,
    function: Optional[Any] = None,
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    a = parse_int(from_addr)
    b = parse_int(to_addr)
    if a is None or b is None:
        raise ValueError("from_addr and to_addr must be ints or int-like strings")

    func = _resolve_code_xref_func(bv, a, function)
    func.remove_user_code_ref(a, b)

    start = int(getattr(func, "start", 0) or 0)
    return {
        "function": getattr(func, "name", "") or "",
        "function_addr": start,
        "function_addr_hex": hex(start),
        "from": a,
        "from_hex": hex(a),
        "to": b,
        "to_hex": hex(b),
    }
