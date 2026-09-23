from __future__ import annotations

import unittest
from contextlib import contextmanager
from types import SimpleNamespace
from typing import Any, Iterator

from knife.reading import ReadActions


class OneView:
    def __init__(self, view: Any) -> None:
        self.view = view

    @contextmanager
    def use(self, session_name: str | None) -> Iterator[Any]:
        yield SimpleNamespace(bv=self.view)


class ReadingTests(unittest.TestCase):
    def test_inspect_keeps_a_numeric_address_inside_a_function(self) -> None:
        block = SimpleNamespace(start=0x1000, end=0x1020)
        function = SimpleNamespace(
            start=0x1000, name="main", type="void()", total_bytes=0x20,
            basic_blocks=[block], get_comment_at=lambda address: "",
            get_instruction_containing_address=lambda address: 0x1008,
        )
        view = SimpleNamespace(
            start=0x1000, end=0x2000,
            get_function_at=lambda address: None,
            get_functions_containing=lambda address: [function],
            get_string_at=lambda address: None,
            get_symbol_at=lambda address: None,
            get_data_var_at=lambda address: None,
            get_sections_at=lambda address: [],
            get_segment_at=lambda address: None,
            get_basic_blocks_at=lambda address: [block],
            get_instruction_length=lambda address: 2,
            get_disassembly=lambda address: "call target",
            read=lambda address, length: b"\x90\x90",
            get_comment_at=lambda address: "",
        )

        result = ReadActions(OneView(view)).inspect(None, {"target": "0x1009"})

        self.assertEqual(result["address"], "0x1009")
        self.assertEqual(result["instruction_address"], "0x1008")
        self.assertEqual(result["function"]["address"], "0x1000")

    def test_outgoing_refs_include_possible_calls_without_a_target_once(self) -> None:
        function = SimpleNamespace(
            start=0x1000, name="main",
            call_sites=[SimpleNamespace(address=0x1010), SimpleNamespace(address=0x1020)],
            instructions=[([], 0x1010), ([], 0x1020)],
            get_instruction_containing_address=lambda address: address,
        )
        view = SimpleNamespace(
            start=0x1000, end=0x3000,
            get_functions_by_name=lambda name: [function] if name == "main" else [],
            get_function_at=lambda address: None,
            get_functions_containing=lambda address: [function] if address < 0x1100 else [],
            get_code_refs_from=lambda address, func=None: [0x2000] if address == 0x1020 else [],
            get_data_refs_from=lambda address: [],
            get_symbol_at=lambda address: None,
        )
        reading = ReadActions(OneView(view))

        whole = reading.refs(None, {"target": "main", "from": True})
        site = reading.refs(None, {"target": "0x1010", "from": True})

        self.assertEqual(
            [(item["kind"], item["site"], item["target"]) for item in whole["items"]],
            [("call site", "0x1010", "?"), ("call", "0x1020", "0x2000")],
        )
        self.assertEqual(site["items"], whole["items"][:1])


if __name__ == "__main__":
    unittest.main()
