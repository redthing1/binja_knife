from __future__ import annotations

import os
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True)
class Config:
    host: str = "127.0.0.1"
    port: int = 18812
    timeout: float = 3600.0
    session: str = "default"
    json_output: bool = False
    pretty: bool = False
    tool_root: Optional[str] = None


def env_default_host() -> str:
    return os.environ.get("BNK_HOST", "127.0.0.1")


def env_default_port() -> int:
    raw = os.environ.get("BNK_PORT")
    if not raw:
        return 18812
    try:
        return int(raw)
    except Exception as exc:
        raise ValueError(f"invalid BNK_PORT={raw!r}") from exc


def env_default_timeout() -> float:
    raw = os.environ.get("BNK_TIMEOUT")
    if not raw:
        return 3600.0
    try:
        return float(raw)
    except Exception as exc:
        raise ValueError(f"invalid BNK_TIMEOUT={raw!r}") from exc


def env_default_session() -> str:
    return os.environ.get("BNK_SESSION", "default")
