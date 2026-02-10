from __future__ import annotations

from pathlib import Path
from typing import Optional


def _looks_like_binja_knife_pyproject(path: Path) -> bool:
    try:
        text = path.read_text(encoding="utf-8")
    except Exception:
        return False
    return 'name = "binja-knife"' in text or 'name="binja-knife"' in text


def find_tool_root(start: Path) -> Optional[Path]:
    cur = start.resolve()
    for parent in [cur] + list(cur.parents):
        pp = parent / "pyproject.toml"
        if pp.exists() and _looks_like_binja_knife_pyproject(pp):
            return parent
    return None
