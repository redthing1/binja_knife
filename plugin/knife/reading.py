from __future__ import annotations

from collections import Counter
from typing import Any

from .arguments import (
    boolean,
    bounded,
    choice,
    limit,
    only,
    optional_address,
    optional_string,
    parse_address,
    required_string,
)
from .sessions import SessionError, SessionStore
from .targets import (
    enum_name,
    hex_address,
    resolve_address,
    resolve_function,
    try_function,
    try_variable,
)


class ReadActions:
    def __init__(self, sessions: SessionStore) -> None:
        self.sessions = sessions

    def find(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        kind = choice(args, "kind", {"strings", "functions", "symbols", "bytes"})
        query = optional_string(args, "query")
        result_limit = limit(args)
        case_sensitive = boolean(args, "case_sensitive", False)
        expand_refs = boolean(args, "refs", False)
        symbol_filter = choice(args, "symbol_filter", {"all", "imports", "exports"}, "all")
        only(args, "kind", "query", "limit", "case_sensitive", "refs", "symbol_filter")

        if expand_refs and kind != "strings":
            raise SessionError("--refs is only valid for strings", kind="invalid_request")
        if symbol_filter != "all" and kind != "symbols":
            raise SessionError("symbol filters are only valid for symbols", kind="invalid_request")

        with self.sessions.use(session_name) as session:
            if kind == "strings":
                items, more = _find_strings(
                    session.bv, query, result_limit, case_sensitive, expand_refs
                )
            elif kind == "functions":
                items, more = _find_functions(session.bv, query, result_limit, case_sensitive)
            elif kind == "symbols":
                items, more = _find_symbols(
                    session.bv, query, result_limit, case_sensitive, symbol_filter
                )
            else:
                if not query:
                    raise SessionError("find bytes requires a hex pattern", kind="invalid_request")
                try:
                    pattern = bytes.fromhex(query)
                except ValueError as error:
                    raise SessionError("byte pattern must be hexadecimal", kind="invalid_request") from error
                if not pattern:
                    raise SessionError("byte pattern must not be empty", kind="invalid_request")
                items, more = _find_bytes(session.bv, pattern, result_limit)
        return {"kind": kind, "query": query, "items": items, "more": more}

    def inspect(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        target = required_string(args, "target")
        show_vars = boolean(args, "vars", False)
        variable_limit = limit(args)
        only(args, "target", "vars", "limit")
        with self.sessions.use(session_name) as session:
            view = session.bv
            variable = try_variable(view, target)
            if variable is not None:
                if show_vars:
                    raise SessionError("--vars requires a function target", kind="invalid_request")
                function = resolve_function(view, target.rsplit("::", 1)[0])
                return {
                    "target": target,
                    "variable": _variable_item(variable),
                    "function": _function_item(function),
                    "variable_target": True,
                }

            if parse_address(target) is not None:
                address = resolve_address(view, target)
                function = view.get_function_at(address)
            else:
                function = try_function(view, target)
                address = int(function.start) if function is not None else resolve_address(view, target)
            containers = list(view.get_functions_containing(address))
            if function is None and len(containers) == 1:
                function = containers[0]
            if show_vars and function is None:
                raise SessionError("--vars requires a function target", kind="invalid_request")
            string = view.get_string_at(address)
            symbol = view.get_symbol_at(address)
            data = view.get_data_var_at(address)
            sections = list(view.get_sections_at(address))
            segment = view.get_segment_at(address)
            blocks = list(view.get_basic_blocks_at(address))
            instruction_address = (
                function.get_instruction_containing_address(address)
                if function is not None and blocks else None
            )
            instruction_length = (
                int(view.get_instruction_length(instruction_address) or 0)
                if instruction_address is not None else 0
            )
            result: dict[str, Any] = {
                "target": target,
                "address": hex_address(address),
                "symbol": _symbol_item(symbol) if symbol is not None else None,
                "sections": [str(section.name) for section in sections],
                "segment": _segment_item(segment) if segment is not None else None,
                "instruction": view.get_disassembly(instruction_address)
                if instruction_address is not None else None,
                "instruction_address": hex_address(instruction_address)
                if instruction_address is not None else None,
                "bytes": bytes(view.read(instruction_address, instruction_length)).hex(" ")
                if instruction_length
                else None,
                "function": _function_item(function) if function is not None else None,
                "functions": (
                    [_function_item(item) for item in containers] if len(containers) > 1 else []
                ),
                "block": _block_item(blocks[0]) if len(blocks) == 1 else None,
                "string": (
                    _string_item(view, string, include_refs=False) if string is not None else None
                ),
                "data": (
                    _data_item(view, data)
                    if data is not None and function is None and string is None else None
                ),
                "view_comment": str(view.get_comment_at(address) or ""),
            }
            if function is not None:
                result["function_comment"] = str(function.get_comment_at(address) or "")
                if address == int(function.start) or show_vars:
                    variables = _useful_variables(function)
                    if not show_vars:
                        result["parameters"] = [
                            _variable_item(item) for item in variables if item.is_parameter_variable
                        ]
                    result["local_count"] = sum(not item.is_parameter_variable for item in variables)
                    if show_vars:
                        names = Counter(str(item.name) for item in variables)
                        result["variables"] = [
                            {**_variable_item(item), "ambiguous": names[str(item.name)] > 1}
                            for item in variables[:variable_limit]
                        ]
                        result["variables_more"] = max(0, len(variables) - variable_limit)
            return result

    def code(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        target = required_string(args, "target")
        level = choice(args, "level", {"hlil", "mlil", "llil", "disasm"}, "hlil")
        ssa = boolean(args, "ssa", False)
        at = optional_address(args, "at")
        line_limit = limit(args, default=200)
        only(args, "target", "level", "ssa", "at", "limit")
        if ssa and level == "disasm":
            raise SessionError("--ssa is not valid for disassembly", kind="invalid_request")

        with self.sessions.use(session_name) as session:
            function = resolve_function(session.bv, target)
            skip_reason = _skip_reason(function)
            if at is None:
                target_address = parse_address(target)
                if target_address is not None and target_address != int(function.start):
                    at = target_address
            instruction_address = (
                function.get_instruction_containing_address(at) if at is not None else None
            )
            if at is not None and instruction_address is None:
                raise SessionError(
                    f"no instruction in {function.name} contains {hex_address(at)}", kind="code"
                )
            shown, more = bounded(
                _code_lines(function, level, ssa=ssa, at=instruction_address), line_limit
            )
            return {
                "function": str(function.name),
                "address": hex_address(function.start),
                "level": level,
                "ssa": ssa,
                "at": hex_address(at) if at is not None else None,
                "instruction_address": hex_address(instruction_address)
                if instruction_address is not None else None,
                "lines": shown,
                "more": more,
                "skip_reason": skip_reason,
            }

    def refs(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        target = required_string(args, "target")
        outbound = boolean(args, "from", False)
        result_limit = limit(args)
        only(args, "target", "from", "limit")
        with self.sessions.use(session_name) as session:
            view = session.bv
            parsed_address = parse_address(target)
            if parsed_address is not None:
                function = None
                address = resolve_address(view, target)
            else:
                function = try_function(view, target)
                address = function.start if function is not None else resolve_address(view, target)
            entry_function = view.get_function_at(address) if parsed_address is not None else None
            site_function = function
            site_address = address
            if outbound and parsed_address is not None:
                containers = list(view.get_functions_containing(address))
                if len(containers) == 1:
                    site_function = containers[0]
                    containing_instruction = site_function.get_instruction_containing_address(
                        address
                    )
                    if containing_instruction is not None:
                        site_address = int(containing_instruction)

            if outbound and parsed_address is not None and entry_function is not None:
                site_items, site_more = bounded(
                    _outbound_refs(
                        view, entry_function, site_address, result_limit + 1, site_only=True
                    ),
                    result_limit,
                )
                function_items, function_more = bounded(
                    _outbound_refs(view, entry_function, address, result_limit + 1),
                    result_limit,
                )
                return {
                    "target": hex_address(address),
                    "address": hex_address(address),
                    "direction": "from",
                    "entry_function": str(entry_function.name),
                    "site_items": site_items,
                    "site_more": site_more,
                    "items": function_items,
                    "more": function_more,
                }

            references = (
                _outbound_refs(
                    view,
                    site_function,
                    site_address,
                    result_limit + 1,
                    site_only=parsed_address is not None,
                )
                if outbound
                else _inbound_refs(
                    view,
                    address,
                    call=function is not None or view.get_function_at(address) is not None,
                )
            )
            shown, more = bounded(references, result_limit)
            result = {
                "target": str(function.name) if function is not None else hex_address(address),
                "address": hex_address(address),
                "site_address": hex_address(site_address) if outbound else None,
                "site_function": (
                    str(site_function.name)
                    if outbound and parsed_address is not None and site_function is not None
                    else None
                ),
                "function_scope": outbound and parsed_address is None and function is not None,
                "direction": "from" if outbound else "to",
                "items": shown,
                "more": more,
            }
            if not outbound and parsed_address is not None:
                anchor = _containing_ref_anchor(view, address)
                if anchor is not None:
                    anchor_kind, anchor_address = anchor
                    anchor_items, anchor_more = bounded(
                        _inbound_refs(
                            view,
                            anchor_address,
                            call=view.get_function_at(anchor_address) is not None,
                        ),
                        result_limit,
                    )
                    if anchor_items:
                        result.update({
                            "anchor_kind": anchor_kind,
                            "anchor_address": hex_address(anchor_address),
                            "anchor_items": anchor_items,
                            "anchor_more": anchor_more,
                        })
            return result

    def sections(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        result_limit = limit(args)
        only(args, "limit")
        with self.sessions.use(session_name) as session:
            values = sorted(
                session.bv.sections.values(),
                key=lambda section: (int(section.start), int(section.end), str(section.name)),
            )
            shown, more = bounded(values, result_limit)
        return {"items": [_section_item(section) for section in shown], "more": more}

    def segments(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        result_limit = limit(args)
        only(args, "limit")
        with self.sessions.use(session_name) as session:
            values = sorted(
                session.bv.segments,
                key=lambda segment: (int(segment.start), int(segment.end)),
            )
            shown, more = bounded(values, result_limit)
        return {"items": [_segment_item(segment) for segment in shown], "more": more}


def _find_strings(
    view: Any,
    query: str | None,
    result_limit: int,
    case_sensitive: bool,
    expand_refs: bool,
) -> tuple[list[dict[str, Any]], bool]:
    found = []
    for string in view.get_strings():
        if _matches(str(string.value), query, case_sensitive):
            found.append(_string_item(view, string, include_refs=expand_refs))
            if len(found) > result_limit:
                break
    return bounded(found, result_limit)


def _find_functions(
    view: Any, query: str | None, result_limit: int, case_sensitive: bool
) -> tuple[list[dict[str, Any]], bool]:
    found = []
    for function in view.functions:
        if _matches(str(function.name), query, case_sensitive):
            found.append(_function_item(function))
            if len(found) > result_limit:
                break
    return bounded(found, result_limit)


def _find_symbols(
    view: Any,
    query: str | None,
    result_limit: int,
    case_sensitive: bool,
    symbol_filter: str,
) -> tuple[list[dict[str, Any]], bool]:
    found = []
    for symbol in view.get_symbols():
        type_name = enum_name(symbol.type)
        binding = enum_name(symbol.binding)
        imported = type_name in {
            "ImportedFunctionSymbol",
            "ImportAddressSymbol",
            "ImportedDataSymbol",
            "ExternalSymbol",
        }
        exported = not imported and binding in {"GlobalBinding", "WeakBinding"}
        if symbol_filter == "imports" and not imported:
            continue
        if symbol_filter == "exports" and not exported:
            continue
        if _matches(str(symbol.name), query, case_sensitive):
            found.append(_symbol_item(symbol))
            if len(found) > result_limit:
                break
    return bounded(found, result_limit)


def _find_bytes(view: Any, pattern: bytes, result_limit: int) -> tuple[list[dict[str, Any]], bool]:
    found = []
    for address, data in view.find_all_data(view.start, view.end, pattern):
        found.append({"address": hex_address(address), "bytes": bytes(data).hex(" ")})
        if len(found) > result_limit:
            break
    return bounded(found, result_limit)


def _code_lines(function: Any, level: str, *, ssa: bool, at: int | None) -> list[dict[str, Any]]:
    if level == "disasm":
        lines = []
        for block in function.basic_blocks:
            for line in block.get_disassembly_text():
                address = int(line.address)
                if at is None or address == at:
                    lines.append({"address": hex_address(address), "text": str(line)})
        return lines

    il = getattr(function, level)
    if il is None:
        skip_reason = _skip_reason(function)
        if skip_reason is not None:
            raise SessionError(
                f"{level} is unavailable: Binary Ninja skipped analysis ({skip_reason}); "
                "try --level disasm",
                kind="code",
            )
        raise SessionError(f"{level} is not available", kind="code")
    if at is not None:
        instructions = _mapped_instructions(function, level, at)
        if ssa:
            instructions = [instruction.ssa_form for instruction in instructions]
        if level == "hlil":
            statements = _hlil_statements(instructions, at)
        else:
            statements = [(instruction, int(instruction.address) == at) for instruction in instructions]
        items = []
        for instruction, direct in statements:
            item = _instruction_item(instruction)
            item["related"] = not direct
            items.append(item)
        return sorted(items, key=lambda item: item["related"])
    if ssa:
        il = il.ssa_form
    if level == "hlil" and il.root is not None:
        return [
            {"address": hex_address(line.address), "index": index, "text": str(line)}
            for index, line in enumerate(il.root.lines)
        ]
    return [
        _instruction_item(instruction)
        for instruction in il.instructions
    ]


def _mapped_instructions(function: Any, level: str, address: int) -> list[Any]:
    low_level = list(function.get_llils_at(address))
    if level == "llil":
        candidates = low_level
    elif level == "mlil":
        candidates = [mapped for instruction in low_level for mapped in instruction.mlils]
    else:
        candidates = [mapped for instruction in low_level for mapped in instruction.hlils]
    unique: dict[tuple[type[Any], int], Any] = {}
    for instruction in candidates:
        unique.setdefault((type(instruction), int(instruction.expr_index)), instruction)
    return list(unique.values())


def _hlil_statements(instructions: list[Any], address: int) -> list[tuple[Any, bool]]:
    unique: dict[int, tuple[Any, bool]] = {}
    for instruction in instructions:
        statement = instruction
        while statement.parent is not None and statement.parent.instr_index == statement.instr_index:
            statement = statement.parent
        key = int(statement.expr_index)
        direct = int(instruction.address) == address
        previous = unique.get(key)
        unique[key] = (statement, direct or (previous[1] if previous is not None else False))
    return list(unique.values())


def _instruction_item(instruction: Any, *, address: int | None = None) -> dict[str, Any]:
    instruction_index = instruction.instr_index
    return {
        "address": hex_address(instruction.address if address is None else address),
        "index": int(instruction_index) if instruction_index is not None else "-",
        "expression": int(instruction.expr_index),
        "text": str(instruction),
    }


def _inbound_refs(view: Any, address: int, *, call: bool) -> list[dict[str, Any]]:
    call_sites = (
        {int(ref.address) for ref in view.get_callers(address)}
        if call
        else set()
    )
    items = [
        _code_ref_item(
            ref,
            target=address,
            kind="call" if int(ref.address) in call_sites else "code",
        )
        for ref in view.get_code_refs(address)
    ]
    items.extend(
        {
            "kind": "data",
            "site": hex_address(site),
            "target": hex_address(address),
            "function": _containing_name(view, site),
        }
        for site in view.get_data_refs(address)
    )
    return items


def _containing_ref_anchor(view: Any, address: int) -> tuple[str, int] | None:
    string = view.get_string_at(address)
    if string is not None and int(string.start) != address:
        return "string", int(string.start)
    data = view.get_data_var_at(address)
    if data is not None and int(data.address) != address:
        return "data", int(data.address)
    functions = list(view.get_functions_containing(address))
    if len(functions) == 1:
        instruction = functions[0].get_instruction_containing_address(address)
        if instruction is not None and int(instruction) != address:
            return "instruction", int(instruction)
    return None


def _outbound_refs(
    view: Any,
    function: Any | None,
    address: int,
    max_items: int,
    *,
    site_only: bool = False,
) -> list[dict[str, Any]]:
    if function is None or site_only:
        sites = [address]
        call_sites = {int(ref.address) for ref in function.call_sites} if function is not None else set()
    else:
        call_sites = {int(ref.address) for ref in function.call_sites}
        sites = list(dict.fromkeys(int(site) for _, site in function.instructions))

    items: list[dict[str, Any]] = []
    seen: set[tuple[str, int, int | None]] = set()
    for site in sites:
        code_kind = "call" if site in call_sites else "code"
        code_targets = view.get_code_refs_from(site, func=function)
        for target in code_targets:
            if _append_reference(items, seen, view, code_kind, site, int(target), max_items):
                return items
        if site in call_sites and not code_targets:
            if _append_reference(items, seen, view, "call site", site, None, max_items):
                return items
        for target in view.get_data_refs_from(site):
            if _append_reference(items, seen, view, "data", site, int(target), max_items):
                return items
    return items


def _append_reference(
    items: list[dict[str, Any]],
    seen: set[tuple[str, int, int | None]],
    view: Any,
    kind: str,
    site: int,
    target: int | None,
    max_items: int,
) -> bool:
    key = (kind, site, target)
    if key not in seen:
        seen.add(key)
        items.append(
            {
                "kind": kind,
                "site": hex_address(site),
                "target": hex_address(target) if target is not None else "?",
                "function": _target_name(view, target) if target is not None else None,
            }
        )
    return len(items) >= max_items


def _code_ref_item(ref: Any, *, target: int, kind: str = "code") -> dict[str, Any]:
    function = getattr(ref, "function", None)
    return {
        "kind": kind,
        "site": hex_address(ref.address),
        "target": hex_address(target),
        "function": str(function.name) if function is not None else None,
    }


def _string_item(view: Any, string: Any, *, include_refs: bool) -> dict[str, Any]:
    code_refs = list(view.get_code_refs(string.start))
    data_refs = list(view.get_data_refs(string.start))
    item = {
        "address": hex_address(string.start),
        "type": enum_name(string.type),
        "length": int(string.length),
        "value": str(string.value),
        "refs": len(code_refs) + len(data_refs),
    }
    if include_refs:
        references = [
            *[_code_ref_item(ref, target=string.start) for ref in code_refs],
            *[
                {
                    "kind": "data",
                    "site": hex_address(site),
                    "target": hex_address(string.start),
                    "function": _containing_name(view, site),
                }
                for site in data_refs
            ],
        ]
        item["references"] = references[:20]
        item["references_more"] = max(0, len(references) - 20)
    return item


def _data_item(view: Any, data: Any) -> dict[str, Any]:
    value = data.value
    shown_value: str | None = None
    if isinstance(value, bool):
        shown_value = str(value)
    elif isinstance(value, int):
        shown_value = hex_address(value) if view.start <= value < view.end else str(value)
    elif isinstance(value, (float, str)) and len(str(value)) <= 80:
        shown_value = str(value)
    return {
        "address": hex_address(data.address),
        "type": str(data.type),
        "value": shown_value,
    }


def _function_item(function: Any) -> dict[str, Any]:
    return {
        "address": hex_address(function.start),
        "name": str(function.name),
        "type": str(function.type),
        "size": int(function.total_bytes),
        "blocks": len(list(function.basic_blocks)),
        "skip_reason": _skip_reason(function),
    }


def _skip_reason(function: Any) -> str | None:
    if not bool(getattr(function, "analysis_skipped", False)):
        return None
    reason = enum_name(function.analysis_skip_reason)
    return {
        "AlwaysSkipReason": "disabled",
        "ExceedFunctionSizeSkipReason": "function size limit",
        "ExceedFunctionAnalysisTimeSkipReason": "analysis time limit",
        "ExceedFunctionUpdateCountSkipReason": "analysis update limit",
        "NewAutoFunctionAnalysisSuppressedReason": "automatic function analysis suppressed",
        "BasicAnalysisSkipReason": "basic analysis only",
        "IntermediateAnalysisSkipReason": "intermediate analysis only",
        "AnalysisPipelineSuspendedReason": "analysis pipeline suspended",
        "NoSkipReason": "reason unavailable",
    }.get(reason, reason)


def _symbol_item(symbol: Any) -> dict[str, Any]:
    return {
        "address": hex_address(symbol.address),
        "name": str(symbol.name),
        "type": enum_name(symbol.type),
        "binding": enum_name(symbol.binding),
    }


def _variable_item(variable: Any) -> dict[str, Any]:
    return {
        "target": f"#{int(variable.identifier)}",
        "name": str(variable.name),
        "type": str(variable.type),
        "parameter": bool(variable.is_parameter_variable),
    }


def _useful_variables(function: Any) -> list[Any]:
    il = getattr(function, "hlil", None)
    values = list(il.vars) if il is not None else list(function.vars)
    unique: dict[int, Any] = {}
    for variable in values:
        unique.setdefault(int(variable.identifier), variable)
    return sorted(
        unique.values(),
        key=lambda variable: (not bool(variable.is_parameter_variable), str(variable.name)),
    )


def _block_item(block: Any) -> dict[str, Any]:
    return {"start": hex_address(block.start), "end": hex_address(block.end)}


def _section_item(section: Any) -> dict[str, Any]:
    return {
        "name": str(section.name),
        "start": hex_address(section.start),
        "end": hex_address(section.end),
        "length": int(section.length),
        "semantics": enum_name(section.semantics),
    }


def _segment_item(segment: Any) -> dict[str, Any]:
    file_offset = int(segment.data_offset)
    file_length = int(segment.data_length)
    return {
        "start": hex_address(segment.start),
        "end": hex_address(segment.end),
        "length": int(segment.length),
        "file_offset": hex_address(file_offset),
        "file_end": hex_address(file_offset + file_length),
        "file_length": file_length,
        "readable": bool(segment.readable),
        "writable": bool(segment.writable),
        "executable": bool(segment.executable),
    }


def _containing_name(view: Any, address: int) -> str | None:
    functions = list(view.get_functions_containing(address))
    return str(functions[0].name) if len(functions) == 1 else None


def _target_name(view: Any, address: int) -> str | None:
    symbol = view.get_symbol_at(address)
    return str(symbol.name) if symbol is not None else _containing_name(view, address)


def _matches(value: str, query: str | None, case_sensitive: bool) -> bool:
    if query is None:
        return True
    return query in value if case_sensitive else query.casefold() in value.casefold()
