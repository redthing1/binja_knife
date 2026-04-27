from __future__ import annotations

import json
from dataclasses import dataclass
from typing import Any, Iterable, Optional


_TABLE_CELL_MAX = 120

_HEX_FIELD_PAIRS = [
    ("address", "address_hex"),
    ("start", "start_hex"),
    ("end", "end_hex"),
    ("data_offset", "data_offset_hex"),
    ("data_end", "data_end_hex"),
]

_PREFERRED_COLUMNS = [
    "index",
    "id",
    "name",
    "mode",
    "target",
    "busy",
    "filename",
    "address_hex",
    "address",
    "start_hex",
    "start",
    "end_hex",
    "end",
    "length_hex",
    "length",
    "data_offset_hex",
    "data_offset",
    "data_end_hex",
    "data_end",
    "data_length_hex",
    "data_length",
    "type",
    "arch",
    "view_type",
    "analysis_state",
    "il",
    "ref_type",
    "function",
]


@dataclass(frozen=True)
class _Listing:
    header: str
    records: list[Any]


def dump_json(value: Any, *, pretty: bool) -> str:
    data = _jsonable(value)
    if pretty:
        return json.dumps(data, indent=2, sort_keys=False)
    return json.dumps(data, separators=(",", ":"), sort_keys=False)


def format_text(value: Any) -> str:
    renderer = _TextRenderer()
    renderer.render(value)
    return renderer.text()


def _jsonable(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, list):
        return [_jsonable(v) for v in value]
    if isinstance(value, dict):
        return {str(k): _jsonable(v) for k, v in value.items()}

    try:
        json.dumps(value)
        return value
    except TypeError:
        return {"type": type(value).__name__, "repr": repr(value)}


def _is_scalar(value: Any) -> bool:
    return value is None or isinstance(value, (bool, int, float, str))


