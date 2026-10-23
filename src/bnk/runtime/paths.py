from __future__ import annotations

import os
from pathlib import Path


def _xdg(name: str, default: str) -> Path:
    value = os.environ.get(name, "")
    base = Path(value) if value and Path(value).is_absolute() else Path.home() / default
    return base / "bnk"


def data_dir() -> Path:
    return _xdg("XDG_DATA_HOME", ".local/share")


def runtime_dir() -> Path:
    return data_dir() / "runtime"


def state_dir() -> Path:
    return _xdg("XDG_STATE_HOME", ".local/state")


def cache_dir() -> Path:
    return _xdg("XDG_CACHE_HOME", ".cache")


def log_path() -> Path:
    return state_dir() / "runtime.log"
