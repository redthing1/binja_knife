from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Callable, Dict, TypeVar

import click
import typer

from .client import ConnectConfig, KnifeClient
from .config import Config
from .output import dump_json, format_text
from .serverlib import ServerlibCall, make_tool_call_code, make_tool_list_code
from .tool_root import find_tool_root


def cfg_from_ctx(ctx: typer.Context) -> Config:
    cfg = getattr(ctx, "obj", None)
    if not isinstance(cfg, Config):
        raise typer.Exit(2)
    return cfg


def connect(cfg: Config) -> KnifeClient:
    try:
        return KnifeClient(
            ConnectConfig(host=cfg.host, port=cfg.port, timeout=cfg.timeout)
        )
    except (EOFError, OSError) as exc:
        raise click.ClickException(
            f"could not connect to {cfg.host}:{cfg.port}: {exc}"
        ) from exc


T = TypeVar("T")


def _attempt_server_interrupt(cfg: Config) -> Dict[str, Any]:
    short_timeout = 2.0
    try:
        with KnifeClient(
            ConnectConfig(host=cfg.host, port=cfg.port, timeout=short_timeout)
        ) as c:
            out = c.request_interrupt()
    except Exception as exc:
        return {"ok": False, "interrupted": False, "error": str(exc)}
    return out


def with_client(cfg: Config, fn: Callable[[KnifeClient], T]) -> T:
    with connect(cfg) as c:
        try:
            return fn(c)
        except TimeoutError as exc:
            msg = f"request timed out after {cfg.timeout:g}s"
            interrupt = _attempt_server_interrupt(cfg)
            if interrupt.get("interrupted"):
                name = interrupt.get("name")
                elapsed = interrupt.get("elapsed_s")
                details = f"interrupt sent to active request"
                if name:
                    details += f" ({name})"
                if isinstance(elapsed, (int, float)):
                    details += f" at {elapsed:.2f}s"
                msg = f"{msg}; {details}"
            else:
                err = interrupt.get("error")
                if err:
                    msg = f"{msg}; interrupt attempt failed: {err}"
                else:
                    msg = f"{msg}; no active request to interrupt"
            raise click.ClickException(msg) from exc


def with_session(cfg: Config, fn: Callable[[KnifeClient], T]) -> T:
    def wrapped(c: KnifeClient) -> T:
        c.session_open(cfg.session)
        return fn(c)

    return with_client(cfg, wrapped)


def print_value(cfg: Config, value: Any) -> None:
    if cfg.json_output:
        typer.echo(dump_json(value, pretty=cfg.pretty))
        return
    typer.echo(format_text(value))


def tool_root(cfg: Config) -> Path:
    if cfg.tool_root:
        return Path(cfg.tool_root).expanduser()
    auto = find_tool_root(Path.cwd())
    if auto is not None:
        return auto

    try:
        import bnk_serverlib  # type: ignore
    except Exception:
        bnk_serverlib = None

    if bnk_serverlib is not None:
        mod_path = getattr(bnk_serverlib, "__file__", None)
        if isinstance(mod_path, str) and mod_path:
            return Path(mod_path).resolve().parent.parent

    raise typer.BadParameter(
        "tool features require --tool-root (binja_knife repo path) or BNK_TOOL_ROOT"
    )


def _run_in_session(cfg: Config, code: str) -> Any:
    return with_session(
        cfg, lambda c: c.run_code(cfg.session, code, capture_output=True)
    )


def serverlib_list(cfg: Config) -> Any:
    root = tool_root(cfg)
    code = make_tool_list_code(root)
    return _run_in_session(cfg, code)


def serverlib_call(cfg: Config, tool: str, params: Dict[str, Any]) -> Any:
    root = tool_root(cfg)
    call = ServerlibCall(tool=tool, params=params)
    code = make_tool_call_code(root, call)
    return _run_in_session(cfg, code)


def parse_kv_args(items: list[str]) -> Dict[str, Any]:
    out: Dict[str, Any] = {}
    for item in items:
        if "=" not in item:
            raise typer.BadParameter(f"expected KEY=VALUE, got {item!r}")
        key, raw = item.split("=", 1)
        key = key.strip()
        if not key:
            raise typer.BadParameter(f"expected KEY=VALUE, got {item!r}")
        raw = raw.strip()
        if raw == "":
            out[key] = ""
            continue
        try:
            out[key] = json.loads(raw)
        except Exception:
            out[key] = raw
    return out
