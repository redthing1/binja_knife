from __future__ import annotations

from typing import Any

from .arguments import parse_address
from .sessions import SessionError


def try_function(view: Any, target: str) -> Any | None:
    address = parse_address(target)
    if address is not None:
        exact = view.get_function_at(address)
        if exact is not None:
            return exact
        containing = list(view.get_functions_containing(address))
        return containing[0] if len(containing) == 1 else None
    matches = list(view.get_functions_by_name(target))
    return matches[0] if len(matches) == 1 else None


def resolve_function(view: Any, target: str) -> Any:
    function = try_function(view, target)
    if function is not None:
        return function
    address = parse_address(target)
    matches = (
        list(view.get_functions_by_name(target))
        if address is None else list(view.get_functions_containing(address))
    )
    if len(matches) > 1:
        raise SessionError(
            f"function target '{target}' is ambiguous",
            kind="target_ambiguous",
            details={"candidates": [
                f"{item.name} @ {hex_address(item.start)}" for item in matches[:8]
            ]},
        )
    raise SessionError(f"function not found: {target}", kind="target_not_found")


def resolve_address(view: Any, target: str) -> int:
    address = parse_address(target)
    if address is not None:
        if address < view.start or address >= view.end:
            raise SessionError(
                f"address is outside the view: {hex_address(address)}", kind="target_not_found"
            )
        return address

    symbols = list(view.get_symbols_by_name(target))
    symbol_addresses = sorted({int(symbol.address) for symbol in symbols})
    if len(symbol_addresses) == 1:
        return symbol_addresses[0]
    if len(symbol_addresses) > 1:
        raise SessionError(
            f"target '{target}' is ambiguous",
            kind="target_ambiguous",
            details={"candidates": [hex_address(item) for item in symbol_addresses[:8]]},
        )

    functions = list(view.get_functions_by_name(target))
    addresses = sorted({int(function.start) for function in functions})
    if len(addresses) == 1:
        return addresses[0]
    if len(addresses) > 1:
        raise SessionError(
            f"target '{target}' is ambiguous",
            kind="target_ambiguous",
            details={"candidates": [hex_address(item) for item in addresses[:8]]},
        )
    raise SessionError(f"target not found: {target}", kind="target_not_found")


def try_variable(view: Any, target: str) -> Any | None:
    if "::" not in target:
        return None
    if view.get_functions_by_name(target) or view.get_symbols_by_name(target):
        return None
    function_target, variable_target = target.rsplit("::", 1)
    function = resolve_function(view, function_target)
    if variable_target.startswith("#"):
        try:
            identifier = int(variable_target[1:], 0)
        except ValueError as error:
            raise SessionError("variable identifier must be an integer", kind="target_not_found") from error
        for variable in function.vars:
            if int(variable.identifier) == identifier:
                return variable
        raise SessionError(f"variable not found: {target}", kind="target_not_found")
    variable = function.get_variable_by_name(variable_target)
    if variable is None:
        raise SessionError(f"variable not found: {target}", kind="target_not_found")
    return variable


def enum_name(value: Any) -> str:
    return str(getattr(value, "name", value))


def hex_address(value: Any) -> str:
    return hex(int(value))
