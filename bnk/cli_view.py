from __future__ import annotations

import typer

from .cli_app import make_app
from .cli_ctx import cfg_from_ctx, print_value, with_client


app = make_app()


@app.command("list")
def view_list(
    ctx: typer.Context,
    include_unnamed: bool = typer.Option(
        False, "--all", "-a", help="include unnamed views"
    ),
    full: bool = typer.Option(False, "--full", "-f", help="include full metadata"),
) -> None:
    cfg = cfg_from_ctx(ctx)
    out = with_client(
        cfg,
        lambda c: c.view_list(include_unnamed=include_unnamed, full=full),
    )
    print_value(cfg, out)
