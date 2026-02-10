from __future__ import annotations

import sys
from pathlib import Path
from typing import Any, Dict, Optional

import typer

from .cli_app import make_app
from .cli_ctx import cfg_from_ctx, print_value, serverlib_call


app = make_app()
fn_app = make_app()
var_app = make_app()
comment_app = make_app()
xref_app = make_app()
tag_app = make_app()
db_app = make_app()

xref_data_app = make_app()
xref_code_app = make_app()

app.add_typer(fn_app, name="fn")
app.add_typer(var_app, name="var")
app.add_typer(comment_app, name="comment")
app.add_typer(xref_app, name="xref")
app.add_typer(tag_app, name="tag")
app.add_typer(db_app, name="db")

xref_app.add_typer(xref_data_app, name="data")
xref_app.add_typer(xref_code_app, name="code")

tag_data_app = make_app()
tag_func_app = make_app()
tag_app.add_typer(tag_data_app, name="data")
tag_app.add_typer(tag_func_app, name="func")


def _edit(ctx: typer.Context, tool: str, params: Dict[str, Any]) -> None:
    cfg = cfg_from_ctx(ctx)
    out = serverlib_call(cfg, tool, params)
    print_value(cfg, out)


@fn_app.command("rename")
def fn_rename(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(...),
    new_name: str = typer.Argument(...),
    analysis: str = typer.Option("none", "--analysis", help="none|update|wait"),
) -> None:
    _edit(
        ctx,
        "edit.fn.rename",
        {"name_or_addr": name_or_addr, "new_name": new_name, "analysis": analysis},
    )


@fn_app.command("type")
def fn_type(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(...),
    proto: str = typer.Argument(..., help="C function prototype string"),
    analysis: str = typer.Option("update", "--analysis", help="none|update|wait"),
) -> None:
    _edit(
        ctx,
        "edit.fn.type",
        {"name_or_addr": name_or_addr, "proto": proto, "analysis": analysis},
    )


@var_app.command("list")
def var_list(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(..., help="function name or address"),
) -> None:
    _edit(ctx, "edit.var.list", {"name_or_addr": name_or_addr})


@var_app.command("rename")
def var_rename(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(..., help="function name or address"),
    var: str = typer.Argument(
        ..., help="variable identifier (hex/dec) or variable name"
    ),
    new_name: str = typer.Argument(...),
    by: str = typer.Option("auto", "--by", help="auto|ident|name"),
    analysis: str = typer.Option("update", "--analysis", help="none|update|wait"),
) -> None:
    _edit(
        ctx,
        "edit.var.rename",
        {
            "name_or_addr": name_or_addr,
            "var": var,
            "new_name": new_name,
            "by": by,
            "analysis": analysis,
        },
    )


@var_app.command("type")
def var_type(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(..., help="function name or address"),
    var: str = typer.Argument(
        ..., help="variable identifier (hex/dec) or variable name"
    ),
    type_str: str = typer.Argument(..., help="C type string"),
    by: str = typer.Option("auto", "--by", help="auto|ident|name"),
    analysis: str = typer.Option("update", "--analysis", help="none|update|wait"),
) -> None:
    _edit(
        ctx,
        "edit.var.type",
        {
            "name_or_addr": name_or_addr,
            "var": var,
            "type": type_str,
            "by": by,
            "analysis": analysis,
        },
    )


def _read_text_arg(text: str) -> str:
    if text == "-":
        return sys.stdin.read()
    return text


@comment_app.command("view")
def comment_view(
    ctx: typer.Context,
    addr: str = typer.Argument(...),
    comment: str = typer.Argument(..., help="comment text, or '-' to read from stdin"),
) -> None:
    _edit(
        ctx,
        "edit.comment.view",
        {"addr": addr, "comment": _read_text_arg(comment)},
    )


@comment_app.command("func")
def comment_func(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(..., help="function name or address"),
    addr: str = typer.Argument(...),
    comment: str = typer.Argument(..., help="comment text, or '-' to read from stdin"),
) -> None:
    _edit(
        ctx,
        "edit.comment.func",
        {
            "name_or_addr": name_or_addr,
            "addr": addr,
            "comment": _read_text_arg(comment),
        },
    )


