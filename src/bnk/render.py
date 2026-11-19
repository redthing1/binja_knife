from __future__ import annotations

import shlex
from typing import Any

from bnk.protocol import API_VERSION


def status_text(value: dict[str, Any]) -> str:
    listen = value.get("listen")
    endpoint = "unknown"
    if isinstance(listen, dict):
        host = listen.get("host")
        port = listen.get("port")
        if isinstance(host, str) and isinstance(port, int):
            endpoint = _line(f"{host}:{port}")

    uptime = value.get("uptime_seconds")
    uptime_text = f"{uptime:.3f}s" if isinstance(uptime, (int, float)) else "unknown"
    rows = [
        ("connect", _line(value.get("connect", "unknown"))),
        ("listen", endpoint),
        ("client", _line(f"{value.get('client_version', 'unknown')} (api {API_VERSION})")),
        (
            "server",
            _line(f"{value.get('server_version', 'unknown')} (api {value.get('api', 'unknown')})"),
        ),
        ("binary ninja", _line(value.get("binary_ninja_version", "unknown"))),
        ("uptime", uptime_text),
    ]
    if value.get("compatible") is False:
        rows.append(("compatible", "no"))
    width = max(len(label) for label, _ in rows)
    return "\n".join(f"{label:<{width}}  {item}" for label, item in rows)


def sessions_text(value: dict[str, Any]) -> str:
    sessions = value.get("sessions")
    if not isinstance(sessions, list) or not sessions:
        return "no sessions"
    rows = []
    for item in sessions:
        if not isinstance(item, dict):
            continue
        name = _line(item.get("name", "unknown"))
        state = _line(item.get("state", "unknown"))
        path = _line(item.get("path", "unknown"))
        if state == "opening":
            detail = _seconds(item.get("elapsed_seconds"))
        else:
            active = item.get("active")
            active_count = active if isinstance(active, int) else 0
            detail = f"active {active_count}  {_seconds(item.get('age_seconds'))}"
        rows.append((name, state, detail, path))
    if not rows:
        return "no sessions"
    widths = [max(len(row[index]) for row in rows) for index in range(3)]
    return "\n".join(
        f"{name:<{widths[0]}}  {state:<{widths[1]}}  {detail:<{widths[2]}}  {path}"
        for name, state, detail, path in rows
    )


def open_text(value: dict[str, Any]) -> str:
    verb = "reused" if value.get("reused") else "opened"
    rows = [
        ("path", _line(value.get("path", "unknown"))),
        ("view", _line(value.get("view", "unknown"))),
        ("architecture", _optional(value.get("architecture"))),
        ("analysis", _line(value.get("analysis", "unknown"))),
        ("functions", _line(value.get("function_count", "unknown"))),
    ]
    return f"{verb} {_line(value.get('session', 'unknown'))}\n{_rows(rows)}"


def summary_text(value: dict[str, Any]) -> str:
    start = _line(value.get("start", "unknown"))
    end = _line(value.get("end", "unknown"))
    length = _line(value.get("length", "unknown"))
    rows = [
        ("session", _line(value.get("session", "unknown"))),
        ("path", _line(value.get("path", "unknown"))),
        ("view", _line(value.get("view", "unknown"))),
        ("architecture", _optional(value.get("architecture"))),
        ("platform", _optional(value.get("platform"))),
        ("range", f"{start}..{end} ({length} bytes)"),
        ("entry", _line(value.get("entry", "unknown"))),
        ("analysis", _line(value.get("analysis", "unknown"))),
        ("functions", _line(value.get("function_count", "unknown"))),
    ]
    if value.get("skipped_function_count"):
        count = value["skipped_function_count"]
        rows.append(("skipped", f"{count} {'function' if count == 1 else 'functions'}"))
    rows.extend(
        [
            ("imports", _line(value.get("import_count", "unknown"))),
            ("strings", _line(value.get("string_count", "unknown"))),
            ("sections", _line(value.get("section_count", "unknown"))),
            ("segments", _line(value.get("segment_count", "unknown"))),
            ("database", "yes" if value.get("has_database") else "no"),
            ("dirty", _dirty(value)),
        ]
    )
    return _rows(rows)


