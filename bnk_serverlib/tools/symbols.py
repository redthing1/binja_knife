from __future__ import annotations

from typing import Any, Dict, List, Optional

from .util import enum_name, hex_addr


def symbols_like(
    *,
    bv: Any,
    pattern: str,
    symbol_type: str = "function",
    case_insensitive: bool = True,
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

    needle = pattern.lower() if case_insensitive else pattern

    results: List[Dict[str, Any]] = []
    for sym_type in types:
        try:
            syms = bv.get_symbols_of_type(sym_type) or []
        except Exception:
            continue
        for sym in syms:
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
                return results
    return results
