from __future__ import annotations

from typing import Any, Tuple


def analysis_update(bv: Any, mode: str) -> None:
    if bv is None:
        raise ValueError("bv is required")

    text = (mode or "none").strip().lower()
    if text in {"none", "no", "false", "0", ""}:
        return
    if text == "update":
        bv.update_analysis()
        return
    if text == "wait":
        bv.update_analysis_and_wait()
        return
    raise ValueError("analysis must be one of: none, update, wait")


def parse_type_string(bv: Any, text: str) -> Tuple[Any, Any]:
    if bv is None:
        raise ValueError("bv is required")
    if text is None:
        raise ValueError("type string is required")

    raw = str(text).strip()
    if not raw:
        raise ValueError("type string is required")

    # parse_type_string expects a declaration with a name, so we append a dummy
    return bv.parse_type_string(f"{raw} __bnk_tmp")
