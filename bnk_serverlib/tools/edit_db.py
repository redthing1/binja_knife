from __future__ import annotations

from typing import Any, Dict

_MISSING = object()


def _make_compact_save_settings():
    try:
        from binaryninja import SaveOption, SaveSettings
    except Exception:
        return None

    settings = SaveSettings()
    settings.set_option(SaveOption.TrimSnapshots)
    settings.set_option(SaveOption.RemoveUndoData)
    return settings


def _run_on_main_thread(fn):
    try:
        from binaryninja import mainthread
    except Exception:
        return fn()

    box: Dict[str, Any] = {}

    def wrapper() -> None:
        box["value"] = fn()

    try:
        mainthread.execute_on_main_thread_and_wait(wrapper)
    except Exception:
        return fn()
    return box.get("value")


def _require_bv_file(bv: Any) -> Any:
    if bv is None:
        raise ValueError("bv is required")

    f = getattr(bv, "file", None)
    if f is None:
        raise ValueError("bv.file is required")
    return f


def _bool_attr(obj: Any, name: str) -> bool | None:
    if obj is None:
        return None
    try:
        value = getattr(obj, name, _MISSING)
    except Exception:
        return None
    if value is _MISSING:
        return None
    return bool(value)


def _db_modified(bv: Any, f: Any) -> bool:
    for obj, name in (
        (bv, "analysis_changed"),
        (f, "analysis_changed"),
        (bv, "modified"),
        (f, "modified"),
    ):
        value = _bool_attr(obj, name)
        if value is not None:
            return value
    return False


def _db_state(bv: Any) -> Dict[str, Any]:
    f = _require_bv_file(bv)
    path = getattr(f, "filename", "") or ""
    source = getattr(f, "original_filename", "") or ""
    out = {
        "path": path,
        "has_database": bool(getattr(f, "has_database", False)),
        "modified": _db_modified(bv, f),
    }
    if source and source != path:
        out["source"] = source
    return out


def db_status(*, bv: Any) -> Dict[str, Any]:
    return _db_state(bv)


def db_save(*, bv: Any) -> Dict[str, Any]:
    state_before = _db_state(bv)
    modified_before = bool(state_before["modified"])

    if not bool(state_before["has_database"]):
        return {
            "saved": False,
            "error": "view is not backed by a database; use 'bnk edit db save-as' first",
            "modified": modified_before,
        }

    settings = _make_compact_save_settings()
    ok = bool(_run_on_main_thread(lambda: bv.save_auto_snapshot(settings=settings)))

    state_after = _db_state(bv)

    out = {
        "saved": ok,
        "modified": bool(state_after["modified"]),
    }
    if not ok:
        out["error"] = (
            "save_auto_snapshot returned false; database may be locked by another open view"
        )
    return out


def db_save_as(*, bv: Any, path: str) -> Dict[str, Any]:
    if path is None:
        raise ValueError("path is required")

    dest = str(path).strip()
    if not dest:
        raise ValueError("path is required")
    if not dest.lower().endswith(".bndb"):
        dest = f"{dest}.bndb"

    settings = _make_compact_save_settings()
    ok = bool(_run_on_main_thread(lambda: bv.create_database(dest, settings=settings)))

    state = _db_state(bv)

    out = {
        "saved": ok,
        "path": str(state.get("path", "") or dest),
        "modified": state["modified"],
    }
    if not ok:
        out["error"] = "create_database returned false"
    return out
