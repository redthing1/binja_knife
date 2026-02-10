from __future__ import annotations

from typing import Any, Dict, List, Optional

from .util import enum_name, hex_addr, ref_address, resolve_function


def _is_import_function(func: Any) -> bool:
    sym = getattr(func, "symbol", None)
    sym_type = getattr(sym, "type", None)
    name = enum_name(sym_type)
    return name in {"ImportedFunctionSymbol", "ImportAddressSymbol"}


def functions_list(
    *,
    bv: Any,
    include_imports: bool = True,
    limit: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    results: List[Dict[str, Any]] = []
    for func in bv.functions:
        if not include_imports and _is_import_function(func):
            continue

        start = int(getattr(func, "start", 0) or 0)
        results.append(
            {
                "name": getattr(func, "name", "") or "",
                "start": start,
                "start_hex": hex_addr(start),
            }
        )
        if limit is not None and len(results) >= limit:
            break
    return results


def functions_like(
    *,
    bv: Any,
    pattern: str,
    include_imports: bool = True,
    case_insensitive: bool = True,
    limit: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if pattern is None:
        raise ValueError("pattern is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    needle = pattern.lower() if case_insensitive else pattern

    results: List[Dict[str, Any]] = []
    for func in bv.functions:
        if not include_imports and _is_import_function(func):
            continue
        name = getattr(func, "name", "") or ""
        hay = name.lower() if case_insensitive else name
        if needle not in hay:
            continue

        start = int(getattr(func, "start", 0) or 0)
        results.append(
            {
                "name": name,
                "start": start,
                "start_hex": hex_addr(start),
            }
        )
        if limit is not None and len(results) >= limit:
            break
    return results


def function_summary(*, bv: Any, name_or_addr: Any) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    calling_conv = getattr(func, "calling_convention", None)
    arch = getattr(func, "arch", None)

    total_bytes = int(getattr(func, "total_bytes", 0) or 0)
    total_bytes_hex = hex_addr(total_bytes)

    try:
        basic_blocks = len(list(func.basic_blocks))
    except Exception:
        basic_blocks = 0

    return {
        "name": getattr(func, "name", "") or "",
        "address": int(getattr(func, "start", 0) or 0),
        "address_hex": hex_addr(int(getattr(func, "start", 0) or 0)),
        "arch": getattr(arch, "name", "") or "",
        "calling_convention": getattr(calling_conv, "name", "") or "",
        "total_bytes": total_bytes,
        "total_bytes_hex": total_bytes_hex,
        "basic_blocks": basic_blocks,
        "too_large": bool(getattr(func, "too_large", False)),
        "type": str(getattr(func, "type", "")),
    }


def function_callers(
    *,
    bv: Any,
    name_or_addr: Any,
    limit: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    results: List[Dict[str, Any]] = []
    for caller in getattr(func, "callers", []):
        start = int(getattr(caller, "start", 0) or 0)
        results.append(
            {
                "name": getattr(caller, "name", "") or "",
                "address": start,
                "address_hex": hex_addr(start),
            }
        )
        if limit is not None and len(results) >= limit:
            break
    return results


def function_callees(
    *,
    bv: Any,
    name_or_addr: Any,
    limit: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    results: List[Dict[str, Any]] = []
    for callee in getattr(func, "callees", []):
        start = int(getattr(callee, "start", 0) or 0)
        results.append(
            {
                "name": getattr(callee, "name", "") or "",
                "address": start,
                "address_hex": hex_addr(start),
            }
        )
        if limit is not None and len(results) >= limit:
            break
    return results


def function_call_sites(
    *,
    bv: Any,
    name_or_addr: Any,
    limit: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")

    results: List[Dict[str, Any]] = []
    for ref in getattr(func, "call_sites", []):
        addr = ref_address(ref)
        results.append(
            {
                "address": addr,
                "address_hex": hex_addr(addr),
                "function": getattr(func, "name", "") or "",
            }
        )
        if limit is not None and len(results) >= limit:
            break
    return results