def close_text(value: dict[str, Any]) -> str:
    suffix = " (discarded changes)" if value.get("discarded") else ""
    session = _line(value.get("session", "unknown"))
    path = _line(value.get("path", "unknown"))
    return f"closed {session}{suffix}\npath  {path}"


def find_text(value: dict[str, Any]) -> str:
    kind = value.get("kind")
    items = value.get("items")
    if not isinstance(items, list) or not items:
        return f"no {kind or 'results'} found"
    lines: list[str] = []
    for item in items:
        if not isinstance(item, dict):
            continue
        if kind == "strings":
            lines.append(
                f"{_line(item.get('address', '?'))}  {_line(item.get('type', '?'))}  "
                f"{item.get('length', '?')} bytes  {item.get('refs', '?')} refs  "
                f"{_line(item.get('value', ''))}"
            )
            references = item.get("references")
            if isinstance(references, list):
                lines.extend(f"  {_reference_line(ref)}" for ref in references if isinstance(ref, dict))
                if item.get("references_more"):
                    lines.append(
                        f"  … {item['references_more']} more references; "
                        f"run bnk refs {_line(item.get('address', '?'))}"
                    )
        elif kind == "functions":
            skip = (
                f"  [analysis skipped: {_line(item['skip_reason'])}]"
                if item.get("skip_reason") else ""
            )
            lines.append(
                f"{_line(item.get('address', '?'))}  {_line(item.get('name', '?'))}  "
                f"{item.get('size', '?')} bytes  {item.get('blocks', '?')} blocks{skip}\n"
                f"  {_line(item.get('type', ''))}"
            )
        elif kind == "symbols":
            lines.append(
                f"{_line(item.get('address', '?'))}  {_line(item.get('type', '?'))}  "
                f"{_line(item.get('name', '?'))}"
            )
        elif kind == "types":
            lines.append(
                f"{_type_target(item['target'])}  {_byte_size(item['size'])}  {_line(item['kind'])}\n"
                f"  {_line(item['text'])}"
            )
        else:
            lines.append(f"{_line(item.get('address', '?'))}  {_line(item.get('bytes', ''))}")
    if value.get("more"):
        lines.append(f"… more matches; rerun with --limit above {len(items)}")
    return "\n".join(lines)


