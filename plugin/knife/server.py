from __future__ import annotations

import json
import socket
import socketserver
import time
import traceback
from collections.abc import Callable, Mapping
from typing import Any, BinaryIO

from . import __version__
from .sessions import SessionError

API_VERSION = 1

VersionProvider = Callable[[], str]
LogError = Callable[[str], None]
Action = Callable[[str | None, dict[str, Any]], Any]


class RequestError(Exception):
    def __init__(
        self,
        message: str,
        *,
        kind: str = "invalid_request",
        details: dict[str, Any] | None = None,
    ) -> None:
        super().__init__(message)
        self.kind = kind
        self.details = details or {}


class KnifeServer(socketserver.ThreadingTCPServer):
    allow_reuse_address = True
    daemon_threads = True

    def __init__(
        self,
        address: tuple[str, int],
        *,
        binary_ninja_version: VersionProvider,
        log_error: LogError,
        actions: Mapping[str, Action] | None = None,
    ) -> None:
        if ":" in address[0]:
            self.address_family = socket.AF_INET6
        self.binary_ninja_version = binary_ninja_version
        self.log_error = log_error
        self.actions = dict(actions or {})
        self.started_at = time.monotonic()
        super().__init__(address, RequestHandler)

    def status(self, client_api: object) -> dict[str, Any]:
        host, port = self.server_address[:2]
        return {
            "api": API_VERSION,
            "server_version": __version__,
            "compatible": _plain_integer(client_api) and client_api == API_VERSION,
            "binary_ninja_version": self.binary_ninja_version(),
            "uptime_seconds": round(time.monotonic() - self.started_at, 3),
            "listen": {"host": host, "port": port},
        }


class RequestHandler(socketserver.StreamRequestHandler):
    server: KnifeServer

    def handle(self) -> None:
        try:
            request = _read_request(self.rfile)
            value = self._dispatch(request)
            result = {"ok": True, "value": value}
        except (RequestError, SessionError) as error:
            result = {
                "ok": False,
                "error": {"kind": error.kind, "message": str(error), **error.details},
            }
        except Exception as error:
            trace = traceback.format_exc()
            self.server.log_error(trace)
            result = {
                "ok": False,
                "error": {
                    "kind": "server",
                    "message": f"{type(error).__name__}: {error}",
                    "traceback": trace,
                },
            }
        self._write(result)

    def _dispatch(self, request: dict[str, Any]) -> Any:
        action = request.get("action")
        client_api = request.get("api")
        args = request.get("args")
        session = request.get("session")
        if not isinstance(action, str) or not action:
            raise RequestError("action must be a non-empty string")
        if not isinstance(args, dict):
            raise RequestError("args must be an object")
        if session is not None and (not isinstance(session, str) or not session):
            raise RequestError("session must be a non-empty string")
        if action == "status":
            return self.server.status(client_api)
        if not _plain_integer(client_api):
            raise RequestError("api must be an integer")
        if client_api != API_VERSION:
            raise RequestError(
                f"client api {client_api} is not compatible with server api {API_VERSION}",
                kind="incompatible_api",
            )
        handler = self.server.actions.get(action)
        if handler is None:
            raise RequestError(f"unknown action: {action}", kind="unknown_action")
        return handler(session, args)

    def _write(self, message: dict[str, Any]) -> None:
        data = json.dumps(message, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
        try:
            self.wfile.write(data + b"\n")
            self.wfile.flush()
        except OSError:
            pass


def _read_request(stream: BinaryIO) -> dict[str, Any]:
    line = stream.readline()
    if not line:
        raise RequestError("connection closed before a request was sent")
    try:
        value = json.loads(line)
    except (UnicodeDecodeError, json.JSONDecodeError) as error:
        raise RequestError("request is not valid JSON") from error
    if not isinstance(value, dict):
        raise RequestError("request must be a JSON object")
    return value


def _plain_integer(value: object) -> bool:
    return isinstance(value, int) and not isinstance(value, bool)
