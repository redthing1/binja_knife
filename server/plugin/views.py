from __future__ import annotations

import weakref
from typing import Any, Dict, List, Optional, Tuple

from .log import dbg


_SHARED_VIEW_IDS: Dict[int, str] = {}
_SHARED_VIEW_NEXT_ID = 0


def _safe_str(value: Any) -> str:
    try:
        return str(value)
    except Exception:
        return repr(value)


def _safe_getattr(obj: Any, name: str, default: Any = None) -> Any:
    try:
        return getattr(obj, name)
    except Exception:
        return default


def _iter_frame_views(frame: Any):
    for attr in ("getCurrentView", "getView"):
        getter = _safe_getattr(frame, attr)
        if callable(getter):
            try:
                view = getter()
            except Exception:
                continue
            if view is not None:
                yield view

    for attr in ("getViews", "getAllViews"):
        getter = _safe_getattr(frame, attr)
        if callable(getter):
            try:
                views = getter() or []
            except Exception:
                continue
            for view in views:
                if view is not None:
                    yield view


def _view_to_bv(view: Any) -> Optional[Any]:
    for attr in ("getData", "getBinaryView", "getCurrentBinaryView"):
        getter = _safe_getattr(view, attr)
        if callable(getter):
            try:
                bv = getter()
            except Exception:
                continue
            if bv is not None:
                return bv
    return None


def view_info_full(bv: Any) -> Dict[str, Any]:
    file_obj = _safe_getattr(bv, "file")
    filename = None
    if file_obj is not None:
        filename = _safe_getattr(file_obj, "filename") or _safe_getattr(
            file_obj, "original_filename"
        )
    arch = _safe_getattr(bv, "arch")
    analysis_state = _safe_getattr(bv, "analysis_state")
    start = _safe_getattr(bv, "start") or 0
    length = _safe_getattr(bv, "length") or 0
    info = {
        "filename": filename or "",
        "view_type": _safe_getattr(bv, "view_type") or "",
        "arch": _safe_getattr(arch, "name") or _safe_str(arch) if arch else "",
        "analysis_state": (
            _safe_getattr(analysis_state, "name") or _safe_str(analysis_state)
            if analysis_state
            else ""
        ),
        "start": start,
        "length": length,
        "repr": _safe_str(bv),
    }
    info["start_hex"] = f"0x{start:x}"
    info["length_hex"] = f"0x{length:x}"
    if not info["filename"]:
        info["filename"] = info["repr"]
    return info


def safe_view_filename(bv: Any) -> str:
    file_obj = _safe_getattr(bv, "file")
    if file_obj is None:
        return ""
    return str(
        _safe_getattr(file_obj, "filename")
        or _safe_getattr(file_obj, "original_filename")
        or ""
    )


def _shared_view_id(bv: Any) -> str:
    global _SHARED_VIEW_NEXT_ID
    key = id(bv)
    existing = _SHARED_VIEW_IDS.get(key)
    if existing is not None:
        return existing
    _SHARED_VIEW_NEXT_ID += 1
    view_id = f"v{_SHARED_VIEW_NEXT_ID}"
    _SHARED_VIEW_IDS[key] = view_id
    return view_id


def merge_csv_field(current: str, new_value: str) -> str:
    parts: List[str] = []
    for value in (current, new_value):
        for item in str(value or "").split(","):
            item = item.strip()
            if item and item not in parts:
                parts.append(item)
    return ",".join(parts)


def is_shared_view_source(source: str) -> bool:
    parts = {item.strip() for item in str(source or "").split(",") if item.strip()}
    return bool(parts & {"ui", "viewframe", "scripting"})


def build_shared_view_inventory(
    gui_entries: List[Tuple[Any, Dict[str, Any]]],
    *,
    include_unnamed: bool = False,
    full: bool = False,
) -> List[Tuple[weakref.ReferenceType[Any], Dict[str, Any]]]:
    by_id: Dict[int, Tuple[weakref.ReferenceType[Any], Dict[str, Any]]] = {}

    def add_entry(bv: Any, info: Dict[str, Any]) -> None:
        filename = str(info.get("filename", "") or "")
        if not include_unnamed and not filename.strip():
            return

        key = id(bv)
        existing = by_id.get(key)
        if existing is None:
            entry = {
                "id": _shared_view_id(bv),
                "target": filename,
            }
            if full:
                entry.update(
                    {
                        "source": str(info.get("source", "") or ""),
                        "repr": str(info.get("repr", "") or ""),
                    }
                )
                try:
                    full_info = view_info_full(bv)
                    entry.update(
                        {
                            "view_type": full_info.get("view_type", ""),
                            "arch": full_info.get("arch", ""),
                            "analysis_state": full_info.get("analysis_state", ""),
                            "start_hex": full_info.get("start_hex", ""),
                            "length_hex": full_info.get("length_hex", ""),
                            "repr": full_info.get("repr", entry.get("repr", "")),
                        }
                    )
                except Exception:
                    pass
            else:
                try:
                    full_info = view_info_full(bv)
                    entry["view_type"] = full_info.get("view_type", "")
                    entry["arch"] = full_info.get("arch", "")
                except Exception:
                    entry["view_type"] = ""
                    entry["arch"] = ""
            by_id[key] = (weakref.ref(bv), entry)
            return

        _bv_ref, entry = existing
        if full:
            entry["source"] = merge_csv_field(
                str(entry.get("source", "")), str(info.get("source", ""))
            )
        if not str(entry.get("target", "") or "").strip() and filename.strip():
            entry["target"] = filename

    for bv, info in gui_entries:
        gui_source = str(info.get("source", "") or "ui")
        if not is_shared_view_source(gui_source):
            continue
        add_entry(
            bv,
            {
                "filename": str(info.get("filename", "") or safe_view_filename(bv)),
                "repr": str(info.get("repr", "") or ""),
                "source": gui_source,
            },
        )

    rows = list(by_id.values())
    rows.sort(
        key=lambda item: (
            str(item[1].get("target", "") or ""),
            str(item[1].get("id", "") or ""),
        )
    )
    return rows


