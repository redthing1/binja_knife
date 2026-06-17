from __future__ import annotations

from typing import Any, Dict

from .bn_compat import bool_attr, compact_save_settings, run_on_main_thread


def _require_bv_file(bv: Any) -> Any:
    if bv is None:
        raise ValueError("bv is required")

    f = getattr(bv, "file", None)
    if f is None:
        raise ValueError("bv.file is required")
    return f


def _db_modified(bv: Any, f: Any) -> bool:
    for obj, name in (
        (bv, "analysis_changed"),
        (f, "analysis_changed"),
        (bv, "modified"),
        (f, "modified"),
    ):
        value = bool_attr(obj, name)
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

    settings = compact_save_settings()
    ok = bool(run_on_main_thread(lambda: bv.save_auto_snapshot(settings=settings)))

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

    settings = compact_save_settings()
    ok = bool(run_on_main_thread(lambda: bv.create_database(dest, settings=settings)))

    state = _db_state(bv)

    out = {
        "saved": ok,
        "path": str(state.get("path", "") or dest),
        "modified": state["modified"],
    }
    if not ok:
        out["error"] = "create_database returned false"
    return out
