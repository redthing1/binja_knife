from __future__ import annotations

from dataclasses import dataclass


DEFAULT_CONNECT = "127.0.0.1:18812"


class EndpointError(ValueError):
    pass


@dataclass(frozen=True)
class Endpoint:
    host: str
    port: int

    @classmethod
    def parse(cls, value: str) -> Endpoint:
        text = value.strip()
        if not text:
            raise EndpointError("connection endpoint is empty")

        if text.startswith("["):
            closing = text.find("]")
            if closing < 0 or text[closing + 1 : closing + 2] != ":":
                raise EndpointError("IPv6 endpoints use [HOST]:PORT")
            host = text[1:closing]
            port_text = text[closing + 2 :]
        else:
            host, separator, port_text = text.rpartition(":")
            if not separator:
                raise EndpointError("connection endpoint must be HOST:PORT")
            if ":" in host:
                raise EndpointError("IPv6 endpoints use [HOST]:PORT")

        if not host:
            raise EndpointError("connection endpoint has no host")
        try:
            port = int(port_text, 10)
        except ValueError as error:
            raise EndpointError("connection endpoint has an invalid port") from error
        if not 1 <= port <= 65535:
            raise EndpointError("connection port must be between 1 and 65535")
        return cls(host, port)

    def __str__(self) -> str:
        host = f"[{self.host}]" if ":" in self.host else self.host
        return f"{host}:{self.port}"
