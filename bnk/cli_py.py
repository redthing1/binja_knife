from __future__ import annotations

import sys
from pathlib import Path

import typer

from .cli_app import CONTEXT_SETTINGS, make_app
from .cli_ctx import cfg_from_ctx, print_value, require_session, with_session


app = make_app()
RUN_CONTEXT_SETTINGS = dict(
    CONTEXT_SETTINGS,
    allow_extra_args=True,
    ignore_unknown_options=True,
)


def _run_session_code(
    ctx: typer.Context,
    code: str,
    *,
    argv: list[str],
) -> None:
    cfg = cfg_from_ctx(ctx)
    session = require_session(cfg)
    out = with_session(
        cfg,
        lambda c: c.run_code(session, code, argv=argv, capture_output=True),
    )
    print_value(cfg, out)


def _script_argv(ctx: typer.Context, argv: list[str]) -> list[str]:
    # Support both repeated --argv and trailing pass-through args after PATH.
    return [*argv, *ctx.args]


@app.command("exec")
def py_exec(
    ctx: typer.Context,
    code: str = typer.Argument(..., help="python code, or '-' to read from stdin"),
    argv: list[str] = typer.Option([], "--argv", help="arguments for sys.argv[1:]"),
) -> None:
    if code == "-":
        code = sys.stdin.read()
    _run_session_code(ctx, code, argv=list(argv))


@app.command("eval")
def py_eval(
    ctx: typer.Context,
    expr: str = typer.Argument(...),
    argv: list[str] = typer.Option([], "--argv", help="arguments for sys.argv[1:]"),
) -> None:
    code = f"__result__ = ({expr})"
    _run_session_code(ctx, code, argv=list(argv))


@app.command("run", context_settings=RUN_CONTEXT_SETTINGS)
def py_run(
    ctx: typer.Context,
    path: Path = typer.Argument(..., exists=True),
    argv: list[str] = typer.Option(
        [],
        "--argv",
        help="arguments for sys.argv[1:] (repeat --argv or pass trailing args after PATH)",
    ),
) -> None:
    cfg = cfg_from_ctx(ctx)
    session = require_session(cfg)
    path = path.expanduser().resolve()
    script_argv = _script_argv(ctx, list(argv))

    out = with_session(
        cfg,
        lambda c: c.run_file(
            session,
            str(path),
            argv=script_argv,
            capture_output=True,
        ),
    )
    print_value(cfg, out)
