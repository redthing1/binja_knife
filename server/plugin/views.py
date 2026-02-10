from __future__ import annotations

from typing import Any, Dict, List, Optional, Tuple

from .log import dbg


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


def match_views(views: List[Dict[str, Any]], match: str) -> List[int]:
    needle = (match or "").lower()
    matches: List[int] = []
    for idx, info in enumerate(views):
        haystacks = [info.get("filename", ""), info.get("repr", "")]
        if any(needle in (h or "").lower() for h in haystacks):
            matches.append(idx)
    return matches
