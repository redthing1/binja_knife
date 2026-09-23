from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import ANY, patch

from typer.testing import CliRunner

from bnk import __version__
from bnk.client import BnkError
from bnk.cli import app
from tests.support import running_server


class CliTests(unittest.TestCase):
    def setUp(self) -> None:
        self.runner = CliRunner()

    def test_root_help_is_compact_and_grouped(self) -> None:
        result = self.runner.invoke(app, ["--help"], color=False)
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertIn("Connection:\n  status", result.output)
        self.assertIn("version", result.output)
        self.assertIn("Sessions:\n  sessions", result.output)
        self.assertIn("open", result.output)
        self.assertIn("summary", result.output)
        self.assertIn("close", result.output)
        self.assertIn("Understand:\n  find", result.output)
        self.assertIn("inspect", result.output)
        self.assertIn("code", result.output)
        self.assertIn("refs", result.output)
        self.assertIn("sections", result.output)
        self.assertIn("segments", result.output)
        self.assertIn("Change and persist:\n  edit", result.output)
        self.assertIn("Python:\n  eval", result.output)
        self.assertIn("Start: bnk open ./program", result.output)
        self.assertNotIn("╭", result.output)

    def test_short_help_works_for_root_and_leaf_commands(self) -> None:
        root = self.runner.invoke(app, ["-h"], color=False)
        leaf = self.runner.invoke(app, ["open", "-h"], color=False)

        self.assertEqual(root.exit_code, 0, root.output)
        self.assertEqual(leaf.exit_code, 0, leaf.output)
        self.assertIn("Usage: bnk", root.output)
        self.assertIn("Usage: bnk open", leaf.output)
        self.assertIn("-h, --help", leaf.output)

    def test_version_is_local(self) -> None:
        result = self.runner.invoke(app, ["version"])
        self.assertEqual(result.exit_code, 0, result.output)
        self.assertEqual(result.output, f"bnk {__version__} (api 1)\n")

    def test_status_is_purpose_built_text(self) -> None:
        with running_server() as (server, _errors):
            host, port = server.server_address[:2]
            result = self.runner.invoke(app, ["--connect", f"{host}:{port}", "status"])

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertIn(f"connect       {host}:{port}\n", result.output)
        self.assertIn(f"client        {__version__} (api 1)\n", result.output)
        self.assertIn("binary ninja  5.3.9757-dev\n", result.output)

    def test_status_text_distinguishes_connect_and_listen_addresses(self) -> None:
        with running_server() as (server, _errors):
            host, port = server.server_address[:2]
            result = self.runner.invoke(app, ["--connect", f"localhost:{port}", "status"])

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertIn(f"connect       localhost:{port}\n", result.output)
        self.assertIn(f"listen        {host}:{port}\n", result.output)

    def test_errors_show_useful_candidates(self) -> None:
        error = BnkError(
            "several sessions are ready; choose one with -s",
            kind="session_ambiguous",
            details={"candidates": ["game", "odd\nname"]},
        )
        with patch("bnk.cli.request", side_effect=error):
            result = self.runner.invoke(app, ["summary"])

        self.assertEqual(result.exit_code, 1)
        self.assertEqual(
            result.stderr,
            "error: several sessions are ready; choose one with -s\n"
            "sessions: game, odd\\nname\n",
        )

    def test_open_resolves_a_client_path_before_sending_it(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "sample.bin")
            path.write_bytes(b"sample")
            value = {
                "session": "sample.bin",
                "path": str(path.resolve()),
                "reused": False,
                "view": "Raw",
                "architecture": None,
                "analysis": "idle",
                "function_count": 0,
            }
            with patch("bnk.cli.request", return_value=value) as remote:
                result = self.runner.invoke(app, ["open", str(path)])

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertIn("opened sample.bin\n", result.output)
        self.assertIn(f"path          {path.resolve()}\n", result.output)
        remote.assert_called_once_with(
            ANY,
            "open",
            {"path": str(path.resolve()), "server_path": False},
            session=None,
        )

    def test_server_path_is_not_required_to_exist_on_the_client(self) -> None:
        value = {
            "session": "remote.bin",
            "path": "/remote/remote.bin",
            "reused": False,
            "view": "ELF",
            "architecture": "x86_64",
            "analysis": "idle",
            "function_count": 10,
        }
        with patch("bnk.cli.request", return_value=value) as remote:
            result = self.runner.invoke(
                app,
                ["open", "/remote/remote.bin", "--server-path", "-s", "remote"],
            )

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertIn("opened", result.output)
        remote.assert_called_once_with(
            ANY,
            "open",
            {"path": "/remote/remote.bin", "server_path": True},
            session="remote",
        )

    def test_summary_reads_the_session_environment_variable(self) -> None:
        value = {
            "session": "game",
            "path": "/game",
            "view": "ELF",
            "architecture": "x86_64",
            "platform": "linux-x86_64",
            "start": "0x1000",
            "end": "0x2000",
            "length": 4096,
            "entry": "0x1100",
            "analysis": "idle",
            "function_count": 4,
            "import_count": 2,
            "string_count": 18,
            "section_count": 3,
            "segment_count": 2,
            "has_database": False,
            "analysis_changed": False,
            "modified": False,
        }
        with patch("bnk.cli.request", return_value=value) as remote:
            result = self.runner.invoke(app, ["summary"], env={"BNK_SESSION": "game"})

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertIn("range         0x1000..0x2000 (4096 bytes)", result.output)
        self.assertIn("imports       2", result.output)
        self.assertIn("strings       18", result.output)
        remote.assert_called_once_with(
            ANY,
            "summary",
            None,
            session="game",
        )

    def test_find_strings_is_one_readable_request_and_result(self) -> None:
        value = {
            "kind": "strings",
            "query": "failed",
            "items": [
                {
                    "address": "0x401020",
                    "type": "AsciiString",
                    "length": 12,
                    "refs": 1,
                    "value": "parse failed",
                    "references": [
                        {
                            "kind": "code",
                            "site": "0x400800",
                            "target": "0x401020",
                            "function": "parse",
                        }
                    ],
                }
            ],
            "more": False,
        }
        with patch("bnk.cli.request", return_value=value) as remote:
            result = self.runner.invoke(
                app,
                ["find", "strings", "failed", "--refs", "-n", "8", "-s", "game"],
            )

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertEqual(
            result.output,
            "0x401020  AsciiString  12 bytes  1 refs  parse failed\n"
            "  code   0x400800 -> 0x401020  parse\n",
        )
        remote.assert_called_once_with(
            ANY,
            "find",
            {
                "kind": "strings",
                "query": "failed",
                "limit": 8,
                "case_sensitive": False,
                "refs": True,
                "symbol_filter": "all",
            },
            session="game",
        )

    def test_find_lists_functions_and_strings_without_a_query(self) -> None:
        empty = {"kind": "functions", "query": None, "items": [], "more": False}
        with patch("bnk.cli.request", return_value=empty) as remote:
            functions = self.runner.invoke(app, ["find", "functions", "-s", "game"])

        self.assertEqual(functions.exit_code, 0, functions.output)
        remote.assert_called_once_with(
            ANY,
            "find",
            {
                "kind": "functions",
                "query": None,
                "limit": 50,
                "case_sensitive": False,
                "refs": False,
                "symbol_filter": "all",
            },
            session="game",
        )

        empty = {"kind": "strings", "query": None, "items": [], "more": False}
        with patch("bnk.cli.request", return_value=empty) as remote:
            strings = self.runner.invoke(app, ["find", "strings", "-s", "game"])

        self.assertEqual(strings.exit_code, 0, strings.output)
        remote.assert_called_once_with(
            ANY,
            "find",
            {
                "kind": "strings",
                "query": None,
                "limit": 50,
                "case_sensitive": False,
                "refs": False,
                "symbol_filter": "all",
            },
            session="game",
        )

    def test_sections_and_segments_are_direct_read_commands(self) -> None:
        sections_value = {
            "items": [
                {
                    "start": "0x1000",
                    "end": "0x1800",
                    "length": 2048,
                    "semantics": "ReadOnlyCodeSectionSemantics",
                    "name": ".text",
                }
            ],
            "more": False,
        }
        with patch("bnk.cli.request", return_value=sections_value) as remote:
            sections = self.runner.invoke(app, ["sections", "-n", "8", "-s", "game"])

        self.assertEqual(sections.exit_code, 0, sections.output)
        self.assertIn("0x1000..0x1800", sections.output)
        self.assertIn(".text", sections.output)
        remote.assert_called_once_with(ANY, "sections", {"limit": 8}, session="game")

        segments_value = {
            "items": [
                {
                    "start": "0x1000",
                    "end": "0x2000",
                    "length": 4096,
                    "file_offset": "0x0",
                    "file_end": "0x1000",
                    "file_length": 4096,
                    "readable": True,
                    "writable": False,
                    "executable": True,
                }
            ],
            "more": False,
        }
        with patch("bnk.cli.request", return_value=segments_value) as remote:
            segments = self.runner.invoke(app, ["segments", "-n", "8", "-s", "game"])

        self.assertEqual(segments.exit_code, 0, segments.output)
        self.assertIn("r-x", segments.output)
        self.assertIn("file 0x0..0x1000", segments.output)
        remote.assert_called_once_with(ANY, "segments", {"limit": 8}, session="game")

    def test_run_transmits_local_source_and_trailing_arguments(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory, "analysis.py")
            path.write_text("print(args)\nresult = len(bv.functions)\n")
            with patch(
                "bnk.cli.request",
                return_value={"output": "['one']\n", "has_result": True, "result": "4"},
            ) as remote:
                result = self.runner.invoke(
                    app,
                    ["run", str(path), "-s", "game", "--", "one"],
                )

        self.assertEqual(result.exit_code, 0, result.output)
        self.assertEqual(result.output, "['one']\nresult  4\n")
        remote.assert_called_once_with(
            ANY,
            "run",
            {
                "args": ["one"],
                "source": "print(args)\nresult = len(bv.functions)\n",
                "path": None,
                "filename": str(path.resolve()),
            },
            session="game",
        )


if __name__ == "__main__":
    unittest.main()
