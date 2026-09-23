from __future__ import annotations

import socket
import threading
import time
import unittest
from concurrent.futures import ThreadPoolExecutor

from bnk.client import BnkError, request
from bnk.endpoint import Endpoint
from bnk.protocol import read_message, write_message
from tests.support import running_server


class ClientServerTests(unittest.TestCase):
    def test_status_round_trip(self) -> None:
        with running_server() as (server, errors):
            host, port = server.server_address[:2]
            response = request(Endpoint(host, port), "status")

        self.assertEqual(response["api"], 1)
        self.assertTrue(response["compatible"])
        self.assertEqual(response["binary_ninja_version"], "5.3.9757-dev")
        self.assertEqual(response["listen"], {"host": host, "port": port})
        self.assertEqual(errors, [])

    def test_status_explains_an_api_mismatch(self) -> None:
        with running_server() as (server, _errors):
            host, port = server.server_address[:2]
            connection = socket.create_connection((host, port))
            with connection, connection.makefile("rwb") as stream:
                write_message(stream, {"api": 99, "action": "status", "args": {}})
                result = read_message(stream)

        self.assertTrue(result["ok"])
        self.assertFalse(result["value"]["compatible"])
        self.assertEqual(result["value"]["api"], 1)

    def test_unknown_action_is_a_plain_remote_error(self) -> None:
        with running_server() as (server, _errors):
            host, port = server.server_address[:2]
            with self.assertRaises(BnkError) as raised:
                request(Endpoint(host, port), "does-not-exist")

        self.assertEqual(raised.exception.kind, "unknown_action")
        self.assertEqual(str(raised.exception), "unknown action: does-not-exist")

    def test_actions_receive_optional_session_context(self) -> None:
        def echo(session: str | None, args: dict[str, object]) -> object:
            return {"session": session, "args": args}

        with running_server(actions={"echo": echo}) as (server, errors):
            host, port = server.server_address[:2]
            endpoint = Endpoint(host, port)
            unnamed = request(endpoint, "echo", {"value": 1})
            named = request(endpoint, "echo", {"value": 2}, session="game")

        self.assertEqual(unnamed["session"], None)
        self.assertEqual(named["session"], "game")
        self.assertEqual(named["args"], {"value": 2})
        self.assertEqual(errors, [])

    def test_requests_can_overlap(self) -> None:
        both_requests_entered = threading.Barrier(2)

        def binary_ninja_version() -> str:
            both_requests_entered.wait(timeout=1)
            return "concurrent-test"

        with running_server(binary_ninja_version) as (server, errors):
            host, port = server.server_address[:2]
            endpoint = Endpoint(host, port)
            with ThreadPoolExecutor(max_workers=2) as workers:
                responses = list(workers.map(lambda _index: request(endpoint, "status"), range(2)))

        self.assertEqual(
            {response["binary_ninja_version"] for response in responses},
            {"concurrent-test"},
        )
        self.assertEqual(errors, [])

    def test_disconnect_does_not_cancel_or_log_a_completed_action(self) -> None:
        entered = threading.Event()
        release = threading.Event()
        completed = threading.Event()

        def finish(
            session: str | None,
            args: dict[str, object],
        ) -> object:
            entered.set()
            release.wait(timeout=1)
            completed.set()
            return {"finished": True}

        with running_server(actions={"finish": finish}) as (server, errors):
            host, port = server.server_address[:2]
            connection = socket.create_connection((host, port))
            stream = connection.makefile("rwb")
            write_message(stream, {"api": 1, "action": "finish", "args": {}})
            self.assertTrue(entered.wait(timeout=1))
            stream.close()
            connection.close()
            release.set()
            self.assertTrue(completed.wait(timeout=1))
            time.sleep(0.05)

        self.assertEqual(errors, [])

    def test_server_surfaces_unexpected_failures_and_the_traceback(self) -> None:
        def binary_ninja_version() -> str:
            raise RuntimeError("private failure detail")

        with running_server(binary_ninja_version) as (server, errors):
            host, port = server.server_address[:2]
            with self.assertRaises(BnkError) as raised:
                request(Endpoint(host, port), "status")

        self.assertEqual(raised.exception.kind, "server")
        self.assertEqual(str(raised.exception), "RuntimeError: private failure detail")
        self.assertIn("RuntimeError: private failure detail", raised.exception.details["traceback"])
        self.assertEqual(len(errors), 1)
        self.assertIn("RuntimeError: private failure detail", errors[0])


if __name__ == "__main__":
    unittest.main()