def inspect_text(value: dict[str, Any]) -> str:
    if value.get("type_target"):
        return "\n".join(_type_lines(value["type_info"]))
    function = value.get("function")
    variable = value.get("variable")
    if value.get("variable_target") and isinstance(variable, dict):
        function_name = _line(function.get("name", "?")) if isinstance(function, dict) else "?"
        rows = [
            ("variable", f"{function_name}::{_line(variable.get('name', '?'))}"),
            ("function", f"{function_name} @ {_line(function.get('address', '?'))}"),
            ("type", _type_summary(variable["type"])),
            ("parameter", "yes" if variable.get("parameter") else "no"),
            ("exact", f"{function_name}::{_line(variable.get('target', '?'))}"),
        ]
        if isinstance(function, dict) and function.get("skip_reason"):
            rows.append(("analysis", f"skipped: {_line(function['skip_reason'])}"))
        return "\n".join([_rows(rows), *_type_lines(value.get("type_info"), embedded=True)])

    address = _line(value.get("address", "unknown"))
    rows = [
        ("address", address),
        ("sections", ", ".join(_string_list(value.get("sections"))) or "none"),
    ]
    segment = value.get("segment")
    if isinstance(segment, dict):
        rows.append(("segment", _segment_line(segment)))
    else:
        rows.append(("segment", "none"))
    symbol = value.get("symbol")
    if isinstance(symbol, dict):
        rows.append(("symbol", f"{_line(symbol.get('name', '?'))} ({_line(symbol.get('type', '?'))})"))
    if isinstance(function, dict):
        rows.extend(
            [
                ("function", f"{_line(function.get('name', '?'))} @ {_line(function.get('address', '?'))}"),
                ("signature", _line(function.get("type", ""))),
            ]
        )
        if function.get("skip_reason"):
            rows.append(("analysis", f"skipped: {_line(function['skip_reason'])}"))
    functions = value.get("functions")
    if isinstance(functions, list) and functions:
        names = ", ".join(
            f"{_line(item.get('name', '?'))} @ {_line(item.get('address', '?'))}"
            for item in functions if isinstance(item, dict)
        )
        rows.append(("functions", names))
    block = value.get("block")
    if isinstance(block, dict):
        rows.append(("block", f"{_line(block.get('start', '?'))}..{_line(block.get('end', '?'))}"))
    instruction = value.get("instruction")
    if instruction:
        instruction_address = _line(value.get("instruction_address") or address)
        rows.append(
            (
                "instruction",
                f"{_anchor(instruction_address, address)}  "
                f"{_line(value.get('bytes') or '')}  {_line(instruction)}".strip(),
            )
        )
    string = value.get("string")
    if isinstance(string, dict):
        rows.append(
            (
                "string",
                f"{_anchor(_line(string.get('address', '?')), address)}  "
                f"{_line(string.get('type', '?'))}, {string.get('length', '?')} bytes, "
                f"{string.get('refs', '?')} refs: {_line(string.get('value', ''))}",
            )
        )
    data = value.get("data")
    if isinstance(data, dict):
        detail = (
            f"{_anchor(_line(data.get('address', '?')), address)}  "
            f"{_type_summary(data['type'])}"
        )
        if data.get("value") is not None:
            detail += f" = {_line(data['value'])}"
        rows.append(("data", detail))
    if value.get("function_comment"):
        rows.append(("func comment", _line(value["function_comment"])))
    if value.get("view_comment"):
        rows.append(("view comment", _line(value["view_comment"])))
    lines = [_rows(rows)]
    lines.extend(_type_lines(value.get("type_info"), embedded=True))
    parameters = value.get("parameters")
    variables = value.get("variables")
    if isinstance(parameters, list) and parameters and not isinstance(variables, list):
        function_name = function.get("name", "?") if isinstance(function, dict) else "?"
        lines.append("parameters")
        lines.extend(
            f"  {_line(function_name)}::{_line(item.get('name', '?'))}  "
            f"{_type_summary(item['type'])}"
            for item in parameters if isinstance(item, dict)
        )
    if isinstance(value.get("local_count"), int):
        hint = "  (use --vars to list)" if not isinstance(variables, list) else ""
        lines.append(f"locals  {value['local_count']}{hint}")
    if isinstance(variables, list) and variables:
        lines.append("variables")
        function_name = function.get("name", "?") if isinstance(function, dict) else "?"
        for variable in variables:
            if not isinstance(variable, dict):
                continue
            identity = variable.get("name") or variable.get("target")
            target = f"{function_name}::{identity}"
            suffix = "  parameter" if variable.get("parameter") else ""
            if variable.get("ambiguous"):
                suffix += f"  [{function_name}::{variable.get('target', '?')}]"
            lines.append(f"  {_line(target)}  {_type_summary(variable['type'])}{_line(suffix)}")
        if value.get("variables_more"):
            lines.append(
                f"  … {value['variables_more']} more; rerun with --limit above {len(variables)}"
            )
    return "\n".join(lines)


def _type_target(target: str) -> str:
    return shlex.quote(target if target.isprintable() else _line(target))


def _type_summary(info: dict[str, Any]) -> str:
    text = _line(info["text"])
    if info.get("target"):
        text += f"  [{_type_target(info['target'])}]"
    related = info.get("pointee") or info.get("element")
    if related and related.get("target"):
        text += f"  -> {_type_target(related['target'])}"
    return text


def _type_base(member: dict[str, Any]) -> str:
    base = member.get("base")
    if base is None:
        return ""
    label = _type_target(base["target"]) if base.get("target") else _line(base["text"])
    return f"  [base {label} +{hex(base['offset'])}]"


def _type_offset(member: dict[str, Any]) -> str:
    offset = hex(member["offset"])
    if member["bits"]:
        offset += f" bit {member['bit_position']}..{member['bit_position'] + member['bits'] - 1}"
    return offset


def _byte_size(size: int) -> str:
    return f"{size} byte{'s' if size != 1 else ''}"


