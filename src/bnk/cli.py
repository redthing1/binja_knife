from __future__ import annotations

import sys
from collections.abc import Callable
from pathlib import Path
from typing import Annotated, Any, Never

import typer
from typer.core import TyperGroup

from bnk import __version__
from bnk.client import BnkError, request
from bnk.endpoint import DEFAULT_CONNECT, Endpoint, EndpointError
from bnk.protocol import API_VERSION
from bnk.render import (
    close_text,
    code_text,
    edit_text,
    error_text,
    find_text,
    history_text,
    inspect_text,
    open_text,
    patch_text,
    python_text,
    refs_text,
    save_text,
    sections_text,
    segments_text,
    sessions_text,
    status_text,
    summary_text,
)


class CompactGroup(TyperGroup):
    def format_commands(self, ctx: typer.Context, formatter: typer.HelpFormatter) -> None:
        groups: dict[str, list[tuple[str, str]]] = {}
        for name in self.list_commands(ctx):
            command = self.get_command(ctx, name)
            if command is None or command.hidden:
                continue
            panel = getattr(command, "rich_help_panel", None) or "Commands"
            groups.setdefault(panel, []).append(
                (name, command.get_short_help_str(limit=formatter.width - 6))
            )
        for panel, rows in groups.items():
            with formatter.section(panel):
                formatter.write_dl(rows)


app = typer.Typer(
    name="bnk",
    cls=CompactGroup,
    help="Persistent Binary Ninja analysis from the command line.",
    epilog="Start: bnk open ./program; then bnk summary or bnk sessions.",
    no_args_is_help=True,
    add_completion=False,
    context_settings={"help_option_names": ["-h", "--help"]},
    pretty_exceptions_enable=False,
    rich_markup_mode=None,
)


@app.callback()
def root(
    context: typer.Context,
    connect: Annotated[
        str,
        typer.Option(
            "--connect",
            "-c",
            envvar="BNK_CONNECT",
            help="Binary Ninja server endpoint as HOST:PORT.",
        ),
    ] = DEFAULT_CONNECT,
) -> None:
    try:
        endpoint = Endpoint.parse(connect)
    except EndpointError as error:
        raise typer.BadParameter(str(error), param_hint="--connect") from error
    context.obj = endpoint


@app.command(rich_help_panel="Connection")
def status(context: typer.Context) -> None:
    """Show the connection, versions, and server uptime."""
    endpoint = _endpoint(context)
    try:
        response = request(endpoint, "status")
        if not isinstance(response, dict):
            raise BnkError("status returned an invalid result", kind="protocol")
        value = {
            **response,
            "client_version": __version__,
            "connect": str(endpoint),
        }
        typer.echo(status_text(value))
    except BnkError as error:
        _fail(error)


@app.command(rich_help_panel="Connection")
def version() -> None:
    """Show the local bnk version and protocol API."""
    typer.echo(f"bnk {__version__} (api {API_VERSION})")


@app.command(rich_help_panel="Sessions")
def sessions(context: typer.Context) -> None:
    """List retained Binary Ninja sessions."""
    _remote(context, "sessions", text=sessions_text)


@app.command("open", rich_help_panel="Sessions")
def open_binary(
    context: typer.Context,
    path: Annotated[str, typer.Argument(help="Binary path to open and analyze.")],
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Name for the session."),
    ] = None,
    server_path: Annotated[
        bool,
        typer.Option(
            "--server-path",
            help="Use an absolute PATH visible only to Binary Ninja.",
        ),
    ] = False,
) -> None:
    """Open, analyze, and retain a BinaryView."""
    try:
        resolved = path if server_path else _client_path(path)
    except BnkError as error:
        _fail(error)
    _remote(
        context,
        "open",
        args={"path": resolved, "server_path": server_path},
        session=session,
        text=open_text,
    )


@app.command(rich_help_panel="Sessions")
def summary(
    context: typer.Context,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to summarize."),
    ] = None,
) -> None:
    """Summarize one retained BinaryView."""
    _remote(
        context,
        "summary",
        session=session,
        text=summary_text,
    )


