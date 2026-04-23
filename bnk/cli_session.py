from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

import typer

from .cli_app import make_app
from .cli_ctx import (
    cfg_from_ctx,
    print_value,
    require_session,
    with_client,
    with_session,
)


app = make_app()


@app.command("list")
def session_list(ctx: typer.Context) -> None:
    cfg = cfg_from_ctx(ctx)
    out = with_client(cfg, lambda c: c.session_list())
    print_value(cfg, out)


@app.command("open")
def session_open(
    ctx: typer.Context, name: Optional[str] = typer.Argument(None)
) -> None:
    cfg = cfg_from_ctx(ctx)
    sess = name or require_session(cfg)
    out = with_client(cfg, lambda c: c.session_open(sess))
    print_value(cfg, out)


@app.command("show")
def session_show(ctx: typer.Context) -> None:
    cfg = cfg_from_ctx(ctx)
    session = require_session(cfg)
    out = with_client(cfg, lambda c: c.session_show(session))
    print_value(cfg, out)


@app.command("load")
def session_load(
    ctx: typer.Context,
    path: str = typer.Argument(..., help="path to binary or .bndb"),
    local_path: bool = typer.Option(
        True,
        "--local/--remote",
        help="Interpret PATH on the client filesystem (--local) vs on the server filesystem (--remote).",
    ),
    update_analysis: bool = typer.Option(
        True, "--update-analysis/--no-update-analysis", help="run analysis"
    ),
    options_json: Optional[str] = typer.Option(
        None, "--options-json", help="json dict"
    ),
) -> None:
    cfg = cfg_from_ctx(ctx)
    session = require_session(cfg)
    if local_path:
        p = Path(path).expanduser().resolve()
        if not p.exists():
            raise typer.BadParameter(f"path does not exist: {p}")
        path_str = str(p)
    else:
        path_str = path

    options: Optional[Dict[str, Any]] = None
    if options_json:
        try:
            options = json.loads(options_json)
        except Exception as exc:
            raise typer.BadParameter(f"invalid --options-json: {exc}") from exc
        if not isinstance(options, dict):
            raise typer.BadParameter("--options-json must be a json object")

    out = with_client(
        cfg,
        lambda c: c.session_load(
            session,
            path_str,
            update_analysis=update_analysis,
            options=options,
        ),
    )
    print_value(cfg, out)


@app.command("attach")
def session_attach(
    ctx: typer.Context,
    view_id: str = typer.Argument(..., help="id from 'bnk view list'"),
    include_unnamed: bool = typer.Option(False, "--all", help="include unnamed views"),
) -> None:
    cfg = cfg_from_ctx(ctx)
    session = require_session(cfg)
    out = with_client(
        cfg,
        lambda c: c.session_attach(
            session,
            view_id=view_id,
            include_unnamed=include_unnamed,
        ),
    )
    print_value(cfg, out)


@app.command("detach")
def session_detach(ctx: typer.Context) -> None:
    cfg = cfg_from_ctx(ctx)
    session = require_session(cfg)
    out = with_client(cfg, lambda c: c.session_detach(session))
    print_value(cfg, out)


@app.command("reset")
def session_reset(
    ctx: typer.Context,
    keep_target: bool = typer.Option(
        True, "--keep-target/--drop-target", help="keep current target"
    ),
) -> None:
    cfg = cfg_from_ctx(ctx)
    session = require_session(cfg)
    out = with_session(cfg, lambda c: c.session_reset(session, keep_bv=keep_target))
    print_value(cfg, out)


@app.command("close")
def session_close(
    ctx: typer.Context, name: Optional[str] = typer.Argument(None)
) -> None:
    cfg = cfg_from_ctx(ctx)
    sess = name or require_session(cfg)
    out = with_client(cfg, lambda c: c.session_close(sess))
    print_value(cfg, out)
