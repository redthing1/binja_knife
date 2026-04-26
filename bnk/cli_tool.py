from __future__ import annotations

import json
from typing import Any, Dict, Optional

import typer

from .cli_app import make_app
from .cli_ctx import (
    cfg_from_ctx,
    parse_kv_args,
    print_value,
    serverlib_call,
    serverlib_list,
)


app = make_app()
tags_app = make_app()
app.add_typer(tags_app, name="tags")


def _call(ctx: typer.Context, tool: str, params: Dict[str, Any]) -> None:
    cfg = cfg_from_ctx(ctx)
    out = serverlib_call(cfg, tool, params)
    print_value(cfg, out)


def _auto_flag_value(*, auto: bool, user: bool) -> Optional[bool]:
    if auto and user:
        raise typer.BadParameter("--auto and --user are mutually exclusive")
    if auto:
        return True
    if user:
        return False
    return None


@app.command("list")
def tool_list(ctx: typer.Context) -> None:
    cfg = cfg_from_ctx(ctx)
    out = serverlib_list(cfg)
    print_value(cfg, out)


@app.command("call")
def tool_call(
    ctx: typer.Context,
    tool: str = typer.Argument(..., help="tool name, e.g. strings.like-data"),
    kv: list[str] = typer.Argument([], help="KEY=VALUE (repeatable)"),
    params_json: Optional[str] = typer.Option(
        None, "--params-json", "-J", help="json object"
    ),
    arg: list[str] = typer.Option([], "--arg", "-a", help="KEY=VALUE"),
) -> None:
    cfg = cfg_from_ctx(ctx)

    params: Dict[str, Any] = {}
    if params_json:
        try:
            params = json.loads(params_json)
        except Exception as exc:
            raise typer.BadParameter(f"invalid --params-json: {exc}") from exc
        if not isinstance(params, dict):
            raise typer.BadParameter("--params-json must be a json object")

    params.update(parse_kv_args(list(kv)))
    params.update(parse_kv_args(list(arg)))

    out = serverlib_call(cfg, tool, params)
    print_value(cfg, out)


@app.command("summary")
def tool_summary(
    ctx: typer.Context,
    function_sample_limit: int = typer.Option(10, "--function-sample-limit", "-F"),
    import_sample_limit: int = typer.Option(10, "--import-sample-limit", "-I"),
    string_sample_limit: int = typer.Option(10, "--string-sample-limit", "-S"),
) -> None:
    _call(
        ctx,
        "binary.summary",
        {
            "function_sample_limit": function_sample_limit,
            "import_sample_limit": import_sample_limit,
            "string_sample_limit": string_sample_limit,
        },
    )


@app.command("function")
def tool_function(ctx: typer.Context, name_or_addr: str = typer.Argument(...)) -> None:
    _call(ctx, "function.info", {"name_or_addr": name_or_addr})


@app.command("hlil")
def tool_hlil(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(...),
    max_lines: Optional[int] = typer.Option(None, "--max-lines", "-n"),
) -> None:
    _call(ctx, "il.hlil", {"name_or_addr": name_or_addr, "max_lines": max_lines})


@app.command("mlil")
def tool_mlil(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(...),
    max_lines: Optional[int] = typer.Option(None, "--max-lines", "-n"),
) -> None:
    _call(ctx, "il.mlil", {"name_or_addr": name_or_addr, "max_lines": max_lines})


@app.command("llil")
def tool_llil(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(...),
    max_lines: Optional[int] = typer.Option(None, "--max-lines", "-n"),
) -> None:
    _call(ctx, "il.llil", {"name_or_addr": name_or_addr, "max_lines": max_lines})


@app.command("sections")
def tool_sections(ctx: typer.Context) -> None:
    _call(ctx, "sections.list", {})


@app.command("segments")
def tool_segments(ctx: typer.Context) -> None:
    _call(ctx, "segments.list", {})


@app.command("imports")
def tool_imports(
    ctx: typer.Context,
    pattern: Optional[str] = typer.Argument(None),
    case_insensitive: bool = typer.Option(
        True,
        "--case-insensitive/--case-sensitive",
        "-i/-I",
        show_default=False,
    ),
    regex: bool = typer.Option(
        False, "--regex/--no-regex", "-r/-R", show_default=False
    ),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
) -> None:
    if pattern:
        _call(
            ctx,
            "imports.like",
            {
                "pattern": pattern,
                "case_insensitive": case_insensitive,
                "regex": regex,
                "limit": limit,
            },
        )
    else:
        _call(ctx, "imports.list", {"limit": limit})