@app.command(rich_help_panel="Sessions")
def close(
    context: typer.Context,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to close."),
    ] = None,
    discard: Annotated[
        bool,
        typer.Option("--discard", help="Close despite unsaved changes."),
    ] = False,
) -> None:
    """Close one retained BinaryView."""
    _remote(
        context,
        "close",
        args={"discard": discard},
        session=session,
        text=close_text,
    )


@app.command(rich_help_panel="Understand")
def find(
    context: typer.Context,
    kind: Annotated[str, typer.Argument(help="strings, functions, symbols, or bytes")],
    query: Annotated[
        str | None,
        typer.Argument(help="Optional substring, or a required exact hex pattern for bytes."),
    ] = None,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to search."),
    ] = None,
    limit: Annotated[int, typer.Option("--limit", "-n", min=1, help="Maximum results.")] = 50,
    case_sensitive: Annotated[
        bool, typer.Option("--case-sensitive", help="Match letter case.")
    ] = False,
    refs: Annotated[
        bool, typer.Option("--refs", help="Expand direct references for string matches.")
    ] = False,
    imports: Annotated[
        bool, typer.Option("--imports", help="Show imported symbols only.")
    ] = False,
    exports: Annotated[
        bool, typer.Option("--exports", help="Show exported symbols only.")
    ] = False,
) -> None:
    """List or search strings, functions, symbols, or exact bytes."""
    if imports and exports:
        raise typer.BadParameter("choose at most one of --imports and --exports")
    symbol_filter = "imports" if imports else "exports" if exports else "all"
    _remote(
        context,
        "find",
        args={
            "kind": kind,
            "query": query,
            "limit": limit,
            "case_sensitive": case_sensitive,
            "refs": refs,
            "symbol_filter": symbol_filter,
        },
        session=session,
        text=find_text,
    )


@app.command(rich_help_panel="Understand")
def inspect(
    context: typer.Context,
    target: Annotated[str, typer.Argument(help="Address, symbol, function, or variable target.")],
    show_vars: Annotated[
        bool, typer.Option("--vars", help="List the function's variables.")
    ] = False,
    limit: Annotated[int, typer.Option("--limit", "-n", min=1, help="Maximum variables with --vars.")] = 50,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to inspect."),
    ] = None,
) -> None:
    """Inspect one semantic target and its immediate context."""
    _remote(
        context,
        "inspect",
        args={"target": target, "vars": show_vars, "limit": limit},
        session=session,
        text=inspect_text,
    )


@app.command(rich_help_panel="Understand")
def code(
    context: typer.Context,
    target: Annotated[
        str, typer.Argument(help="Function name or address; an interior address focuses that site.")
    ],
    level: Annotated[
        str, typer.Option("--level", "-l", help="hlil, mlil, llil, or disasm.")
    ] = "hlil",
    ssa: Annotated[bool, typer.Option("--ssa", help="Show SSA form.")] = False,
    at: Annotated[
        str | None, typer.Option("--at", help="Focus on one native address.")
    ] = None,
    limit: Annotated[int, typer.Option("--limit", "-n", min=1, help="Maximum lines.")] = 200,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to read."),
    ] = None,
) -> None:
    """Read a function or site as HLIL, MLIL, LLIL, or disassembly."""
    _remote(
        context,
        "code",
        args={"target": target, "level": level, "ssa": ssa, "at": at, "limit": limit},
        session=session,
        text=code_text,
    )


@app.command(rich_help_panel="Understand")
def refs(
    context: typer.Context,
    target: Annotated[str, typer.Argument(help="Address, symbol, or function.")],
    from_target: Annotated[
        bool,
        typer.Option(
            "--from",
            help="Show outgoing refs; named functions scan the whole body.",
        ),
    ] = False,
    limit: Annotated[int, typer.Option("--limit", "-n", min=1, help="Maximum references.")] = 50,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to read."),
    ] = None,
) -> None:
    """Show code and data references at a site or across a function."""
    _remote(
        context,
        "refs",
        args={"target": target, "from": from_target, "limit": limit},
        session=session,
        text=refs_text,
    )


