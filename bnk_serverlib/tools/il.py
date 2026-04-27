from __future__ import annotations

from typing import Any, Dict, Iterable, Iterator, Optional

from .util import hex_addr, resolve_function


def _line_text(value: Any) -> str:
    text = str(value).rstrip("\n")
    return "" if not text.strip() else text.rstrip()


def _instruction_lines(il_obj: Any) -> Iterator[str]:
    for idx, ins in enumerate(il_obj.instructions):
        addr = hex_addr(getattr(ins, "address", None))
        prefix = f"{idx:4}"
        if addr:
            prefix = f"{prefix} @ {addr}"
        yield f"{prefix}  {_line_text(ins)}"


def _hlil_lines(il_obj: Any) -> Optional[Iterator[str]]:
    root = getattr(il_obj, "root", None)
    lines = getattr(root, "lines", None) if root is not None else None
    if lines is None:
        return None
    return (_line_text(line) for line in lines)


def _linear_lines(func: Any, il_attr: str) -> Optional[Iterator[str]]:
    try:
        from binaryninja.lineardisassembly import LinearViewCursor, LinearViewObject
    except Exception:
        return None

    factory = getattr(LinearViewObject, f"single_function_{il_attr}", None)
    if factory is None:
        return None

    try:
        cursor = LinearViewCursor(factory(func))
        cursor.seek_to_begin()
    except Exception:
        return None

    def generate() -> Iterator[str]:
        if cursor.valid and not cursor.after_end:
            cursor.next()
        while cursor.valid and not cursor.after_end:
            for item in cursor.lines:
                line = getattr(item, "contents", item)
                yield _line_text(line)
            cursor.next()

    return generate()


def _rendered_lines(func: Any, il_obj: Any, il_attr: str) -> Iterable[str]:
    if il_attr == "hlil":
        lines = _hlil_lines(il_obj)
        if lines is not None:
            return lines
    elif il_attr in {"mlil", "llil"}:
        lines = _linear_lines(func, il_attr)
        if lines is not None:
            return lines

    return _instruction_lines(il_obj)


def _collect_text(
    lines: Iterable[str], *, max_lines: Optional[int]
) -> tuple[str, int, bool]:
    out: list[str] = []
    for idx, line in enumerate(lines):
        if max_lines is not None and idx >= max_lines:
            return "\n".join(out), len(out), True
        out.append(line)
    return "\n".join(out), len(out), False


def _il_dump(func: Any, il_attr: str, *, max_lines: Optional[int]) -> Dict[str, Any]:
    il_obj = getattr(func, il_attr, None)
    if il_obj is None:
        raise ValueError(f"{il_attr} is not available")

    text, line_count, truncated = _collect_text(
        _rendered_lines(func, il_obj, il_attr), max_lines=max_lines
    )

    start = int(getattr(func, "start", 0) or 0)
    return {
        "function": getattr(func, "name", "") or "",
        "address": start,
        "address_hex": hex_addr(start),
        "il": il_attr,
        "line_count": line_count,
        "truncated": truncated,
        "text": text,
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
