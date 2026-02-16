from __future__ import annotations

from typing import Any, Dict, List, Optional

from .util import enum_name, hex_addr, make_text_matcher


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
    regex: bool = False,
    limit: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if pattern is None:
        raise ValueError("pattern is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    matches_pattern = make_text_matcher(
        pattern,
        case_insensitive=case_insensitive,
        regex=regex,
    )

    results: List[Dict[str, Any]] = []
    for sym in _import_symbols(bv):
        name = getattr(sym, "name", "") or ""
        if not matches_pattern(name):
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