def shared_view_inventory(
    *,
    include_unnamed: bool = False,
    full: bool = False,
) -> List[Tuple[weakref.ReferenceType[Any], Dict[str, Any]]]:
    return build_shared_view_inventory(
        collect_gui_bvs(),
        include_unnamed=include_unnamed,
        full=full,
    )


def find_shared_view(
    view_id: str,
    *,
    include_unnamed: bool = False,
) -> Tuple[Any, Dict[str, Any]]:
    wanted = str(view_id or "").strip()
    if not wanted:
        raise ValueError("view id is required")

    for bv_ref, info in shared_view_inventory(include_unnamed=include_unnamed):
        if str(info.get("id", "")) != wanted:
            continue
        bv = bv_ref()
        if bv is None:
            raise RuntimeError("selected shared view is no longer available")
        return bv, dict(info)

    raise ValueError(f"unknown shared view id: {wanted}")


def _run_on_main_thread(fn):
    try:
        from binaryninja import mainthread
    except Exception:
        return fn()
    box: Dict[str, Any] = {}

    def wrapper():
        box["value"] = fn()

    try:
        mainthread.execute_on_main_thread_and_wait(wrapper)
    except Exception:
        return fn()
    return box.get("value")


def collect_gui_bvs() -> List[Tuple[Any, Dict[str, Any]]]:
    try:
        import binaryninjaui as ui  # type: ignore
    except Exception:
        return []

    def _collect() -> List[Tuple[Any, Dict[str, Any]]]:
        out: List[Tuple[Any, Dict[str, Any]]] = []
        try:
            contexts = list(ui.UIContext.allContexts())
        except Exception:
            contexts = []

        for ctx in contexts:
            try:
                available = ctx.getAvailableBinaryViews() or []
            except Exception:
                available = []

            for item in available:
                filename = ""
                bv = None
                if isinstance(item, tuple) and item:
                    bv = item[0]
                    if len(item) > 1 and isinstance(item[1], str):
                        filename = item[1]
                else:
                    bv = item
                if bv is None:
                    continue
                if not filename:
                    file_obj = _safe_getattr(bv, "file")
                    filename = (
                        _safe_getattr(file_obj, "filename")
                        or _safe_getattr(file_obj, "original_filename")
                        or ""
                    )
                info: Dict[str, Any] = {
                    "filename": filename or "",
                    "repr": filename or _safe_str(bv),
                    "source": "ui",
                }
                out.append((bv, info))

        try:
            frames = list(ui.ViewFrame.viewFrames())
        except Exception:
            frames = []

        for frame in frames:
            for view in _iter_frame_views(frame):
                bv = _view_to_bv(view)
                if bv is None:
                    continue
                file_obj = _safe_getattr(bv, "file")
                filename = (
                    _safe_getattr(file_obj, "filename")
                    or _safe_getattr(file_obj, "original_filename")
                    or ""
                )
                info: Dict[str, Any] = {
                    "filename": filename or "",
                    "repr": filename or _safe_str(bv),
                    "source": "viewframe",
                }
                out.append((bv, info))
        return out

    entries = _run_on_main_thread(_collect) or []

    # optional: also attempt to discover bvs from scripting provider instances
    try:
        import binaryninja.scriptingprovider as sp  # type: ignore
    except Exception:
        sp = None
    if sp is not None:
        instances = list(
            getattr(sp.PythonScriptingInstance, "_registered_instances", [])
        )
        for inst in instances:
            try:
                bv = sp.PythonScriptingProvider.magic_variables["bv"].get_value(inst)
            except Exception:
                bv = None
            if bv is None:
                continue
            file_obj = _safe_getattr(bv, "file")
            filename = (
                _safe_getattr(file_obj, "filename")
                or _safe_getattr(file_obj, "original_filename")
                or ""
            )
            info = {
                "filename": filename or "",
                "repr": filename or _safe_str(bv),
                "source": "scripting",
            }
            entries.append((bv, info))

    # dedupe by object identity, but merge metadata from multiple sources
    by_id: Dict[int, Tuple[Any, Dict[str, Any]]] = {}
    for bv, info in entries:
        key = id(bv)
        cur = by_id.get(key)
        if cur is None:
            by_id[key] = (bv, dict(info))
            continue

        _cur_bv, cur_info = cur
        cur_filename = (cur_info.get("filename") or "").strip()
        new_filename = (info.get("filename") or "").strip()
        if not cur_filename and new_filename:
            cur_info["filename"] = new_filename
            cur_info["repr"] = new_filename or cur_info.get("repr", "")

        cur_source = (cur_info.get("source") or "").strip()
        new_source = (info.get("source") or "").strip()
        if new_source:
            parts = [p for p in cur_source.split(",") if p]
            if new_source not in parts:
                parts.append(new_source)
                cur_info["source"] = ",".join(parts)

    unique = list(by_id.values())
    dbg(f"collect_gui_bvs: {len(unique)} unique views")
    return unique
