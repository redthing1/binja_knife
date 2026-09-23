from __future__ import annotations

import io
import unittest

from bnk.protocol import ProtocolError, read_message, write_message


class ProtocolTests(unittest.TestCase):
    def test_round_trip_is_one_compact_json_line(self) -> None:
        stream = io.BytesIO()
        write_message(stream, {"hello": "世界", "number": 3})
        self.assertEqual(stream.getvalue(), b'{"hello":"\xe4\xb8\x96\xe7\x95\x8c","number":3}\n')
        stream.seek(0)
        self.assertEqual(read_message(stream), {"hello": "世界", "number": 3})

    def test_rejects_invalid_json(self) -> None:
        with self.assertRaisesRegex(ProtocolError, "invalid JSON"):
            read_message(io.BytesIO(b"not-json\n"))

    def test_rejects_non_object(self) -> None:
        with self.assertRaisesRegex(ProtocolError, "JSON object"):
            read_message(io.BytesIO(b"[]\n"))


if __name__ == "__main__":
    unittest.main()
