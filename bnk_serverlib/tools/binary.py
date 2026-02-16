from __future__ import annotations

from typing import Any, Dict, List

from .functions import functions_list
from .imports import imports_list
from .sections import sections_list
from .segments import segments_list
from .util import enum_name, hex_addr


def _count_and_sample_strings(
    bv: Any, *, sample_limit: int
) -> tuple[int, List[Dict[str, Any]]]:
    if sample_limit < 0:
        raise ValueError("string_sample_limit must be >= 0")

    count = 0
    sample: List[Dict[str, Any]] = []
    for sref in bv.get_strings():
        count += 1
        if len(sample) >= sample_limit:
            continue
        sample.append(
            {
                "address": sref.start,
                "address_hex": hex_addr(sref.start),
                "value": str(sref.value),
                "type": enum_name(sref.type),
                "length": sref.length,
            }
        )
    return count, sample


def binary_summary(
    *,
    bv: Any,
    function_sample_limit: int = 10,
    import_sample_limit: int = 10,
    string_sample_limit: int = 10,
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")
    if function_sample_limit < 0:
        raise ValueError("function_sample_limit must be >= 0")
    if import_sample_limit < 0:
        raise ValueError("import_sample_limit must be >= 0")
    if string_sample_limit < 0:
        raise ValueError("string_sample_limit must be >= 0")

    start = int(getattr(bv, "start", 0) or 0)
    end = int(getattr(bv, "end", 0) or 0)
    length = int(getattr(bv, "length", 0) or 0)
    entry_point = getattr(bv, "entry_point", None)
    entry_addr = int(entry_point) if isinstance(entry_point, int) else None

    bv_file = getattr(bv, "file", None)
    file_path = getattr(bv_file, "filename", "") or ""
    file_name = getattr(bv_file, "original_filename", "") or ""

    sections = sections_list(bv=bv)
    segments = segments_list(bv=bv)
    function_count = len(getattr(bv, "functions", []) or [])
    import_count = len(imports_list(bv=bv))
    string_count, string_samples = _count_and_sample_strings(
        bv,
        sample_limit=string_sample_limit,
    )

    function_samples = functions_list(
        bv=bv,
        include_imports=True,
        limit=function_sample_limit,
    )
    import_samples = imports_list(
        bv=bv,
        limit=import_sample_limit,
    )

    return {
        "file": {
            "path": file_path,
            "name": file_name,
        },
        "view": {
            "name": getattr(bv, "name", "") or "",
            "view_type": getattr(bv, "view_type", "") or "",
            "analysis_state": enum_name(getattr(bv, "analysis_state", None)),
            "arch": getattr(getattr(bv, "arch", None), "name", "") or "",
            "platform": getattr(getattr(bv, "platform", None), "name", "") or "",
        },
        "address_space": {
            "start": start,
            "start_hex": hex_addr(start),
            "end": end,
            "end_hex": hex_addr(end),
            "length": length,
            "length_hex": hex_addr(length),
            "entry_point": entry_addr,
            "entry_point_hex": hex_addr(entry_addr),
        },
        "counts": {
            "functions": function_count,
            "imports": import_count,
            "strings": string_count,
            "sections": len(sections),
            "segments": len(segments),
        },
        "samples": {
            "functions": function_samples,
            "imports": import_samples,
            "strings": string_samples,
        },
        "sections": sections,
        "segments": segments,
    }
