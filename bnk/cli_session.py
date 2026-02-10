from __future__ import annotations

from typing import Optional

import typer

from .cli_app import make_app
from .cli_ctx import cfg_from_ctx, print_value, with_client, with_session


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
    sess = name or cfg.session
    out = with_client(cfg, lambda c: c.session_open(sess))
    print_value(cfg, out)


@app.command("reset")
def session_reset(
    ctx: typer.Context,
    keep_bv: bool = typer.Option(True, "--keep-bv/--drop-bv", help="keep attached bv"),
) -> None:
    cfg = cfg_from_ctx(ctx)
    out = with_session(cfg, lambda c: c.session_reset(cfg.session, keep_bv=keep_bv))
    print_value(cfg, out)


@app.command("close")
def session_close(
    ctx: typer.Context, name: Optional[str] = typer.Argument(None)
) -> None:
    cfg = cfg_from_ctx(ctx)
    sess = name or cfg.session
    out = with_client(cfg, lambda c: c.session_close(sess))
    print_value(cfg, out)
