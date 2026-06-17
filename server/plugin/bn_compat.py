from __future__ import annotations

from typing import Any, Callable, TypeVar


T = TypeVar("T")


def safe_str(value: Any) -> str:
    try:
        return str(value)
    except Exception:
        return repr(value)


def safe_getattr(obj: Any, name: str, default: Any = None) -> Any:
    try:
        return getattr(obj, name)
    except Exception:
        return default


def run_on_main_thread(fn: Callable[[], T]) -> T:
    try:
        from binaryninja import mainthread
    except Exception:
        return fn()

    box: dict[str, T] = {}

    def wrapper() -> None:
        box["value"] = fn()

    try:
        mainthread.execute_on_main_thread_and_wait(wrapper)
    except Exception:
        return fn()
    return box.get("value")  # type: ignore[return-value]


def view_filename(bv: Any) -> str:
    file_obj = safe_getattr(bv, "file")
    if file_obj is None:
        return ""
    return str(
        safe_getattr(file_obj, "filename")
        or safe_getattr(file_obj, "original_filename")
        or ""
    )
