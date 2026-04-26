from __future__ import annotations

from pathlib import Path
from typing import Optional

import typer

from .cli_app import make_app
from .cli_ctx import cfg_from_ctx, print_value, with_client
from .cli_edit import app as edit_app
from .cli_py import app as py_app
from .cli_request import app as request_app
from .cli_session import app as session_app
from .cli_tool import app as tool_app
from .cli_view import app as view_app
from .config import (
    Config,
    env_default_host,
    env_default_port,
    env_default_session,
    env_default_timeout,
)
from .endpoint import parse_endpoint


app = make_app(name="bnk", help="bnk: binaryninja knife")
app.add_typer(session_app, name="session")
app.add_typer(view_app, name="view")
app.add_typer(request_app, name="request")
app.add_typer(py_app, name="py")
app.add_typer(tool_app, name="tool")
app.add_typer(edit_app, name="edit")


@app.callback()
def main_cb(
    ctx: typer.Context,
    connect: Optional[str] = typer.Option(
        None,
        "--connect",
        "-c",
        help="HOST:PORT",
    ),
    host: str = typer.Option(env_default_host(), "--host", "-H", help="host"),
    port: int = typer.Option(env_default_port(), "--port", "-p", help="port"),
    timeout: float = typer.Option(
        env_default_timeout(),
        "--timeout",
        "-t",
        help="timeout seconds (0 disables)",
    ),
    session: Optional[str] = typer.Option(
        env_default_session(),
        "-s",
        "--session",
        help="session name",
    ),
    json_output: bool = typer.Option(
        False, "-j", "--json", help="json"
    ),
    pretty: bool = typer.Option(False, "--pretty", "-P", help="pretty json"),
    tool_root: Optional[Path] = typer.Option(
        None,
        "--tool-root",
        "-T",
        envvar="BNK_TOOL_ROOT",
        help="serverlib root",
    ),
) -> None:
    if connect:
        try:
            host, port = parse_endpoint(connect)
        except ValueError as exc:
            raise typer.BadParameter(str(exc)) from exc
    ctx.obj = Config(
        host=host,
        port=port,
        timeout=timeout,
        session=session,
        json_output=json_output,
        pretty=pretty,
        tool_root=(
            str(tool_root.expanduser().resolve()) if tool_root is not None else None
        ),
    )


@app.command("ping")
def ping(ctx: typer.Context) -> None:
    cfg = cfg_from_ctx(ctx)
    out = with_client(cfg, lambda c: {"core_version": c.core_version()})
    print_value(cfg, out if cfg.json_output else out["core_version"])


def main() -> None:
    app()


if __name__ == "__main__":
    main()
