from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Dict, List

from .tools.functions import (
    function_callees,
    function_call_sites,
    function_callers,
    function_summary,
    functions_like,
    functions_list,
)
from .tools.il import hlil, llil, mlil
from .tools.imports import imports_like, imports_list
from .tools.sections import sections_list
from .tools.segments import segments_list
from .tools.strings import strings_like, strings_like_data, xrefs_to_string
from .tools.symbols import symbols_like
from .tools.tags import tags_at, tags_function, tags_list, tags_types
from .tools.xrefs import xrefs_to
from .tools.edit_comments import comment_func_set, comment_view_set
from .tools.edit_db import db_save, db_save_as, db_status
from .tools.edit_functions import fn_rename, fn_set_type
from .tools.edit_tags import (
    tag_data_add,
    tag_data_remove_type,
    tag_func_add,
    tag_func_remove_type,
)
from .tools.edit_vars import var_list, var_rename, var_set_type
from .tools.edit_xrefs import (
    xref_code_add,
    xref_code_remove,
    xref_data_add,
    xref_data_remove,
)


@dataclass(frozen=True)
class Tool:
    name: str
    fn: Callable[..., Any]
    doc: str


_TOOLS: List[Tool] = [
    Tool(name="function.callees", fn=function_callees, doc="callees of a function"),
    Tool(
        name="function.call-sites",
        fn=function_call_sites,
        doc="call site addresses in a function",
    ),
    Tool(name="function.callers", fn=function_callers, doc="callers of a function"),
    Tool(name="function.summary", fn=function_summary, doc="basic function metadata"),
    Tool(
        name="functions.like",
        fn=functions_like,
        doc="substring search over function names",
    ),
    Tool(name="functions.list", fn=functions_list, doc="list functions"),
    Tool(name="il.hlil", fn=hlil, doc="HLIL for a function (name or address)"),
    Tool(name="il.llil", fn=llil, doc="LLIL for a function (name or address)"),
    Tool(name="il.mlil", fn=mlil, doc="MLIL for a function (name or address)"),
    Tool(name="imports.like", fn=imports_like, doc="substring search over imports"),
    Tool(name="imports.list", fn=imports_list, doc="list imported symbols"),
    Tool(name="sections.list", fn=sections_list, doc="list sections"),
    Tool(name="segments.list", fn=segments_list, doc="list segments"),
    Tool(
        name="strings.like", fn=strings_like, doc="substring search over bv.get_strings"
    ),
    Tool(
        name="strings.like-data",
        fn=strings_like_data,
        doc="raw byte search + nearby c-string extraction",
    ),
    Tool(
        name="strings.xrefs",
        fn=xrefs_to_string,
        doc="raw byte search + xrefs for each match",
    ),
    Tool(name="symbols.like", fn=symbols_like, doc="substring search over symbols"),
    Tool(name="tags.at", fn=tags_at, doc="data tags at an address"),
    Tool(name="tags.function", fn=tags_function, doc="function tags for a function"),
    Tool(name="tags.list", fn=tags_list, doc="list data tags (optionally filtered)"),
    Tool(name="tags.types", fn=tags_types, doc="list tag types present in the view"),
    Tool(name="xrefs.to", fn=xrefs_to, doc="xrefs to an address or symbol name"),
    Tool(name="edit.fn.rename", fn=fn_rename, doc="rename a function"),
    Tool(name="edit.fn.type", fn=fn_set_type, doc="set a user function type"),
    Tool(name="edit.var.list", fn=var_list, doc="list variables in a function"),
    Tool(name="edit.var.rename", fn=var_rename, doc="rename a variable"),
    Tool(name="edit.var.type", fn=var_set_type, doc="set a variable type"),
    Tool(
        name="edit.comment.view",
        fn=comment_view_set,
        doc="set a view comment at an address",
    ),
    Tool(
        name="edit.comment.func",
        fn=comment_func_set,
        doc="set a function comment at an address",
    ),
    Tool(
        name="edit.db.status", fn=db_status, doc="database status for the current view"
    ),
    Tool(name="edit.db.save", fn=db_save, doc="save database to its current file"),
    Tool(name="edit.db.save-as", fn=db_save_as, doc="save database to a new bndb path"),
    Tool(name="edit.tag.data.add", fn=tag_data_add, doc="add a data tag"),
    Tool(
        name="edit.tag.data.remove-type",
        fn=tag_data_remove_type,
        doc="remove all data tags of a type at an address",
    ),
    Tool(
        name="edit.tag.func.add", fn=tag_func_add, doc="add a function or address tag"
    ),
    Tool(
        name="edit.tag.func.remove-type",
        fn=tag_func_remove_type,
        doc="remove all function or address tags of a type",
    ),
    Tool(name="edit.xref.data.add", fn=xref_data_add, doc="add a user data xref"),
    Tool(
        name="edit.xref.data.remove", fn=xref_data_remove, doc="remove a user data xref"
    ),
    Tool(name="edit.xref.code.add", fn=xref_code_add, doc="add a user code xref"),
    Tool(
        name="edit.xref.code.remove", fn=xref_code_remove, doc="remove a user code xref"
    ),
]


def list_tools() -> List[Dict[str, Any]]:
    out: List[Dict[str, Any]] = []
    for tool in _TOOLS:
        out.append({"name": tool.name, "doc": tool.doc})
    return out


def call_tool(name: str, *, bv, **params) -> Any:
    if bv is None:
        raise ValueError("bv is required (attach a view first)")
    for tool in _TOOLS:
        if tool.name == name:
            return tool.fn(bv=bv, **params)
    known = ", ".join(t.name for t in _TOOLS)
    raise KeyError(f"unknown tool: {name!r} (known: {known})")