@app.command(rich_help_panel="Understand")
def sections(
    context: typer.Context,
    limit: Annotated[int, typer.Option("--limit", "-n", min=1, help="Maximum sections.")] = 50,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to read."),
    ] = None,
) -> None:
    """List the BinaryView sections."""
    _remote(
        context,
        "sections",
        args={"limit": limit},
        session=session,
        text=sections_text,
    )


@app.command(rich_help_panel="Understand")
def segments(
    context: typer.Context,
    limit: Annotated[int, typer.Option("--limit", "-n", min=1, help="Maximum segments.")] = 50,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to read."),
    ] = None,
) -> None:
    """List the BinaryView segments and file mappings."""
    _remote(
        context,
        "segments",
        args={"limit": limit},
        session=session,
        text=segments_text,
    )


@app.command(rich_help_panel="Change and persist")
def edit(
    context: typer.Context,
    target: Annotated[
        str,
        typer.Argument(help="Function, address, or variable such as main::length."),
    ],
    name: Annotated[str | None, typer.Option("--name", help="Set a user name.")] = None,
    type_text: Annotated[str | None, typer.Option("--type", help="Set a C type.")] = None,
    comment: Annotated[
        str | None,
        typer.Option("--comment", help="Set a comment; use - to remove it."),
    ] = None,
    scope: Annotated[
        str,
        typer.Option("--scope", help="Comment scope: auto, function, or view."),
    ] = "auto",
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to change."),
    ] = None,
) -> None:
    """Set a common name, type, or comment as one undoable change."""
    if comment == "-":
        comment = ""
    _remote(
        context,
        "edit",
        args={"target": target, "name": name, "type": type_text, "comment": comment, "scope": scope},
        session=session,
        text=edit_text,
    )


@app.command(rich_help_panel="Change and persist")
def patch(
    context: typer.Context,
    target: Annotated[str, typer.Argument(help="Address or symbol to patch.")],
    bytes_: Annotated[
        str, typer.Argument(help="Hex bytes, for example '90 90'.", metavar="BYTES")
    ],
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to change."),
    ] = None,
) -> None:
    """Replace raw bytes as one undoable change."""
    _remote(
        context,
        "patch",
        args={"target": target, "bytes": bytes_},
        session=session,
        text=patch_text,
    )


@app.command(rich_help_panel="Change and persist")
def undo(
    context: typer.Context,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to change."),
    ] = None,
) -> None:
    """Undo the last Binary Ninja change."""
    _remote(context, "undo", session=session, text=history_text)


@app.command(rich_help_panel="Change and persist")
def redo(
    context: typer.Context,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to change."),
    ] = None,
) -> None:
    """Redo the last undone Binary Ninja change."""
    _remote(context, "redo", session=session, text=history_text)


@app.command(rich_help_panel="Change and persist")
def save(
    context: typer.Context,
    path: Annotated[str | None, typer.Argument(help="New .bndb path.")] = None,
    server_path: Annotated[
        bool,
        typer.Option("--server-path", help="Use an absolute PATH visible only to Binary Ninja."),
    ] = False,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to save."),
    ] = None,
) -> None:
    """Save the current BNDB, or create one at PATH."""
    try:
        destination = None if path is None else _destination_path(path, server_path=server_path)
    except BnkError as error:
        _fail(error)
    _remote(
        context,
        "save",
        args={"path": destination},
        session=session,
        text=save_text,
    )


@app.command(rich_help_panel="Change and persist")
def export(
    context: typer.Context,
    path: Annotated[str, typer.Argument(help="Patched binary destination.")],
    server_path: Annotated[
        bool,
        typer.Option("--server-path", help="Use an absolute PATH visible only to Binary Ninja."),
    ] = False,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to export."),
    ] = None,
) -> None:
    """Export current binary bytes to PATH."""
    try:
        destination = _destination_path(path, server_path=server_path)
    except BnkError as error:
        _fail(error)
    _remote(
        context,
        "export",
        args={"path": destination},
        session=session,
        text=lambda value: save_text(value, verb="exported"),
    )