def _to_text(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _is_run_result(value: dict[str, Any]) -> bool:
    return "ok" in value and "stdout" in value and "stderr" in value


def _listing_from_mapping(value: dict[str, Any]) -> Optional[_Listing]:
    records = value.get("lines")
    if not isinstance(records, list):
        return None

    if {"function", "address_hex", "il", "count"}.issubset(value.keys()):
        return _Listing(header=_il_header(value), records=records)

    return None


def _is_il_text(value: dict[str, Any]) -> bool:
    return {"function", "address_hex", "il", "line_count", "text"}.issubset(
        value.keys()
    ) and isinstance(value.get("text"), str)


def _il_header(value: dict[str, Any]) -> str:
    header = (
        f"{value.get('il', 'il')} {value.get('function', '')} "
        f"@ {value.get('address_hex', '')}"
    ).strip()
    count = value.get("line_count", value.get("count"))
    if isinstance(count, int):
        suffix = f"{count} lines"
        if value.get("truncated"):
            suffix += ", truncated"
        header = f"{header} ({suffix})"
    return header


def _ordered_columns(records: list[dict[str, Any]]) -> list[str]:
    cols: list[str] = []
    seen: set[str] = set()

    for rec in records:
        for key in rec.keys():
            name = str(key)
            if name in seen:
                continue
            seen.add(name)
            cols.append(name)

    cols = _drop_redundant_fields(cols)
    preferred = [col for col in _PREFERRED_COLUMNS if col in cols]
    rest = [col for col in cols if col not in preferred]
    return preferred + rest


def _drop_redundant_fields(fields: list[str]) -> list[str]:
    field_set = set(fields)
    drop = {
        base
        for base, hex_field in _HEX_FIELD_PAIRS
        if base in field_set and hex_field in field_set
    }
    if "idx" in field_set:
        drop.add("idx")

    if not drop:
        return fields
    return [field for field in fields if field not in drop]


def _table_lines(records: list[dict[str, Any]]) -> Optional[list[str]]:
    if not records:
        return None

    cols = _ordered_columns(records)
    if not cols:
        return None

    rows: list[list[str]] = []
    widths: dict[str, int] = {col: len(col) for col in cols}
    align_right: dict[str, bool] = {col: True for col in cols}

    for rec in records:
        row: list[str] = []
        for col in cols:
            value = rec.get(col, "")
            text = _table_cell_text(value)
            if text is None:
                return None

            if value is not None and not isinstance(value, (int, float)):
                align_right[col] = False

            widths[col] = max(widths[col], len(text))
            row.append(text)
        rows.append(row)

    return _render_table(cols, rows, widths=widths, align_right=align_right)


def _table_cell_text(value: Any) -> Optional[str]:
    if not _is_scalar(value):
        return None
    text = _escape_table_text(_to_text(value))
    if len(text) > _TABLE_CELL_MAX:
        return f"{text[: _TABLE_CELL_MAX - 3]}..."
    return text


def _escape_table_text(text: str) -> str:
    out: list[str] = []
    for char in text:
        code = ord(char)
        if char == "\\":
            out.append("\\\\")
        elif char == "\n":
            out.append("\\n")
        elif char == "\r":
            out.append("\\r")
        elif char == "\t":
            out.append("\\t")
        elif code < 0x20 or code == 0x7F:
            out.append(f"\\x{code:02x}")
        else:
            out.append(char)
    return "".join(out)


def _render_table(
    cols: list[str],
    rows: list[list[str]],
    *,
    widths: dict[str, int],
    align_right: dict[str, bool],
) -> list[str]:
    def render_row(values: Iterable[str]) -> str:
        parts: list[str] = []
        for col, cell in zip(cols, values):
            width = widths[col]
            if align_right.get(col, False):
                parts.append(cell.rjust(width))
            else:
                parts.append(cell.ljust(width))
        return "  ".join(parts).rstrip()

    out = [render_row(cols), render_row(["-" * widths[col] for col in cols])]
    out.extend(render_row(row) for row in rows)
    return out


class _TextRenderer:
    def __init__(self) -> None:
        self._lines: list[str] = []

    def text(self) -> str:
        return "\n".join(self._lines).rstrip("\n")

    def render(self, value: Any, *, indent: int = 0) -> None:
        if isinstance(value, dict):
            self._mapping(value, indent=indent)
            return

        if isinstance(value, list):
            self._sequence(value, indent=indent)
            return

        if _is_scalar(value):
            self._emit(indent, _to_text(value))
            return

        self._emit(indent, repr(value))

    def _mapping(self, value: dict[str, Any], *, indent: int) -> None:
        if _is_run_result(value):
            self._run_result(value, indent=indent)
            return

        if _is_il_text(value):
            self._il_text(value, indent=indent)
            return

        listing = _listing_from_mapping(value)
        if listing is not None:
            self._listing(listing, indent=indent)
            return

        if not value:
            self._emit(indent, "{}")
            return

        self._plain_mapping(value, indent=indent)

    def _run_result(self, value: dict[str, Any], *, indent: int) -> None:
        ok = bool(value.get("ok", False))
        stdout = str(value.get("stdout", ""))
        stderr = str(value.get("stderr", ""))
        has_exit_code = "exit_code" in value
        exit_code = value.get("exit_code") if has_exit_code else None
        has_result = "result" in value
        result = value.get("result", None)

        if ok and not stdout and not stderr and not has_exit_code and has_result:
            self.render(result, indent=indent)
            return

        self._emit(indent, f"ok: {'true' if ok else 'false'}")
        self._block("stdout", stdout, indent=indent)
        self._block("stderr", stderr, indent=indent)
        if not ok:
            self._block("error", str(value.get("error", "")), indent=indent)
        if exit_code is not None:
            self._emit(indent, f"exit_code: {_to_text(exit_code)}")
        if has_result:
            self._emit(indent, "result:")
            self.render(result, indent=indent + 2)

    def _listing(self, listing: _Listing, *, indent: int) -> None:
        self._emit(indent, listing.header)
        for record in listing.records:
            self._listing_record(record, indent=indent + 2)

    def _il_text(self, value: dict[str, Any], *, indent: int) -> None:
        self._emit(indent, _il_header(value))
        text = str(value.get("text", ""))
        if text:
            self._block_lines(text, indent=indent)

    def _listing_record(self, record: Any, *, indent: int) -> None:
        if not isinstance(record, dict):
            self._emit(indent, _to_text(record))
            return

        idx = str(record.get("idx", "")).rjust(4)
        addr = record.get("address_hex", "")
        text = _to_text(record.get("text", ""))
        prefix = f"{idx}  {addr}" if addr else idx
        self._emit(indent, f"{prefix}  {text}".rstrip())

    def _plain_mapping(self, value: dict[str, Any], *, indent: int) -> None:
        items = _visible_items(value)
        key_pad = max((len(str(key)) for key, _value in items), default=0)

        for key, item in items:
            name = str(key)
            if isinstance(item, str) and _is_multiline(item):
                self._emit(indent, f"{name.ljust(key_pad)}:")
                self._block_lines(item, indent=indent + 2)
                continue

            if _is_scalar(item):
                self._emit(indent, f"{name.ljust(key_pad)}: {_to_text(item)}")
                continue

            self._emit(indent, f"{name.ljust(key_pad)}:")
            self.render(item, indent=indent + 2)

    def _sequence(self, value: list[Any], *, indent: int) -> None:
        if not value:
            self._emit(indent, "[]")
            return

        if all(isinstance(item, dict) for item in value):
            table = _table_lines([item for item in value if isinstance(item, dict)])
            if table is not None:
                self._lines.extend(f"{self._pad(indent)}{line}" for line in table)
                return

        for idx, item in enumerate(value):
            if isinstance(item, str) and _is_multiline(item):
                self._emit(indent, f"[{idx}]")
                self._block_lines(item, indent=indent + 2)
                continue

            if _is_scalar(item):
                self._emit(indent, f"[{idx}] {_to_text(item)}")
                continue

            self._emit(indent, f"[{idx}]")
            self.render(item, indent=indent + 2)

    def _block(self, header: str, text: str, *, indent: int) -> None:
        if not text:
            return
        self._emit(indent, f"{header}:")
        self._block_lines(text, indent=indent + 2)

    def _block_lines(self, text: str, *, indent: int) -> None:
        for line in text.rstrip("\n").splitlines():
            self._emit(indent, line)

    def _emit(self, indent: int, text: str) -> None:
        self._lines.append(f"{self._pad(indent)}{text}")

    @staticmethod
    def _pad(indent: int) -> str:
        return " " * indent


def _visible_items(value: dict[str, Any]) -> list[tuple[Any, Any]]:
    items = list(value.items())
    keys = [str(key) for key, _item in items]
    keep_keys = _drop_redundant_fields(keys)
    if keep_keys == keys:
        return items

    keep = set(keep_keys)
    return [(key, item) for key, item in items if str(key) in keep]


def _is_multiline(value: str) -> bool:
    return "\n" in value or "\r" in value