def _type_lines(info: dict[str, Any] | None, *, embedded: bool = False) -> list[str]:
    if info is None:
        return []
    if (
        embedded
        and not any(key in info for key in ("members", "values", "selected", "unresolved"))
        and "count" not in info["layout"]
    ):
        return []
    declared = info["type"]
    layout = info["layout"]
    rows = []
    if not embedded:
        rows.extend(
            [
                ("type", _line(info.get("name", declared["text"]))),
                ("kind", _line(declared["kind"])),
                ("size", _byte_size(declared["size"])),
                ("alignment", str(declared["alignment"])),
            ]
        )
        if info.get("target"):
            rows.append(("target", _type_target(info["target"])))
        if info.get("exact") and info["exact"] != info.get("target"):
            rows.append(("exact", _type_target(info["exact"])))
    for step in info["steps"]:
        rows.append(
            (
                "field",
                (f"{_line(step['parent'])}.{_line(step['name'])} "
                 f"+{_type_offset(step)}  {_type_summary(step['type'])}{_type_base(step)}"),
            )
        )
    if info.get("selected"):
        selected = info["selected"]
        rows.append(("selected", f"{_type_summary(selected)} ({_byte_size(selected['size'])})"))
    if embedded or info.get("aliases") or "pointer_size" in info:
        rows.append(
            (
                "layout",
                f"{_type_summary(layout)} ({_byte_size(layout['size'])}, alignment {layout['alignment']})",
            )
        )
        if "pointer_size" in info:
            rows.append(("pointer", _byte_size(info["pointer_size"])))
    if info.get("unresolved"):
        rows.append(("status", _line(info["unresolved"])))
    lines = [_rows(rows)] if rows else []
    members = info.get("members", [])
    if members:
        lines.append(info.get("variant", "struct") + " members (offset, size, name, type)")
        for member in members:
            offset = _type_offset(member)
            size = (
                f"{member['bits']} bit{'s' if member['bits'] != 1 else ''}"
                if member["bits"]
                else _byte_size(member["type"]["size"])
            )
            lines.append(
                f"  {offset:<16} {size:<9} {_line(member['name'])}  "
                f"{_type_summary(member['type'])}{_type_base(member)}"
            )
    values = info.get("values", [])
    if values:
        lines.append("enum values")
        lines.extend(f"  {_line(v['name'])} = {v['value']} ({hex(v['value'])})" for v in values)
    if "count" in layout:
        lines.append(f"elements  {layout['count']}  {_type_summary(layout['element'])}")
    if info.get("more"):
        lines.append(f"… more entries; rerun with --limit above {len(members or values)}")
    return lines


def read_text(value: dict[str, Any]) -> str:
    address = int(value["address"], 16)
    width = value["address_size"] * 2
    data = bytes.fromhex(value["bytes"])
    lines = []
    for offset in range(0, len(data), 16):
        chunk = data[offset:offset + 16]
        ascii_text = "".join(chr(byte) if 32 <= byte < 127 else "." for byte in chunk)
        lines.append(f"0x{address + offset:0{width}x}  {chunk.hex(' '):<47}  |{ascii_text}|")
    if len(data) < value["length"]:
        lines.append(f"read {len(data)} of {value['length']} bytes (stopped at {address + len(data):#x})")
    return "\n".join(lines)


def code_text(value: dict[str, Any]) -> str:
    level = _line(value.get("level", "code"))
    if value.get("ssa"):
        level += " ssa"
    header = f"{_line(value.get('function', '?'))} @ {_line(value.get('address', '?'))}  {level}"
    if value.get("at"):
        header += f" at {_line(value['at'])}"
        instruction_address = value.get("instruction_address")
        if isinstance(instruction_address, str) and instruction_address != value["at"]:
            header += f" (instruction {_anchor(instruction_address, value['at'])})"
    if value.get("skip_reason"):
        header += f"\nanalysis skipped: {_line(value['skip_reason'])}"
    raw_lines = value.get("lines")
    if not isinstance(raw_lines, list) or not raw_lines:
        return f"{header}\n(no matching lines)"
    lines = [header]
    related = False
    for item in raw_lines:
        if not isinstance(item, dict):
            continue
        if item.get("related") and not related:
            lines.append("related")
            related = True
        identity = str(item.get("index", ""))
        if "expression" in item:
            identity = f"{identity}:{item['expression']}"
        prefix = f"{_line(item.get('address', '?'))}"
        if identity:
            prefix += f"  {identity}"
        lines.append(_prefixed_text(prefix, str(item.get("text", ""))))
    if value.get("more"):
        lines.append(f"… more lines; rerun with --limit above {len(raw_lines)}")
    return "\n".join(lines)


