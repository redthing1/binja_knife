from __future__ import annotations

import json
from typing import Any, Iterable, Optional


def _jsonable(value: Any) -> Any:
    if value is None:
        return None
    if isinstance(value, (bool, int, float, str)):
        return value
    if isinstance(value, list):
        return [_jsonable(v) for v in value]
    if isinstance(value, dict):
        out = {}
        for k, v in value.items():
            out[str(k)] = _jsonable(v)
        return out

    try:
        json.dumps(value)
        return value
    except TypeError:
        return {"type": type(value).__name__, "repr": repr(value)}


def dump_json(value: Any, *, pretty: bool) -> str:
    data = _jsonable(value)
    if pretty:
        return json.dumps(data, indent=2, sort_keys=False)
    return json.dumps(data, separators=(",", ":"), sort_keys=False)


def _is_scalar(value: Any) -> bool:
    return value is None or isinstance(value, (bool, int, float, str))


def _to_text(value: Any) -> str:
    if value is None:
        return "null"
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def _is_run_result(d: dict[str, Any]) -> bool:
    return "ok" in d and "stdout" in d and "stderr" in d


def _format_block(lines: list[str], header: str, text: str, *, indent: int) -> None:
    if not text:
        return
    pad = " " * indent
    lines.append(f"{pad}{header}:")
    for line in text.rstrip("\n").splitlines():
        lines.append(f"{pad}  {line}")


def _preferred_columns(cols: list[str]) -> list[str]:
    preferred = [
        "index",
        "name",
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
    pref = [c for c in preferred if c in cols]
    rest = [c for c in cols if c not in pref]
    return pref + rest


def _table(records: list[dict[str, Any]]) -> Optional[str]:
    if not records:
        return None

    cols: list[str] = []
    seen: set[str] = set()
    for rec in records:
        for k in rec.keys():
            key = str(k)
            if key in seen:
                continue
            seen.add(key)
            cols.append(key)

    cols = _preferred_columns(cols)

    rows: list[list[str]] = []
    widths: dict[str, int] = {c: len(c) for c in cols}
    align_right: dict[str, bool] = {c: True for c in cols}

    for rec in records:
        row: list[str] = []
        for c in cols:
            v = rec.get(c, "")
            if not _is_scalar(v):
                return None
            s = _to_text(v)
            if "\n" in s:
                return None
            if len(s) > 120:
                return None

            if v is not None and not isinstance(v, (int, float)):
                align_right[c] = False

            widths[c] = max(widths[c], len(s))
            row.append(s)
        rows.append(row)

    if not cols:
        return None

    def render_row(values: Iterable[str]) -> str:
        parts: list[str] = []
        for c, cell in zip(cols, values):
            w = widths[c]
            if align_right.get(c, False):
                parts.append(cell.rjust(w))
            else:
                parts.append(cell.ljust(w))
        return "  ".join(parts).rstrip()

    out_lines = [render_row(cols), render_row(["-" * widths[c] for c in cols])]
    for row in rows:
        out_lines.append(render_row(row))
    return "\n".join(out_lines)


def format_text(value: Any) -> str:
    lines: list[str] = []
    _format_any(lines, value, indent=0)
    return "\n".join(lines).rstrip("\n")


def _format_any(lines: list[str], value: Any, *, indent: int) -> None:
    pad = " " * indent

    if isinstance(value, dict):
        if _is_run_result(value):
            ok = bool(value.get("ok", False))
            stdout = str(value.get("stdout", ""))
            stderr = str(value.get("stderr", ""))
            has_exit_code = "exit_code" in value
            exit_code = value.get("exit_code") if has_exit_code else None
            has_result = "result" in value
            result = value.get("result", None)

            # common happy-path output: return only the result
            if ok and not stdout and not stderr and not has_exit_code and has_result:
                _format_any(lines, result, indent=indent)
                return

            lines.append(f"{pad}ok: {'true' if ok else 'false'}")
            _format_block(lines, "stdout", stdout, indent=indent)
            _format_block(lines, "stderr", stderr, indent=indent)
            if not ok:
                _format_block(
                    lines, "error", str(value.get("error", "")), indent=indent
                )
            if exit_code is not None:
                lines.append(f"{pad}exit_code: {_to_text(exit_code)}")
            if has_result:
                lines.append(f"{pad}result:")
                _format_any(lines, result, indent=indent + 2)
            return

        if not value:
            lines.append(f"{pad}{{}}")
            return

        keys = [str(k) for k in value.keys()]
        key_pad = max((len(k) for k in keys), default=0)
        for k, v in value.items():
            ks = str(k)
            if isinstance(v, str) and ("\n" in v or "\r" in v):
                lines.append(f"{pad}{ks.ljust(key_pad)}:")
                pad2 = " " * (indent + 2)
                for line in v.rstrip("\n").splitlines():
                    lines.append(f"{pad2}{line}")
                continue
            if _is_scalar(v):
                lines.append(f"{pad}{ks.ljust(key_pad)}: {_to_text(v)}")
                continue
            lines.append(f"{pad}{ks.ljust(key_pad)}:")
            _format_any(lines, v, indent=indent + 2)
        return

    if isinstance(value, list):
        if not value:
            lines.append(f"{pad}[]")
            return

        if all(isinstance(v, dict) for v in value):
            tbl = _table([v for v in value if isinstance(v, dict)])
            if tbl is not None:
                for line in tbl.splitlines():
                    lines.append(f"{pad}{line}")
                return

        for idx, item in enumerate(value):
            if isinstance(item, str) and ("\n" in item or "\r" in item):
                lines.append(f"{pad}[{idx}]")
                pad2 = " " * (indent + 2)
                for line in item.rstrip("\n").splitlines():
                    lines.append(f"{pad2}{line}")
                continue
            if _is_scalar(item):
                lines.append(f"{pad}[{idx}] {_to_text(item)}")
                continue
            lines.append(f"{pad}[{idx}]")
            _format_any(lines, item, indent=indent + 2)
        return

    if _is_scalar(value):
        lines.append(f"{pad}{_to_text(value)}")
        return

    lines.append(f"{pad}{repr(value)}")
