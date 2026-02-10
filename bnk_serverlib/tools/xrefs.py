from __future__ import annotations

from typing import Any, Dict, List, Optional

from .util import hex_addr, ref_address, ref_function_name, resolve_target_addrs


def xrefs_to(
    *,
    bv: Any,
    target: Any,
    include_code: bool = True,
    include_data: bool = True,
    limit: Optional[int] = None,
) -> List[Dict[str, Any]]:
    if bv is None:
        raise ValueError("bv is required")
    if limit is not None and limit < 0:
        raise ValueError("limit must be >= 0")

    addresses = resolve_target_addrs(bv, target)
    if not addresses:
        raise ValueError("target not found")

    results: List[Dict[str, Any]] = []
    for addr in addresses:
        if include_code:
            for ref in bv.get_code_refs(addr):
                ref_addr = ref_address(ref)
                results.append(
                    {
                        "target": addr,
                        "target_hex": hex_addr(addr),
                        "ref_type": "code",
                        "address": ref_addr,
                        "address_hex": hex_addr(ref_addr),
                        "function": ref_function_name(ref),
                    }
                )
                if limit is not None and len(results) >= limit:
                    return results
        if include_data:
            for ref in bv.get_data_refs(addr):
                ref_addr = ref_address(ref)
                results.append(
                    {
                        "target": addr,
                        "target_hex": hex_addr(addr),
                        "ref_type": "data",
                        "address": ref_addr,
                        "address_hex": hex_addr(ref_addr),
                        "function": ref_function_name(ref),
                    }
                )
                if limit is not None and len(results) >= limit:
                    return results
    return results
