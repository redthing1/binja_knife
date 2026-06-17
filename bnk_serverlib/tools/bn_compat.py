from __future__ import annotations

from typing import Any, Callable, TypeVar


T = TypeVar("T")


def bool_attr(obj: Any, name: str) -> bool | None:
    if obj is None:
        return None
    try:
        value = getattr(obj, name)
    except Exception:
        return None
    return bool(value)


def compact_save_settings() -> Any:
    try:
        from binaryninja import SaveOption, SaveSettings
    except Exception:
        return None

    settings = SaveSettings()
    settings.set_option(SaveOption.TrimSnapshots)
    settings.set_option(SaveOption.RemoveUndoData)
    return settings


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
