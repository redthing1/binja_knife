from __future__ import annotations

from typing import Any, Dict, List

from .util import enum_name, hex_addr


def sections_list(*, bv: Any) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")

    results: List[Dict[str, Any]] = []
    for sec in bv.sections.values():
        start = int(getattr(sec, "start", 0) or 0)
        end = int(getattr(sec, "end", 0) or 0)
        length = int(getattr(sec, "length", 0) or (end - start))
        results.append(
            {
                "name": getattr(sec, "name", "") or "",
                "start": start,
                "end": end,
                "length": length,
                "start_hex": hex_addr(start),
                "end_hex": hex_addr(end),
                "length_hex": hex_addr(length),
                "semantics": enum_name(getattr(sec, "semantics", None)),
            }
        )
    return results
