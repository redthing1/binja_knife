from __future__ import annotations

import builtins
import io
import traceback
from pathlib import Path
from typing import Any

from .arguments import only, optional_string, required_string, string_list
from .sessions import Session, SessionError, SessionStore


class PythonActions:
    def __init__(self, bn: Any, sessions: SessionStore) -> None:
        self.bn = bn
        self.sessions = sessions

    def evaluate(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        expression = required_string(args, "source")
        script_args = string_list(args, "args")
        only(args, "source", "args")
        with self.sessions.use(session_name) as session:
            return self._execute(session, expression, script_args, mode="eval", filename="<bnk eval>")

    def execute(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        source = required_string(args, "source", allow_empty=True)
        script_args = string_list(args, "args")
        filename = optional_string(args, "filename") or "<bnk exec>"
        only(args, "source", "args", "filename")
        with self.sessions.use(session_name) as session:
            return self._execute(session, source, script_args, mode="exec", filename=filename)

    def run(self, session_name: str | None, args: dict[str, Any]) -> dict[str, Any]:
        source = optional_string(args, "source", allow_empty=True)
        path = optional_string(args, "path")
        source_name = optional_string(args, "filename")
        script_args = string_list(args, "args")
        only(args, "source", "path", "filename", "args")
        if (source is None) == (path is None):
            raise SessionError("run requires exactly one of source or server path", kind="invalid_request")
        if path is not None:
            try:
                source = Path(path).read_text()
            except (OSError, UnicodeError) as error:
                raise SessionError(f"cannot read script {path}: {error}", kind="path") from error
            filename = path
        else:
            filename = source_name or "<bnk run>"
        assert source is not None
        with self.sessions.use(session_name) as session:
            return self._execute(session, source, script_args, mode="exec", filename=filename)

    def _execute(
        self, session: Session, source: str, args: list[str], *, mode: str, filename: str
    ) -> dict[str, Any]:
        output = io.StringIO()

        def local_print(*values: Any, **kwargs: Any) -> None:
            kwargs = dict(kwargs)
            destination = kwargs.pop("file", output)
            if destination is None:
                destination = output
            if destination is not output:
                raise ValueError("bnk script print does not support another file")
            builtins.print(*values, file=output, **kwargs)

        namespace: dict[str, Any] = {
            "__name__": "__main__",
            "__file__": filename,
            "bn": self.bn,
            "bv": session.bv,
            "session": {"name": session.name, "path": session.path},
            "args": list(args),
            "print": local_print,
        }
        try:
            if mode == "eval":
                result = eval(compile(source, filename, "eval"), namespace, namespace)
                has_result = True
            else:
                exec(compile(source, filename, "exec"), namespace, namespace)
                has_result = "result" in namespace
                result = namespace.get("result")
            result_text = repr(result) if has_result else None
        except BaseException as error:
            raise SessionError(
                f"{type(error).__name__}: {error}",
                kind="python",
                details={"traceback": traceback.format_exc(), "output": output.getvalue()},
            ) from error
        return {
            "output": output.getvalue(),
            "has_result": has_result,
            "result": result_text,
        }
