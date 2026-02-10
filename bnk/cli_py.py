from __future__ import annotations

import sys
from pathlib import Path

import typer

from .cli_app import make_app
from .cli_ctx import cfg_from_ctx, print_value, with_session


app = make_app()


@app.command("exec")
def py_exec(
    ctx: typer.Context,
    code: str = typer.Argument(..., help="python code, or '-' to read from stdin"),
    argv: list[str] = typer.Option([], "--argv", help="arguments for sys.argv[1:]"),
) -> None:
    cfg = cfg_from_ctx(ctx)
    if code == "-":
        code = sys.stdin.read()
    out = with_session(
        cfg,
        lambda c: c.run_code(cfg.session, code, argv=list(argv), capture_output=True),
    )
    print_value(cfg, out)


@app.command("eval")
def py_eval(
    ctx: typer.Context,
    expr: str = typer.Argument(...),
    argv: list[str] = typer.Option([], "--argv", help="arguments for sys.argv[1:]"),
) -> None:
    cfg = cfg_from_ctx(ctx)
    code = f"__result__ = ({expr})"
    out = with_session(
        cfg,
        lambda c: c.run_code(cfg.session, code, argv=list(argv), capture_output=True),
    )
    print_value(cfg, out)


@app.command("run")
def py_run(
    ctx: typer.Context,
    path: Path = typer.Argument(..., exists=True),
    argv: list[str] = typer.Option([], "--argv", help="arguments for sys.argv[1:]"),
) -> None:
    cfg = cfg_from_ctx(ctx)
    path = path.expanduser().resolve()

    code = "\n".join(
        [
            "import sys",
            f"_path = {str(path)!r}",
            "_old_argv = sys.argv",
            "sys.argv = [_path] + sys.argv[1:]",
            "globals()['__file__'] = _path",
            "globals()['__name__'] = '__main__'",
            "globals()['__package__'] = None",
            "try:",
            "    with open(_path, 'r', encoding='utf-8') as _fh:",
            "        _source = _fh.read()",
            "    _compiled = compile(_source, _path, 'exec')",
            "    exec(_compiled, globals(), globals())",
            "finally:",
            "    sys.argv = _old_argv",
        ]
    )

    out = with_session(
        cfg,
        lambda c: c.run_code(cfg.session, code, argv=list(argv), capture_output=True),
    )
    print_value(cfg, out)
