from __future__ import annotations

import unittest
from contextlib import contextmanager
from types import SimpleNamespace
from typing import Any, Iterator

from knife.scripting import PythonActions
from knife.sessions import SessionError


class OneSession:
    @contextmanager
    def use(self, session_name: str | None) -> Iterator[Any]:
        self.selected = session_name
        yield SimpleNamespace(
            name="game",
            path="/game",
            bv=SimpleNamespace(functions=[1, 2, 3]),
        )


class ScriptingTests(unittest.TestCase):
    def setUp(self) -> None:
        self.sessions: Any = OneSession()
        self.python = PythonActions(SimpleNamespace(version="test"), self.sessions)

    def test_exec_gets_a_fresh_useful_namespace(self) -> None:
        result = self.python.execute(
            "game",
            {
                "source": "print(session['name'], args); result = (bn.version, len(bv.functions))",
                "args": ["one"],
            },
        )

        self.assertEqual(self.sessions.selected, "game")
        self.assertEqual(
            result,
            {"output": "game ['one']\n", "has_result": True, "result": "('test', 3)"},
        )

    def test_script_failure_preserves_output_and_a_traceback(self) -> None:
        with self.assertRaises(SessionError) as raised:
            self.python.execute(
                None,
                {"source": "print('before'); raise ValueError('bad')", "args": []},
            )

        self.assertEqual(raised.exception.kind, "python")
        self.assertEqual(raised.exception.details["output"], "before\n")
        self.assertIn("ValueError: bad", raised.exception.details["traceback"])

    def test_failed_result_repr_preserves_script_output(self) -> None:
        with self.assertRaises(SessionError) as raised:
            self.python.execute(
                None,
                {
                    "source": "print('before'); result = type('Broken', (), "
                    "{'__repr__': lambda self: 1/0})()",
                    "args": [],
                },
            )

        self.assertEqual(raised.exception.kind, "python")
        self.assertEqual(raised.exception.details["output"], "before\n")
        self.assertIn("ZeroDivisionError", raised.exception.details["traceback"])


if __name__ == "__main__":
    unittest.main()
