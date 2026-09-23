from __future__ import annotations

import json
from collections.abc import Mapping
from typing import Any, BinaryIO


API_VERSION = 1


class ProtocolError(Exception):
    pass


def write_message(stream: BinaryIO, message: Mapping[str, Any]) -> None:
    payload = json.dumps(
        message,
        ensure_ascii=False,
        separators=(",", ":"),
    ).encode("utf-8")
    stream.write(payload + b"\n")
    stream.flush()


def read_message(stream: BinaryIO) -> dict[str, Any]:
    line = stream.readline()
    if not line:
        raise ProtocolError("connection closed before the final result")
    try:
        value = json.loads(line.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise ProtocolError("server sent invalid JSON") from error
    if not isinstance(value, dict):
        raise ProtocolError("server message must be a JSON object")
    return value
