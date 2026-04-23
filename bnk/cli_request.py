from __future__ import annotations

import typer

from .cli_app import make_app
from .cli_ctx import cfg_from_ctx, print_value, with_client


app = make_app()


@app.command("status")
def request_status(ctx: typer.Context) -> None:
    cfg = cfg_from_ctx(ctx)
    out = with_client(cfg, lambda c: c.request_status(cfg.session))
    print_value(cfg, out)


@app.command("interrupt")
def request_interrupt(ctx: typer.Context) -> None:
    cfg = cfg_from_ctx(ctx)
    out = with_client(cfg, lambda c: c.request_interrupt(cfg.session))
    print_value(cfg, out)