@app.command("strings")
def tool_strings(
    ctx: typer.Context,
    pattern: str = typer.Argument(...),
    section: Optional[str] = typer.Option(None, "--section", "-S"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    case_insensitive: bool = typer.Option(
        True,
        "--case-insensitive/--case-sensitive",
        "-i/-I",
        show_default=False,
    ),
    regex: bool = typer.Option(
        False, "--regex/--no-regex", "-r/-R", show_default=False
    ),
    data: bool = typer.Option(False, "--data", "-d", help="raw bytes"),
    xrefs: bool = typer.Option(False, "--xrefs", "-x", help="with xrefs"),
    max_len: int = typer.Option(
        256, "--max-len", "-m", help="max c-string len"
    ),
    string_limit: Optional[int] = typer.Option(None, "--string-limit", "-L"),
    xref_limit: Optional[int] = typer.Option(None, "--xref-limit", "-X"),
) -> None:
    if data and xrefs:
        raise typer.BadParameter("--data and --xrefs are mutually exclusive")

    if xrefs:
        _call(
            ctx,
            "strings.xrefs",
            {
                "pattern": pattern,
                "section": section,
                "case_insensitive": case_insensitive,
                "regex": regex,
                "string_limit": string_limit,
                "xref_limit": xref_limit,
            },
        )
        return

    if data:
        _call(
            ctx,
            "strings.like-data",
            {
                "pattern": pattern,
                "section": section,
                "case_insensitive": case_insensitive,
                "regex": regex,
                "limit": limit,
                "max_len": max_len,
            },
        )
        return

    _call(
        ctx,
        "strings.like",
        {
            "pattern": pattern,
            "section": section,
            "case_insensitive": case_insensitive,
            "regex": regex,
            "limit": limit,
        },
    )


@app.command("functions")
def tool_functions(
    ctx: typer.Context,
    pattern: Optional[str] = typer.Argument(None),
    include_imports: bool = typer.Option(
        True, "--include-imports/--no-include-imports", show_default=False
    ),
    case_insensitive: bool = typer.Option(
        True,
        "--case-insensitive/--case-sensitive",
        "-i/-I",
        show_default=False,
    ),
    regex: bool = typer.Option(
        False, "--regex/--no-regex", "-r/-R", show_default=False
    ),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
) -> None:
    if pattern:
        _call(
            ctx,
            "functions.like",
            {
                "pattern": pattern,
                "include_imports": include_imports,
                "case_insensitive": case_insensitive,
                "regex": regex,
                "limit": limit,
            },
        )
    else:
        _call(
            ctx,
            "functions.list",
            {"include_imports": include_imports, "limit": limit},
        )


@app.command("symbols")
def tool_symbols(
    ctx: typer.Context,
    pattern: str = typer.Argument(...),
    symbol_type: str = typer.Option("function", "--type", "-t"),
    case_insensitive: bool = typer.Option(
        True,
        "--case-insensitive/--case-sensitive",
        "-i/-I",
        show_default=False,
    ),
    regex: bool = typer.Option(
        False, "--regex/--no-regex", "-r/-R", show_default=False
    ),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
) -> None:
    _call(
        ctx,
        "symbols.like",
        {
            "pattern": pattern,
            "symbol_type": symbol_type,
            "case_insensitive": case_insensitive,
            "regex": regex,
            "limit": limit,
        },
    )


@app.command("callers")
def tool_callers(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(...),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
) -> None:
    _call(ctx, "function.callers", {"name_or_addr": name_or_addr, "limit": limit})


@app.command("callees")
def tool_callees(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(...),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
) -> None:
    _call(ctx, "function.callees", {"name_or_addr": name_or_addr, "limit": limit})


@app.command("call-sites")
def tool_call_sites(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(...),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
) -> None:
    _call(ctx, "function.call-sites", {"name_or_addr": name_or_addr, "limit": limit})


@app.command("xrefs")
def tool_xrefs(
    ctx: typer.Context,
    target: str = typer.Argument(...),
    code: bool = typer.Option(True, "--code/--no-code", "-c/-C", show_default=False),
    data: bool = typer.Option(True, "--data/--no-data", "-d/-D", show_default=False),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
) -> None:
    _call(
        ctx,
        "xrefs.to",
        {"target": target, "include_code": code, "include_data": data, "limit": limit},
    )


@tags_app.command("types")
def tool_tags_types(ctx: typer.Context) -> None:
    _call(ctx, "tags.types", {})


@tags_app.command("list")
def tool_tags_list(
    ctx: typer.Context,
    tag_type: Optional[str] = typer.Option(None, "--type", "-t"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    auto: bool = typer.Option(False, "--auto", "-a", help="auto tags"),
    user: bool = typer.Option(False, "--user", "-u", help="user tags"),
) -> None:
    _call(
        ctx,
        "tags.list",
        {
            "tag_type": tag_type,
            "limit": limit,
            "auto": _auto_flag_value(auto=auto, user=user),
        },
    )


@tags_app.command("at")
def tool_tags_at(
    ctx: typer.Context,
    addr: str = typer.Argument(...),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    auto: bool = typer.Option(False, "--auto", "-a", help="auto tags"),
    user: bool = typer.Option(False, "--user", "-u", help="user tags"),
) -> None:
    _call(
        ctx,
        "tags.at",
        {"addr": addr, "limit": limit, "auto": _auto_flag_value(auto=auto, user=user)},
    )


@tags_app.command("function")
def tool_tags_function(
    ctx: typer.Context,
    name_or_addr: str = typer.Argument(...),
    tag_type: Optional[str] = typer.Option(None, "--type", "-t"),
    limit: Optional[int] = typer.Option(None, "--limit", "-l"),
    auto: bool = typer.Option(False, "--auto", "-a", help="auto tags"),
    user: bool = typer.Option(False, "--user", "-u", help="user tags"),
) -> None:
    _call(
        ctx,
        "tags.function",
        {
            "name_or_addr": name_or_addr,
            "tag_type": tag_type,
            "limit": limit,
            "auto": _auto_flag_value(auto=auto, user=user),
        },
    )
