from __future__ import annotations

from typing import Any, Dict, List, Optional

from .util import enum_name, hex_addr, ref_address, ref_function_name, section_range


def strings_like(
    *,
    bv: Any,
    pattern: str,
    section: Optional[str] = None,
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

    start = length = None
    if section:
        sec = section_range(bv, section)
        if not sec:
            raise ValueError(f"unknown section: {section}")
        start, end = sec
        length = end - start

    matches: List[Dict[str, Any]] = []
    strings = bv.get_strings(start, length) if start is not None else bv.get_strings()
    for sref in strings:
        value = str(sref.value)
        hay = value.lower() if case_insensitive else value
        if needle not in hay:
            continue
        matches.append(
            {
                "address": sref.start,
                "address_hex": hex_addr(sref.start),
                "value": value,
                "type": enum_name(sref.type),
                "length": sref.length,
            }
        )
        if limit is not None and len(matches) >= limit:
            break
    return matches


def _extract_cstring(
    bv: Any, addr: int, *, max_back: int = 96, max_len: int = 256
) -> str:
    start = addr - max_back if addr > max_back else addr
    data = bytes(bv.read(start, max_back + max_len))
    rel = addr - start
    before = data.rfind(b"\x00", 0, rel)
    before = 0 if before == -1 else before + 1
    after = data.find(b"\x00", rel)
    after = len(data) if after == -1 else after
    return data[before:after].decode("utf-8", errors="ignore")


def strings_like_data(
    *,
    bv: Any,
    pattern: str,
    section: Optional[str] = None,
    case_insensitive: bool = True,
    limit: Optional[int] = None,
    max_len: int = 256,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if not pattern:
        raise ValueError("pattern is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    from binaryninja.enums import FindFlag

    needle = pattern.encode("utf-8", errors="ignore")
    flags = (
        FindFlag.FindCaseInsensitive if case_insensitive else FindFlag.FindCaseSensitive
    )

    start = length = None
    if section:
        sec = section_range(bv, section)
        if not sec:
            raise ValueError(f"unknown section: {section}")
        start, end = sec
        length = end - start

    if start is None:
        start = bv.start
        length = bv.length
    end = start + (length or 0)

    results: List[Dict[str, Any]] = []
    for addr, _buf in bv.find_all_data(start, end, needle, flags):
        results.append(
            {
                "address": addr,
                "address_hex": hex_addr(addr),
                "string": _extract_cstring(bv, addr, max_len=max_len),
            }
        )
        if limit is not None and len(results) >= limit:
            break
    return results


def xrefs_to_string(
    *,
    bv: Any,
    pattern: str,
    section: Optional[str] = None,
    case_insensitive: bool = True,
    string_limit: Optional[int] = None,
    xref_limit: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if not pattern:
        raise ValueError("pattern is required")
    if string_limit is not None and string_limit < 0:
        raise ValueError("string_limit must be >= 0")
    if xref_limit is not None and xref_limit < 0:
        raise ValueError("xref_limit must be >= 0")

    matches = strings_like_data(
        bv=bv,
        pattern=pattern,
        section=section,
        case_insensitive=case_insensitive,
        limit=string_limit,
    )

    results: List[Dict[str, Any]] = []
    for match in matches:
        addr = match.get("address")
        if addr is None:
            continue

        refs: List[Dict[str, Any]] = []
        for ref in bv.get_code_refs(addr):
            ref_addr = ref_address(ref)
            refs.append(
                {
                    "ref_type": "code",
                    "address": ref_addr,
                    "address_hex": hex_addr(ref_addr),
                    "function": ref_function_name(ref),
                }
            )
            if xref_limit is not None and len(refs) >= xref_limit:
                break

        if xref_limit is None or len(refs) < xref_limit:
            for ref in bv.get_data_refs(addr):
                ref_addr = ref_address(ref)
                refs.append(
                    {
                        "ref_type": "data",
                        "address": ref_addr,
                        "address_hex": hex_addr(ref_addr),
                        "function": ref_function_name(ref),
                    }
                )
                if xref_limit is not None and len(refs) >= xref_limit:
                    break

        results.append(
            {
                "address": addr,
                "address_hex": hex_addr(addr),
                "string": match.get("string", ""),
                "refs": refs,
            }
        )
    return results