@xref_data_app.command("add")
def xref_data_add(
    ctx: typer.Context,
    from_addr: str = typer.Argument(...),
    to_addr: str = typer.Argument(...),
) -> None:
    _edit(ctx, "edit.xref.data.add", {"from_addr": from_addr, "to_addr": to_addr})


@xref_data_app.command("remove")
def xref_data_remove(
    ctx: typer.Context,
    from_addr: str = typer.Argument(...),
    to_addr: str = typer.Argument(...),
) -> None:
    _edit(ctx, "edit.xref.data.remove", {"from_addr": from_addr, "to_addr": to_addr})


@xref_code_app.command("add")
def xref_code_add(
    ctx: typer.Context,
    from_addr: str = typer.Argument(...),
    to_addr: str = typer.Argument(...),
    function: Optional[str] = typer.Option(
        None, "--function", "-f", help="function name or address (optional)"
    ),
) -> None:
    _edit(
        ctx,
        "edit.xref.code.add",
        {"from_addr": from_addr, "to_addr": to_addr, "function": function},
    )


@xref_code_app.command("remove")
def xref_code_remove(
    ctx: typer.Context,
    from_addr: str = typer.Argument(...),
    to_addr: str = typer.Argument(...),
    function: Optional[str] = typer.Option(
        None, "--function", "-f", help="function name or address (optional)"
    ),
) -> None:
    _edit(
        ctx,
        "edit.xref.code.remove",
        {"from_addr": from_addr, "to_addr": to_addr, "function": function},
    )


@tag_data_app.command("add")
def tag_data_add(
    ctx: typer.Context,
    addr: str = typer.Argument(...),
    tag_type: str = typer.Argument(...),
    data: str = typer.Argument(..., help="tag data, or '-' to read from stdin"),
    auto: bool = typer.Option(
        False, "--auto", help="create an auto tag (not user tag)"
    ),
) -> None:
    _edit(
        ctx,
        "edit.tag.data.add",
        {
            "addr": addr,
            "tag_type": tag_type,
            "data": _read_text_arg(data),
            "user": not auto,
        },
    )


@tag_data_app.command("remove-type")
def tag_data_remove_type(
    ctx: typer.Context,
    addr: str = typer.Argument(...),
    tag_type: str = typer.Argument(...),
    auto: bool = typer.Option(False, "--auto", help="remove auto tags (not user tags)"),
) -> None:
    _edit(
        ctx,
        "edit.tag.data.remove-type",
        {"addr": addr, "tag_type": tag_type, "user": not auto},
    )


@tag_func_app.command("add")
def tag_func_add(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(..., help="function name or address"),
    tag_type: str = typer.Argument(...),
    data: str = typer.Argument(..., help="tag data, or '-' to read from stdin"),
    addr: Optional[str] = typer.Option(None, "--addr", help="add an address tag"),
    auto: bool = typer.Option(False, "--auto", help="create an auto tag"),
) -> None:
    _edit(
        ctx,
        "edit.tag.func.add",
        {
            "name_or_addr": name_or_addr,
            "tag_type": tag_type,
            "data": _read_text_arg(data),
            "addr": addr,
            "auto": auto,
        },
    )


@tag_func_app.command("remove-type")
def tag_func_remove_type(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(..., help="function name or address"),
    tag_type: str = typer.Argument(...),
    addr: Optional[str] = typer.Option(
        None, "--addr", help="remove address tags at addr"
    ),
    auto: bool = typer.Option(False, "--auto", help="remove auto tags"),
) -> None:
    _edit(
        ctx,
        "edit.tag.func.remove-type",
        {
            "name_or_addr": name_or_addr,
            "tag_type": tag_type,
            "addr": addr,
            "auto": auto,
        },
    )


@db_app.command("status")
def db_status(ctx: typer.Context) -> None:
    _edit(ctx, "edit.db.status", {})


@db_app.command("save")
def db_save(ctx: typer.Context) -> None:
    _edit(ctx, "edit.db.save", {})


@db_app.command("save-as")
def db_save_as(
    ctx: typer.Context,
    path: Path = typer.Argument(..., help="destination .bndb path"),
) -> None:
    dest = path.expanduser().resolve()
    _edit(ctx, "edit.db.save-as", {"path": str(dest)})
