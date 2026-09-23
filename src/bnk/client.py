from __future__ import annotations

import socket
from typing import Any

from bnk.endpoint import Endpoint
from bnk.protocol import API_VERSION, ProtocolError, read_message, write_message


class BnkError(Exception):
    def __init__(self, message: str, *, kind: str = "error", details: dict[str, Any] | None = None):
        super().__init__(message)
        self.kind = kind
        self.details = details or {}


def request(
    endpoint: Endpoint,
    action: str,
    args: dict[str, Any] | None = None,
    *,
    session: str | None = None,
    connect_timeout: float = 2.0,
) -> Any:
    message = {
        "api": API_VERSION,
        "action": action,
        "args": args or {},
    }
    if session is not None:
        message["session"] = session

    try:
        connection = socket.create_connection(
            (endpoint.host, endpoint.port),
            timeout=connect_timeout,
        )
    except OSError as error:
        raise BnkError(
            f"cannot connect to bnk at {endpoint}",
            kind="connection",
        ) from error

    try:
        connection.settimeout(None)
        with connection, connection.makefile("rwb") as stream:
            write_message(stream, message)
            result = read_message(stream)
            if result.get("ok") is False:
                _raise_remote(result.get("error"))
            if result.get("ok") is not True:
                raise ProtocolError("server result has no valid status")
            return result.get("value")
    except ProtocolError as error:
        raise BnkError(str(error), kind="protocol") from error
    except OSError as error:
        raise BnkError(
            f"connection to bnk at {endpoint} was lost",
            kind="connection",
        ) from error


def _raise_remote(value: object) -> None:
    if isinstance(value, dict):
        message = value.get("message")
        kind = value.get("kind")
        if isinstance(message, str):
            raise BnkError(
                message,
                kind=kind if isinstance(kind, str) else "server",
                details={
                    key: item
                    for key, item in value.items()
                    if key not in {"message", "kind"}
                },
            )
    raise BnkError("bnk server returned an invalid error", kind="protocol")
