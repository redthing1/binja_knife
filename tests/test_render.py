from __future__ import annotations

import unittest

from bnk.render import (
    close_text,
    code_text,
    error_text,
    find_text,
    inspect_text,
    refs_text,
    sections_text,
    segments_text,
    sessions_text,
)


class RenderTests(unittest.TestCase):
    def test_one_line_rows_escape_controls_and_backslashes(self) -> None:
        rendered = sessions_text(
            {
                "sessions": [
                    {
                        "name": "odd\nname",
                        "state": "ready",
                        "path": "/tmp/a\tb\\c",
                        "active": 0,
                        "age_seconds": 1.25,
                    }
                ]
            }
        )

        self.assertEqual(rendered, "odd\\nname  ready  active 0  1.250s  /tmp/a\\tb\\\\c")

    def test_error_details_remain_small_and_actionable(self) -> None:
        rendered = error_text(
            "several sessions are ready; choose one with -s",
            kind="session_ambiguous",
            details={"candidates": ["one", "two"]},
        )

        self.assertEqual(
            rendered,
            "error: several sessions are ready; choose one with -s\n"
            "sessions: one, two",
        )

    def test_close_mentions_discard_only_when_the_server_reports_it(self) -> None:
        value = {"session": "game", "path": "/tmp/game", "discarded": False}

        self.assertEqual(close_text(value), "closed game\npath  /tmp/game")

    def test_find_keeps_full_evidence_and_makes_a_bound_visible(self) -> None:
        rendered = find_text(
            {
                "kind": "strings",
                "items": [
                    {
                        "address": "0x1000",
                        "type": "AsciiString",
                        "length": 5,
                        "refs": 0,
                        "value": "a\nb\\c",
                    }
                ],
                "more": True,
            }
        )

        self.assertEqual(
            rendered,
            "0x1000  AsciiString  5 bytes  0 refs  a\\nb\\\\c\n"
            "… more matches; rerun with --limit above 1",
        )

    def test_code_preserves_multiline_text(self) -> None:
        rendered = code_text(
            {
                "function": "main",
                "address": "0x1000",
                "level": "hlil",
                "ssa": False,
                "at": None,
                "lines": [
                    {"address": "0x1000", "index": 0, "text": "if (ready)\n    work()"}
                ],
                "more": False,
            }
        )

        self.assertEqual(
            rendered,
            "main @ 0x1000  hlil\n"
            "0x1000  0  if (ready)\n"
            "               work()",
        )

    def test_inspect_keeps_containing_anchors_and_variable_identity(self) -> None:
        instruction = inspect_text(
            {
                "address": "0x1001",
                "sections": [".text"],
                "instruction_address": "0x1000",
                "instruction": "call target",
                "bytes": "e8 00",
            }
        )
        self.assertIn("instruction  0x1000 +1  e8 00  call target", instruction)

        string = inspect_text(
            {
                "address": "0x1001",
                "sections": [".rodata"],
                "string": {
                    "address": "0x1000", "type": "AsciiString", "length": 8,
                    "refs": 2, "value": "example",
                },
            }
        )
        self.assertIn("string    0x1000 +1  AsciiString, 8 bytes, 2 refs: example", string)

        variable = inspect_text(
            {
                "variable_target": True,
                "function": {"name": "main", "address": "0x1000"},
                "variable": {
                    "name": "argc", "target": "#123", "type": "int32_t", "parameter": True,
                },
            }
        )
        self.assertIn("variable   main::argc", variable)
        self.assertIn("exact      main::#123", variable)
        self.assertNotIn("instruction", variable)

    def test_focused_code_and_entry_refs_label_their_scope(self) -> None:
        code = code_text(
            {
                "function": "main", "address": "0x1000", "level": "hlil", "ssa": False,
                "at": "0x1001", "instruction_address": "0x1000",
                "lines": [
                    {"address": "0x1000", "index": 1, "expression": 2, "text": "call()", "related": False},
                    {"address": "0x1008", "index": 3, "expression": 4, "text": "use()", "related": True},
                ],
                "more": False,
            }
        )
        self.assertIn("at 0x1001 (instruction 0x1000 +1)", code)
        self.assertIn("\nrelated\n0x1008", code)

        refs = refs_text(
            {
                "target": "0x1000", "direction": "from", "entry_function": "main",
                "site_items": [], "site_more": False,
                "items": [{"kind": "call", "site": "0x1008", "target": "0x2000"}],
                "more": False,
            }
        )
        self.assertIn("at entry\nnone\nfrom main (whole function)", refs)
        self.assertIn("call   0x1008 -> 0x2000", refs)

    def test_interior_refs_keep_exact_and_containing_results_distinct(self) -> None:
        rendered = refs_text(
            {
                "target": "0x1001", "address": "0x1001", "direction": "to",
                "items": [], "more": False,
                "anchor_kind": "string", "anchor_address": "0x1000",
                "anchor_items": [{"kind": "code", "site": "0x2000", "target": "0x1000"}],
                "anchor_more": False,
            }
        )

        self.assertEqual(
            rendered,
            "references to 0x1001\nnone\n"
            "containing string at 0x1000 +1\ncode   0x2000 -> 0x1000",
        )

    def test_sections_and_segments_preserve_layout_details(self) -> None:
        section = {
            "start": "0x1000",
            "end": "0x1800",
            "length": 2048,
            "semantics": "ReadOnlyCodeSectionSemantics",
            "name": ".text",
        }
        segment = {
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

        self.assertEqual(
            sections_text({"items": [section], "more": False}),
            "0x1000..0x1800  2048 bytes  read-only code  .text",
        )
        self.assertEqual(
            segments_text({"items": [segment], "more": False}),
            "0x1000..0x2000  4096 bytes  r-x  file 0x0..0x1000 (4096 bytes)",
        )
        inspected = inspect_text(
            {"address": "0x1200", "sections": [".text"], "segment": segment}
        )
        self.assertIn("sections  .text", inspected)
        self.assertIn("segment   0x1000..0x2000", inspected)


if __name__ == "__main__":
    unittest.main()