@app.command("eval", rich_help_panel="Python")
def evaluate(
    context: typer.Context,
    expression: Annotated[str, typer.Argument(help="Python expression.")],
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to use."),
    ] = None,
) -> None:
    """Evaluate unrestricted Python in a fresh Binary Ninja namespace."""
    _remote(
        context,
        "eval",
        args={"source": expression, "args": []},
        session=session,
        text=python_text,
    )


@app.command("exec", rich_help_panel="Python")
def execute(
    context: typer.Context,
    source: Annotated[str, typer.Argument(help="Python source, or - for stdin.")],
    arg: Annotated[list[str] | None, typer.Option("--arg", "-a", help="Script argument.")] = None,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to use."),
    ] = None,
) -> None:
    """Execute unrestricted Python source."""
    if source == "-":
        source = sys.stdin.read()
    _remote(
        context,
        "exec",
        args={"source": source, "args": arg or []},
        session=session,
        text=python_text,
    )


RUN_CONTEXT = {"allow_extra_args": True, "ignore_unknown_options": True}


@app.command("run", rich_help_panel="Python", context_settings=RUN_CONTEXT)
def run_script(
    context: typer.Context,
    path: Annotated[str, typer.Argument(help="Python script path.")],
    server: Annotated[
        bool, typer.Option("--server", help="Read the script on Binary Ninja's filesystem.")
    ] = False,
    session: Annotated[
        str | None,
        typer.Option("--session", "-s", envvar="BNK_SESSION", help="Session to use."),
    ] = None,
) -> None:
    """Run an unrestricted Python script; pass arguments after --."""
    args: dict[str, Any] = {"args": list(context.args)}
    if server:
        args["path"] = path
    else:
        try:
            script_path = Path(path).expanduser().resolve()
            args["source"] = script_path.read_text()
            args["path"] = None
            args["filename"] = str(script_path)
        except (OSError, UnicodeError) as error:
            _fail(BnkError(f"cannot read script {path}: {error}", kind="path"))
    _remote(context, "run", args=args, session=session, text=python_text)


def _endpoint(context: typer.Context) -> Endpoint:
    value = context.obj
    if not isinstance(value, Endpoint):
        raise RuntimeError("bnk CLI context was not initialized")
    return value


def _remote(
    context: typer.Context,
    action: str,
    *,
    text: Callable[[dict[str, Any]], str],
    args: dict[str, Any] | None = None,
    session: str | None = None,
) -> None:
    try:
        response = request(_endpoint(context), action, args, session=session)
        if not isinstance(response, dict):
            raise BnkError(f"{action} returned an invalid result", kind="protocol")
        typer.echo(text(response))
    except BnkError as error:
        _fail(error)


def _client_path(value: str) -> str:
    try:
        path = Path(value).expanduser().resolve()
    except OSError as error:
        raise BnkError(f"cannot resolve path {value}: {error}", kind="path") from error
    if not path.is_file():
        raise BnkError(f"not a regular file: {path}", kind="path", details={"path": str(path)})
    return str(path)


def _destination_path(value: str, *, server_path: bool) -> str:
    if server_path:
        path = Path(value).expanduser()
        if not path.is_absolute():
            raise BnkError("server destination must be absolute", kind="path")
        return str(path)
    try:
        path = Path(value).expanduser().resolve()
    except OSError as error:
        raise BnkError(f"cannot resolve destination {value}: {error}", kind="path") from error
    if not path.parent.is_dir():
        raise BnkError(f"destination directory does not exist: {path.parent}", kind="path")
    return str(path)


def _fail(error: BnkError) -> Never:
    typer.echo(error_text(str(error), kind=error.kind, details=error.details), err=True)
    raise typer.Exit(1)


def main() -> None:
    app(prog_name="bnk")
