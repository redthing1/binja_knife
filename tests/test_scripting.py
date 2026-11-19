from __future__ import annotations

import unittest
from contextlib import contextmanager
from threading import Event
from types import SimpleNamespace
from typing import Any, Iterator

from knife.scripting import PythonActions
from knife.sessions import SessionError

from bnk.client import request
from bnk.endpoint import Endpoint
from tests.support import running_server


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

    def test_client_receives_flushed_output_before_script_finishes(self) -> None:
        resume = Event()
        chunks = []
        python = PythonActions(SimpleNamespace(resume=resume), self.sessions)

        def receive(chunk: str) -> None:
            chunks.append(chunk)
            if chunk == "working ✓":
                resume.set()

        source = (
            "print('working ✓', end='', flush=True)\n"
            "assert bn.resume.wait(5)\n"
            "print(' done', end='')\n"
            "result = 42\n"
        )
        with running_server(actions={"exec": python.execute}) as (server, errors):
            result = request(
                Endpoint(*server.server_address[:2]), "exec", {"source": source},
                on_output=receive, response_timeout=10,
            )

        self.assertEqual(chunks, ["working ✓", " done"])
        self.assertEqual(result, {"output": "", "has_result": True, "result": "42"})
        self.assertEqual(errors, [])

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