def refs_text(value: dict[str, Any]) -> str:
    direction = "from" if value.get("direction") == "from" else "to"
    header = f"references {direction} {_line(value.get('target', value.get('address', '?')))}"
    entry_function = value.get("entry_function")
    if isinstance(entry_function, str):
        lines = [f"{header} ({_line(entry_function)} entry)", "at entry"]
        lines.extend(_reference_rows(value.get("site_items"), value.get("site_more")))
        lines.append(f"from {_line(entry_function)} (whole function)")
        lines.extend(_reference_rows(value.get("items"), value.get("more")))
        return "\n".join(lines)
    if value.get("function_scope"):
        header += " (whole function)"
    site_address = value.get("site_address")
    if isinstance(site_address, str):
        context = value.get("site_function")
        if site_address != value.get("address"):
            header += f" (instruction {_anchor(site_address, value['address'])}"
            if context:
                header += f" in {_line(context)}"
            header += ")"
        elif context:
            header += f" (in {_line(context)})"
    lines = [header, *_reference_rows(value.get("items"), value.get("more"))]
    anchor_address = value.get("anchor_address")
    if isinstance(anchor_address, str):
        kind = _line(value.get("anchor_kind", "object"))
        lines.append(f"containing {kind} at {_anchor(anchor_address, value['address'])}")
        lines.extend(_reference_rows(value.get("anchor_items"), value.get("anchor_more")))
    return "\n".join(lines)


def sections_text(value: dict[str, Any]) -> str:
    items = value.get("items")
    if not isinstance(items, list) or not items:
        return "no sections"
    lines = [
        f"{_line(item.get('start', '?'))}..{_line(item.get('end', '?'))}  "
        f"{item.get('length', '?')} bytes  {_section_semantics(item.get('semantics'))}  "
        f"{_line(item.get('name', '?'))}"
        for item in items
        if isinstance(item, dict)
    ]
    if value.get("more"):
        lines.append(f"… more sections; rerun with --limit above {len(items)}")
    return "\n".join(lines)


def segments_text(value: dict[str, Any]) -> str:
    items = value.get("items")
    if not isinstance(items, list) or not items:
        return "no segments"
    lines = [_segment_line(item) for item in items if isinstance(item, dict)]
    if value.get("more"):
        lines.append(f"… more segments; rerun with --limit above {len(items)}")
    return "\n".join(lines)


def edit_text(value: dict[str, Any]) -> str:
    lines = [
        f"edited {_line(value.get('kind', 'target'))} {_line(value.get('target', '?'))} "
        f"@ {_line(value.get('address', '?'))}"
    ]
    changes = value.get("changes")
    if isinstance(changes, list):
        for change in changes:
            if not isinstance(change, dict):
                continue
            field = _line(change.get("field", "change"))
            if change.get("scope"):
                field += f" ({_line(change['scope'])})"
            lines.append(f"{field}\n  before  {_line(change.get('before', ''))}\n  after   {_line(change.get('after', ''))}")
    return "\n".join(lines)


def patch_text(value: dict[str, Any]) -> str:
    rows = [
        ("address", _line(value.get("address", "?"))),
        ("bytes before", _line(value.get("old", ""))),
        ("bytes after", _line(value.get("new", ""))),
    ]
    if value.get("before") is not None or value.get("after") is not None:
        rows.extend(
            [
                ("code before", _optional(value.get("before"))),
                ("code after", _optional(value.get("after"))),
            ]
        )
    return _rows(rows)


def save_text(value: dict[str, Any], *, verb: str = "saved") -> str:
    suffix = f"\nbytes  {value['bytes']}" if "bytes" in value else ""
    return f"{verb} {_line(value.get('session', '?'))}\npath  {_line(value.get('path', '?'))}{suffix}"


def python_text(value: dict[str, Any]) -> str:
    output = value.get("output")
    text = output if isinstance(output, str) else ""
    if value.get("has_result"):
        result = f"result  {_line(value.get('result', ''))}"
        if text and not text.endswith("\n"):
            text += "\n"
        text += result
    return text.rstrip("\n")


