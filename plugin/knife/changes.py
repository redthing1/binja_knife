from __future__ import annotations

from contextlib import contextmanager
from pathlib import Path
from typing import Any, Iterator

from .arguments import choice, only, optional_string, parse_address, required_string
from .sessions import Session, SessionError, SessionStore
from .targets import hex_address, resolve_address, resolve_function, try_function, try_variable


class ChangeActions:
    def __init__(self, bn: Any, sessions: SessionStore) -> None:
        self.bn = bn
        self.sessions = sessions

    def edit(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        target = required_string(args, "target")
        name = optional_string(args, "name")
        type_text = optional_string(args, "type")
        comment = optional_string(args, "comment", allow_empty=True)
        scope = choice(args, "scope", {"auto", "function", "view"}, "auto")
        only(args, "target", "name", "type", "comment", "scope")
        if name is None and type_text is None and comment is None:
            raise SessionError("edit requires --name, --type, or --comment", kind="invalid_request")

        with self.sessions.use(session_name) as session:
            try:
                with _change(session):
                    return self._edit(session.bv, target, name, type_text, comment, scope)
            except SessionError:
                raise
            except Exception as error:
                raise SessionError(f"edit failed: {error}", kind="edit") from error

    def patch(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        target = required_string(args, "target")
        data_text = required_string(args, "bytes")
        only(args, "target", "bytes")
        try:
            data = bytes.fromhex(data_text)
        except ValueError as error:
            raise SessionError("patch bytes must be hexadecimal", kind="invalid_request") from error
        if not data:
            raise SessionError("patch bytes must not be empty", kind="invalid_request")

        with self.sessions.use(session_name) as session:
            view = session.bv
            address = resolve_address(view, target)
            old = bytes(view.read(address, len(data)))
            if len(old) != len(data):
                raise SessionError("patch extends beyond readable data", kind="patch")
            is_code = bool(view.get_basic_blocks_at(address))
            before = view.get_disassembly(address) if is_code else None
            try:
                with _change(session):
                    written = int(view.write(address, data))
                    if written != len(data):
                        raise SessionError(
                            f"Binary Ninja wrote {written} of {len(data)} bytes", kind="patch"
                        )
                    new = bytes(view.read(address, len(data)))
                    if new != data:
                        raise SessionError(
                            "Binary Ninja did not retain the requested bytes", kind="patch"
                        )
            except SessionError:
                raise
            except Exception as error:
                raise SessionError(f"patch failed: {error}", kind="patch") from error
            return {
                "address": hex_address(address),
                "old": old.hex(" "),
                "new": new.hex(" "),
                "before": before,
                "after": view.get_disassembly(address) if is_code else None,
            }

    def undo(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        only(args)
        return self._history(session_name, redo=False)

    def redo(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        only(args)
        return self._history(session_name, redo=True)

    def save(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        path = optional_string(args, "path")
        only(args, "path")
        with self.sessions.use(session_name) as session:
            view = session.bv
            settings = self.bn.SaveSettings()
            settings.set_option(self.bn.SaveOption.TrimSnapshots)
            settings.set_option(self.bn.SaveOption.RemoveUndoData)
            with session.changes:
                if path is None:
                    if not view.file.has_database:
                        raise SessionError(
                            "this view has no database; provide a .bndb path", kind="save"
                        )
                    try:
                        ok = bool(view.save_auto_snapshot(settings=settings))
                    except Exception as error:
                        raise SessionError(f"save failed: {error}", kind="save") from error
                    destination = str(view.file.filename)
                else:
                    try:
                        ok = bool(view.create_database(path, settings=settings))
                    except Exception as error:
                        raise SessionError(f"save failed: {error}", kind="save") from error
                    destination = path
            if not ok:
                raise SessionError(f"Binary Ninja could not save {destination}", kind="save")
            return {
                "session": session.name,
                "path": destination,
                "analysis_changed": bool(view.file.analysis_changed),
                "modified": bool(view.file.modified),
            }

    def export(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        path = required_string(args, "path")
        only(args, "path")
        with self.sessions.use(session_name) as session:
            try:
                ok = bool(session.bv.save(path))
            except Exception as error:
                raise SessionError(f"export failed: {error}", kind="export") from error
            if not ok:
                raise SessionError(f"Binary Ninja could not export {path}", kind="export")
            return {"session": session.name, "path": path, "bytes": Path(path).stat().st_size}

    def _edit(
        self,
        view: Any,
        target: str,
        name: str | None,
        type_text: str | None,
        comment: str | None,
        scope: str,
    ) -> dict[str, Any]:
        variable = try_variable(view, target)
        parsed_address = parse_address(target)
        if variable is not None:
            function = None
            address = resolve_function(view, target.rsplit("::", 1)[0]).start
        elif parsed_address is not None:
            address = resolve_address(view, target)
            function = view.get_function_at(address)
        else:
            function = try_function(view, target)
            address = function.start if function is not None else resolve_address(view, target)
        data = view.get_data_var_at(address) if variable is None and function is None else None
        kind = (
            "variable"
            if variable is not None
            else "function"
            if function is not None
            else "data"
            if data is not None
            else "address"
        )
        if variable is None and function is None and data is None and (name is not None or type_text is not None):
            raise SessionError(
                "name and type edits require a function, variable, or existing data target",
                kind="edit",
            )
        changes: list[dict[str, str]] = []

        if name is not None:
            if not name:
                raise SessionError("name must not be empty", kind="edit")
            if variable is not None:
                before = str(variable.name)
                variable.set_name_async(name)
                view.update_analysis_and_wait()
                after = str(variable.name)
            elif function is not None:
                before = str(function.name)
                function.name = name
                after = str(function.name)
            else:
                before_symbol = view.get_symbol_at(address)
                before = str(before_symbol.name) if before_symbol is not None else ""
                view.define_user_symbol(self.bn.Symbol(self.bn.SymbolType.DataSymbol, address, name))
                after_symbol = view.get_symbol_at(address)
                after = str(after_symbol.name) if after_symbol is not None else ""
            if after != name:
                raise SessionError(
                    f"Binary Ninja retained the name {after!r}, not {name!r}", kind="edit"
                )
            changes.append({"field": "name", "before": before, "after": after})

        if type_text is not None:
            if not type_text.strip():
                raise SessionError("type must not be empty", kind="edit")
            if variable is not None:
                before = str(variable.type)
                parsed, _ = view.parse_type_string(type_text)
                variable.set_type_async(parsed)
                view.update_analysis_and_wait()
                after = str(variable.type)
            elif function is not None:
                before = str(function.type)
                function.set_user_type(type_text)
                view.update_analysis_and_wait()
                after = str(function.type)
            else:
                before = str(data.type)
                parsed, _ = view.parse_type_string(type_text)
                existing_name = name
                if existing_name is None:
                    symbol = view.get_symbol_at(address)
                    existing_name = str(symbol.name) if symbol is not None else None
                view.define_user_data_var(address, parsed, existing_name)
                after_data = view.get_data_var_at(address)
                after = str(after_data.type) if after_data is not None else ""
            changes.append({"field": "type", "before": before, "after": after})

        if comment is not None:
            if variable is not None:
                raise SessionError("comments cannot target a variable", kind="edit")
            actual_scope = scope
            comment_function = function
            if actual_scope == "auto":
                containers = list(view.get_functions_containing(address))
                if comment_function is None and len(containers) == 1:
                    comment_function = containers[0]
                actual_scope = "function" if comment_function is not None else "view"
            if actual_scope == "function":
                if comment_function is None:
                    containers = list(view.get_functions_containing(address))
                    if len(containers) != 1:
                        raise SessionError(
                            "function comment scope requires one containing function", kind="edit"
                        )
                    comment_function = containers[0]
                before = str(comment_function.get_comment_at(address) or "")
                comment_function.set_comment_at(address, comment)
                after = str(comment_function.get_comment_at(address) or "")
            else:
                before = str(view.get_comment_at(address) or "")
                view.set_comment_at(address, comment)
                after = str(view.get_comment_at(address) or "")
            if after != comment:
                raise SessionError("Binary Ninja did not retain the requested comment", kind="edit")
            changes.append(
                {"field": "comment", "scope": actual_scope, "before": before, "after": after}
            )

        return {"target": target, "kind": kind, "address": hex_address(address), "changes": changes}

    def _history(self, session_name: str | None, *, redo: bool) -> dict[str, Any]:
        with self.sessions.use(session_name) as session:
            view = session.bv
            source = view.file.redo_entries if redo else view.file.undo_entries
            if not source:
                raise SessionError(f"nothing to {'redo' if redo else 'undo'}", kind="history")
            with session.changes:
                view.redo() if redo else view.undo()
                view.update_analysis_and_wait()
            return {
                "action": "redo" if redo else "undo",
                "undo": len(view.file.undo_entries),
                "redo": len(view.file.redo_entries),
                "analysis_changed": bool(view.file.analysis_changed),
                "modified": bool(view.file.modified),
            }


@contextmanager
def _change(session: Session) -> Iterator[None]:
    with session.changes:
        state = session.bv.begin_undo_actions()
        try:
            yield
        except BaseException:
            session.bv.revert_undo_actions(state)
            session.bv.update_analysis_and_wait()
            raise
        else:
            session.bv.commit_undo_actions(state)
