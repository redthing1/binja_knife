from __future__ import annotations

from typing import Any, Dict, List, Optional

from .util import enum_name, hex_addr, make_text_matcher


def symbols_like(
    *,
    bv: Any,
    pattern: str,
    symbol_type: str = "function",
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

    from binaryninja.enums import SymbolType

    symbol_map = {
        "function": [SymbolType.FunctionSymbol, SymbolType.ImportedFunctionSymbol],
        "import": [SymbolType.ImportedFunctionSymbol],
        "import_address": [SymbolType.ImportAddressSymbol],
        "data": [SymbolType.DataSymbol],
        "external": [SymbolType.ExternalSymbol],
    }

    types = symbol_map.get((symbol_type or "").lower())
    if not types:
        raise ValueError(f"unknown symbol_type: {symbol_type}")

    matches_pattern = make_text_matcher(
        pattern,
        case_insensitive=case_insensitive,
        regex=regex,
    )

    results: List[Dict[str, Any]] = []
    for sym_type in types:
        try:
            syms = bv.get_symbols_of_type(sym_type) or []
        except Exception:
            continue
        for sym in syms:
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
                return results
    return results
