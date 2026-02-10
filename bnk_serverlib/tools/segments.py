from __future__ import annotations

from typing import Any, Dict, List

from .util import hex_addr


def segments_list(*, bv: Any) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")

    results: List[Dict[str, Any]] = []
    for seg in getattr(bv, "segments", []) or []:
        start = int(getattr(seg, "start", 0) or 0)
        end = int(getattr(seg, "end", 0) or 0)
        length = int(getattr(seg, "length", 0) or (end - start))

        data_offset = int(getattr(seg, "data_offset", 0) or 0)
        data_end = int(getattr(seg, "data_end", 0) or 0)
        data_length = int(getattr(seg, "data_length", 0) or 0)

        results.append(
            {
                "start": start,
                "end": end,
                "length": length,
                "start_hex": hex_addr(start),
                "end_hex": hex_addr(end),
                "length_hex": hex_addr(length),
                "data_offset": data_offset,
                "data_end": data_end,
                "data_length": data_length,
                "data_offset_hex": hex_addr(data_offset),
                "data_end_hex": hex_addr(data_end),
                "data_length_hex": hex_addr(data_length),
                "readable": bool(getattr(seg, "readable", False)),
                "writable": bool(getattr(seg, "writable", False)),
                "executable": bool(getattr(seg, "executable", False)),
                "auto_defined": bool(getattr(seg, "auto_defined", False)),
            }
        )
    return results

