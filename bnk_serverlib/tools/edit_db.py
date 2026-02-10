from __future__ import annotations

from typing import Any, Dict


def db_status(*, bv: Any) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    f = getattr(bv, "file", None)
    if f is None:
        raise ValueError("bv.file is required")

    filename = getattr(f, "filename", "") or ""
    original_filename = getattr(f, "original_filename", "") or ""
    has_database = bool(getattr(f, "has_database", False))
    modified = bool(getattr(f, "modified", False))
    saved = bool(getattr(f, "saved", False))

    return {
        "filename": filename,
        "original_filename": original_filename,
        "has_database": has_database,
        "modified": modified,
        "saved": saved,
    }


def db_save(*, bv: Any) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")

    f = getattr(bv, "file", None)
    if f is None:
        raise ValueError("bv.file is required")

    filename = getattr(f, "filename", "") or ""
    has_database = bool(getattr(f, "has_database", False))
    modified_before = bool(getattr(f, "modified", False))
    saved_before = bool(getattr(f, "saved", False))

    if not has_database:
        return {
            "saved": False,
            "error": "view is not backed by a database; use 'bnk edit db save-as' first",
            "filename": filename,
            "has_database": has_database,
            "modified": modified_before,
            "saved_flag": saved_before,
        }

    ok = bool(bv.save_auto_snapshot())

    modified_after = bool(getattr(f, "modified", False))
    saved_after = bool(getattr(f, "saved", False))

    return {
        "saved": ok,
        "filename": filename,
        "has_database": has_database,
        "modified_before": modified_before,
        "modified_after": modified_after,
        "saved_before": saved_before,
        "saved_after": saved_after,
    }


def db_save_as(*, bv: Any, path: str) -> Dict[str, Any]:
    if bv is None:
        raise ValueError("bv is required")
    if path is None:
        raise ValueError("path is required")

    dest = str(path).strip()
    if not dest:
        raise ValueError("path is required")
    if not dest.lower().endswith(".bndb"):
        dest = f"{dest}.bndb"

    ok = bool(bv.create_database(dest))

    f = getattr(bv, "file", None)
    filename = getattr(f, "filename", "") or ""
    has_database = bool(getattr(f, "has_database", False))
    modified = bool(getattr(f, "modified", False)) if f is not None else False
    saved = bool(getattr(f, "saved", False)) if f is not None else False

    return {
        "saved": ok,
        "path": dest,
        "filename": filename,
        "has_database": has_database,
        "modified": modified,
        "saved_flag": saved,
    }
