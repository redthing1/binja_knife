from __future__ import annotations

from typing import Any, Dict, List, Optional

from .util import enum_name, hex_addr


def _import_symbols(bv: Any):
    from binaryninja.enums import SymbolType

    for sym_type in (SymbolType.ImportedFunctionSymbol, SymbolType.ImportAddressSymbol):
        try:
            syms = bv.get_symbols_of_type(sym_type) or []
        except Exception:
            continue
        for sym in syms:
            yield sym


def imports_list(*, bv: Any, limit: Optional[int] = None) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    results: List[Dict[str, Any]] = []
    for sym in _import_symbols(bv):
        addr = getattr(sym, "address", None)
        results.append(
            {
                "name": getattr(sym, "name", "") or "",
                "address": addr,
                "address_hex": hex_addr(addr),
                "type": enum_name(getattr(sym, "type", None)),
            }
        )
        if limit is not None and len(results) >= limit:
            break
    return results


def imports_like(
    *,
    bv: Any,
    pattern: str,
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
    for sym in _import_symbols(bv):
        name = getattr(sym, "name", "") or ""
        hay = name.lower() if case_insensitive else name
        if needle not in hay:
            continue
        addr = getattr(sym, "address", None)
        results.append(
            {
                "name": name,
                "address": addr,
                "address_hex": hex_addr(addr),
                "type": enum_name(getattr(sym, "type", None)),
            }
        )
        if limit is not None and len(results) >= limit:
            break
    return results