def error_text(message: str, *, kind: str, details: dict[str, Any]) -> str:
    lines = [f"error: {_line(message)}"]
    candidates = _string_list(details.get("candidates"))
    if candidates:
        label = "sessions" if kind.startswith("session_") else "candidates"
        rendered = (_type_target(item) if item.startswith("type:") else _line(item) for item in candidates)
        lines.append(f"{label}: {', '.join(rendered)}")
    openings = _string_list(details.get("openings"))
    if openings:
        lines.append(f"opening: {', '.join(_line(item) for item in openings)}")
    output = details.get("output")
    if isinstance(output, str) and output:
        lines.append("output:\n" + output.rstrip("\n"))
    trace = details.get("traceback")
    if isinstance(trace, str) and trace:
        lines.append(trace.rstrip("\n"))
    return "\n".join(lines)


def _anchor(base: str, requested: str) -> str:
    try:
        offset = int(requested, 0) - int(base, 0)
    except ValueError:
        return base
    return f"{base} +{offset}" if offset > 0 else base


def _reference_rows(items: Any, more: Any) -> list[str]:
    if not isinstance(items, list) or not items:
        return ["none"]
    lines = [_reference_line(item) for item in items if isinstance(item, dict)]
    if more:
        lines.append(f"… more results; rerun with --limit above {len(items)}")
    return lines


def _reference_line(value: dict[str, Any]) -> str:
    kind = _line(value.get("kind", "ref"))
    site = _line(value.get("site", "?"))
    target = _line(value.get("target", "?"))
    function = value.get("function")
    context = f"  {_line(function)}" if function else ""
    return f"{kind:<5}  {site} -> {target}{context}"


def _segment_line(value: dict[str, Any]) -> str:
    flags = "".join(
        (
            "r" if value.get("readable") else "-",
            "w" if value.get("writable") else "-",
            "x" if value.get("executable") else "-",
        )
    )
    file_length = value.get("file_length")
    mapping = (
        "no file data"
        if file_length == 0
        else f"file {_line(value.get('file_offset', '?'))}..{_line(value.get('file_end', '?'))} "
        f"({file_length if file_length is not None else '?'} bytes)"
    )
    return (
        f"{_line(value.get('start', '?'))}..{_line(value.get('end', '?'))}  "
        f"{value.get('length', '?')} bytes  {flags}  {mapping}"
    )


def _section_semantics(value: Any) -> str:
    names = {
        "DefaultSectionSemantics": "default",
        "ReadOnlyCodeSectionSemantics": "read-only code",
        "ReadOnlyDataSectionSemantics": "read-only data",
        "ReadWriteDataSectionSemantics": "read/write data",
        "ExternalSectionSemantics": "external",
    }
    text = str(value)
    return names.get(text, _line(text))


def _prefixed_text(prefix: str, value: str) -> str:
    parts = value.splitlines() or [""]
    indent = " " * (len(prefix) + 2)
    return f"{prefix}  {parts[0]}" + "".join(f"\n{indent}{part}" for part in parts[1:])


def _rows(rows: list[tuple[str, str]]) -> str:
    width = max(len(label) for label, _ in rows)
    return "\n".join(f"{label:<{width}}  {item}" for label, item in rows)


def _optional(value: Any) -> str:
    return "unknown" if value is None else _line(value)


def _seconds(value: Any) -> str:
    return f"{value:.3f}s" if isinstance(value, (int, float)) else "unknown"


def _dirty(value: dict[str, Any]) -> str:
    changes = []
    if value.get("analysis_changed"):
        changes.append("analysis")
    if value.get("modified"):
        changes.append("bytes")
    return ", ".join(changes) if changes else "no"


def _string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    return [item for item in value if isinstance(item, str)]


def _line(value: Any) -> str:
    rendered = []
    for character in str(value):
        codepoint = ord(character)
        if character == "\\":
            rendered.append("\\\\")
        elif character == "\n":
            rendered.append("\\n")
        elif character == "\r":
            rendered.append("\\r")
        elif character == "\t":
            rendered.append("\\t")
        elif character.isprintable():
            rendered.append(character)
        elif codepoint <= 0xFF:
            rendered.append(f"\\x{codepoint:02x}")
        elif codepoint <= 0xFFFF:
            rendered.append(f"\\u{codepoint:04x}")
        else:
            rendered.append(f"\\U{codepoint:08x}")
    return "".join(rendered)
