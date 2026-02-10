from __future__ import annotations

from typing import Any, Dict, List, Optional

from .util import hex_addr, resolve_function


def _il_dump(func: Any, il_attr: str, *, max_lines: Optional[int]) -> Dict[str, Any]:
    il_obj = getattr(func, il_attr, None)
    if il_obj is None:
        raise ValueError(f"{il_attr} is not available")

    lines: List[Dict[str, Any]] = []
    for idx, ins in enumerate(il_obj.instructions):
        addr = getattr(ins, "address", None)
        lines.append(
            {
                "idx": idx,
                "address": addr,
                "address_hex": hex_addr(addr),
                "text": str(ins),
            }
        )
        if max_lines is not None and len(lines) >= max_lines:
            break

    count: Optional[int] = getattr(il_obj, "instruction_count", None)
    if not isinstance(count, int):
        count = None
    if count is None:
        try:
            count = len(il_obj)
        except Exception:
            count = None
    if count is None and max_lines is None:
        count = len(lines)

    start = int(getattr(func, "start", 0) or 0)
    return {
        "function": getattr(func, "name", "") or "",
        "address": start,
        "address_hex": hex_addr(start),
        "il": il_attr,
        "count": count,
        "lines": lines,
    }


def hlil(
    *, bv: Any, name_or_addr: Any, max_lines: Optional[int] = None
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")
    if max_lines is not None and max_lines < 0:
        raise ValueError("max_lines must be >= 0")
    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")
    return _il_dump(func, "hlil", max_lines=max_lines)


def mlil(
    *, bv: Any, name_or_addr: Any, max_lines: Optional[int] = None
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")
    if max_lines is not None and max_lines < 0:
        raise ValueError("max_lines must be >= 0")
    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")
    return _il_dump(func, "mlil", max_lines=max_lines)


def llil(
    *, bv: Any, name_or_addr: Any, max_lines: Optional[int] = None
) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")
    if max_lines is not None and max_lines < 0:
        raise ValueError("max_lines must be >= 0")
    func = resolve_function(bv, name_or_addr)
    if func is None:
        raise ValueError("function not found")
    return _il_dump(func, "llil", max_lines=max_lines)
