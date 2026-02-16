from __future__ import annotations

import re
from typing import Any, Callable, Optional, Pattern


def hex_addr(value: Any) -> str:
    if not isinstance(value, int):
        return ""
    return hex(value)


def enum_name(value: Any) -> str:
    if value is None:
        return ""
    name = getattr(value, "name", None)
    if isinstance(name, str) and name:
        return name
    try:
        return str(value)
    except Exception:
        return repr(value)


def parse_int(value: Any) -> Optional[int]:
    if isinstance(value, int):
        return value
    if not isinstance(value, str):
        return None

    text = value.strip().lower()
    if not text:
        return None
    if text.startswith("0x"):
        try:
            return int(text, 16)
        except ValueError:
            return None
    try:
        return int(text, 10)
    except ValueError:
        return None


def section_range(bv: Any, name: str) -> Optional[tuple[int, int]]:
    if not name:
        return None
    sections = {s.name.lower(): s for s in bv.sections.values()}
    sec = sections.get(name.lower())
    if not sec:
        return None
    return sec.start, sec.end


def resolve_target_addrs(bv: Any, target: Any) -> list[int]:
    if isinstance(target, int):
        return [target]
    if isinstance(target, str):
        text = target.strip()
        addr = parse_int(text)
        if addr is not None:
            return [addr]

        try:
            syms = bv.get_symbols_by_name(text) or []
        except Exception:
            syms = []

        addrs: list[int] = []
        for sym in syms:
            a = getattr(sym, "address", None)
            if isinstance(a, int):
                addrs.append(a)

        out: list[int] = []
        seen: set[int] = set()
        for a in addrs:
            if a in seen:
                continue
            seen.add(a)
            out.append(a)
        return out
    return []


def resolve_function(bv: Any, target: Any) -> Optional[Any]:
    if bv is None:
        return None
    if isinstance(target, int):
        try:
            return bv.get_function_at(target)
        except Exception:
            return None
    if isinstance(target, str):
        text = target.strip()
        addr = parse_int(text)
        if addr is not None:
            try:
                return bv.get_function_at(addr)
            except Exception:
                return None
        try:
            funcs = bv.get_functions_by_name(text) or []
        except Exception:
            funcs = []
        return funcs[0] if funcs else None
    return None


def ref_address(ref: Any) -> Optional[int]:
    if isinstance(ref, int):
        return ref
    addr = getattr(ref, "address", None)
    return addr if isinstance(addr, int) else None


def ref_function_name(ref: Any) -> str:
    func = getattr(ref, "function", None)
    if func is None:
        return ""
    return getattr(func, "name", "") or ""


def make_text_matcher(
    pattern: str,
    *,
    case_insensitive: bool = True,
    regex: bool = False,
) -> Callable[[Any], bool]:
    if pattern is None:
        raise ValueError("pattern is required")

    if regex:
        flags = re.IGNORECASE if case_insensitive else 0
        try:
            compiled = re.compile(pattern, flags)
        except re.error as exc:
            raise ValueError(f"invalid regex pattern: {exc}") from exc

        def _matches(value: Any) -> bool:
            return bool(compiled.search(str(value)))

        return _matches

    needle = pattern.lower() if case_insensitive else pattern

    if case_insensitive:

        def _matches(value: Any) -> bool:
            return needle in str(value).lower()

        return _matches

    def _matches(value: Any) -> bool:
        return needle in str(value)

    return _matches


def compile_bytes_regex(
    pattern: str,
    *,
    case_insensitive: bool = True,
) -> Pattern[bytes]:
    flags = re.IGNORECASE if case_insensitive else 0
    try:
        return re.compile(pattern.encode("utf-8", errors="ignore"), flags)
    except re.error as exc:
        raise ValueError(f"invalid regex pattern: {exc}") from exc
