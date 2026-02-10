from __future__ import annotations


def parse_endpoint(text: str) -> tuple[str, int]:
    raw = (text or "").strip()
    if raw.startswith("tcp://"):
        raw = raw[len("tcp://") :]
    if ":" not in raw:
        raise ValueError("expected HOST:PORT")
    host, port_text = raw.rsplit(":", 1)
    host = host.strip()
    if not host:
        raise ValueError("host is empty")
    try:
        port = int(port_text)
    except Exception as exc:
        raise ValueError(f"invalid port in endpoint: {text!r}") from exc
    return host, port
