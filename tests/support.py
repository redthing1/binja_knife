from __future__ import annotations

import threading
from collections.abc import Callable, Mapping
from contextlib import contextmanager
from typing import Any, Iterator

from knife.server import KnifeServer


@contextmanager
def running_server(
    binary_ninja_version: Callable[[], str] | None = None,
    *,
    actions: Mapping[str, Callable[[str | None, dict[str, Any]], Any]] | None = None,
) -> Iterator[tuple[KnifeServer, list[str]]]:
    errors: list[str] = []
    server = KnifeServer(
        ("127.0.0.1", 0),
        binary_ninja_version=binary_ninja_version or (lambda: "5.3.9757-dev"),
        log_error=errors.append,
        actions=actions,
    )
    thread = threading.Thread(target=server.serve_forever, daemon=True)
    thread.start()
    try:
        yield server, errors
    finally:
        server.shutdown()
        server.server_close()
        thread.join()
