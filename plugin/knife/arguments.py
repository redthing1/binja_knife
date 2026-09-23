from __future__ import annotations

from typing import Any

from .sessions import SessionError


def bounded(values: list[Any], limit: int) -> tuple[list[Any], bool]:
    return values[:limit], len(values) > limit


def limit(args: dict[str, Any], *, default: int = 50) -> int:
    value = args.get("limit", default)
    if type(value) is not int or value < 1:
        raise SessionError("limit must be a positive integer", kind="invalid_request")
    return value


def boolean(args: dict[str, Any], name: str, default: bool) -> bool:
    value = args.get(name, default)
    if type(value) is not bool:
        raise SessionError(f"{name} must be a boolean", kind="invalid_request")
    return value


def required_string(args: dict[str, Any], name: str, *, allow_empty: bool = False) -> str:
    value = args.get(name)
    if not isinstance(value, str) or (not allow_empty and not value):
        raise SessionError(f"{name} must be a non-empty string", kind="invalid_request")
    return value


def optional_string(
    args: dict[str, Any], name: str, *, allow_empty: bool = False
) -> str | None:
    value = args.get(name)
    if value is None:
        return None
    if not isinstance(value, str) or (not allow_empty and not value):
        raise SessionError(f"{name} must be a string", kind="invalid_request")
    return value


def string_list(args: dict[str, Any], name: str) -> list[str]:
    value = args.get(name, [])
    if not isinstance(value, list) or not all(isinstance(item, str) for item in value):
        raise SessionError(f"{name} must be a list of strings", kind="invalid_request")
    return value


def choice(
    args: dict[str, Any], name: str, choices: set[str], default: str | None = None
) -> str:
    value = args.get(name, default)
    if not isinstance(value, str) or value not in choices:
        raise SessionError(
            f"{name} must be one of: {', '.join(sorted(choices))}", kind="invalid_request"
        )
    return value


def optional_address(args: dict[str, Any], name: str) -> int | None:
    value = args.get(name)
    if value is None:
        return None
    if not isinstance(value, str):
        raise SessionError(f"{name} must be an address", kind="invalid_request")
    address = parse_address(value)
    if address is None:
        raise SessionError(f"invalid address: {value}", kind="invalid_request")
    return address


def parse_address(value: str) -> int | None:
    try:
        return int(value, 0)
    except ValueError:
        return None


def only(args: dict[str, Any], *allowed: str) -> None:
    unknown = set(args) - set(allowed)
    if unknown:
        raise SessionError(
            f"unknown argument{'s' if len(unknown) != 1 else ''}: {', '.join(sorted(unknown))}",
            kind="invalid_request",
        )
