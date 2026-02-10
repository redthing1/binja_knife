from __future__ import annotations

import json
from pathlib import Path
from typing import Any, Dict, Optional

import typer

from .cli_app import make_app
from .cli_ctx import cfg_from_ctx, print_value, with_session


app = make_app()


@app.command("list")
def view_list(
    ctx: typer.Context,
    include_unnamed: bool = typer.Option(False, "--all", help="include unnamed views"),
    full: bool = typer.Option(False, "--full", help="include full metadata"),
) -> None:
    cfg = cfg_from_ctx(ctx)
    out = with_session(
        cfg,
        lambda c: c.view_list(cfg.session, include_unnamed=include_unnamed, full=full),
    )
    print_value(cfg, out)


@app.command("attach")
def view_attach(
    ctx: typer.Context,
    index: Optional[int] = typer.Option(None, "--index", help="index from view list"),
    match: Optional[str] = typer.Option(None, "--match", help="substring match"),
    include_unnamed: bool = typer.Option(False, "--all", help="include unnamed views"),
) -> None:
    cfg = cfg_from_ctx(ctx)
    if (index is None) == (match is None):
        raise typer.BadParameter("provide exactly one of --index or --match")
    out = with_session(
        cfg,
        lambda c: c.view_attach(
            cfg.session,
            index=index,
            match=match,
            include_unnamed=include_unnamed,
        ),
    )
    print_value(cfg, out)


@app.command("status")
def view_status(ctx: typer.Context) -> None:
    cfg = cfg_from_ctx(ctx)
    out = with_session(cfg, lambda c: c.view_status(cfg.session))
    print_value(cfg, out)


@app.command("load")
def view_load(
    ctx: typer.Context,
    path: str = typer.Argument(..., help="path to binary (default: validated/canonicalized locally)"),
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
    if local_path:
        p = Path(path).expanduser().resolve()
        if not p.exists():
            raise typer.BadParameter(f"path does not exist: {p}")
        path_str = str(p)
    else:
        # Do not rewrite remote paths (docker mounts, SSH FS, etc.). Pass through as-is.
        path_str = path

    options: Optional[Dict[str, Any]] = None
    if options_json:
        try:
            options = json.loads(options_json)
        except Exception as exc:
            raise typer.BadParameter(f"invalid --options-json: {exc}") from exc
        if not isinstance(options, dict):
            raise typer.BadParameter("--options-json must be a json object")

    out = with_session(
        cfg,
        lambda c: c.view_load(
            cfg.session,
            path_str,
            update_analysis=update_analysis,
            options=options,
        ),
    )
    print_value(cfg, out)
