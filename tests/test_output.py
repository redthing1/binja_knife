import json
import unittest

from bnk.output import dump_json, format_text


class TextOutputTests(unittest.TestCase):
    def test_flat_records_stay_tabular_with_multiline_and_long_scalars(self) -> None:
        text = format_text(
            [
                {"address_hex": "0x1", "value": "short", "length": 5},
                {"address_hex": "0x2", "value": "line1\nline2", "length": 11},
                {"address_hex": "0x3", "value": "x" * 160, "length": 160},
            ]
        )

        self.assertNotIn("[0]", text)
        self.assertTrue(text.splitlines()[0].startswith("address_hex"))
        self.assertIn(r"line1\nline2", text)
        self.assertIn(("x" * 117) + "...", text)

    def test_table_cells_escape_control_characters(self) -> None:
        text = format_text(
            [
                {
                    "address_hex": "0x1",
                    "value": "tab\t nul\x00 esc\x1b[31m slash\\",
                    "length": 25,
                }
            ]
        )

        self.assertIn(r"tab\t nul\x00 esc\x1b[31m slash\\", text)
        self.assertNotIn("\t", text)
        self.assertNotIn("\x00", text)
        self.assertNotIn("\x1b", text)

    def test_nested_records_use_block_rendering(self) -> None:
        text = format_text([{"address_hex": "0x1", "value": "ok", "refs": []}])

        self.assertTrue(text.startswith("[0]"))
        self.assertIn("refs", text)

    def test_json_output_keeps_original_values(self) -> None:
        rows = [{"value": "line1\nline2\t\x00"}]

        payload = json.loads(dump_json(rows, pretty=True))

        self.assertEqual(payload, rows)


if __name__ == "__main__":
    unittest.main()
