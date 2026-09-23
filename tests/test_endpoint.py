from __future__ import annotations

import unittest

from bnk.endpoint import Endpoint, EndpointError


class EndpointTests(unittest.TestCase):
    def test_parses_host_and_port(self) -> None:
        endpoint = Endpoint.parse("example.test:18812")
        self.assertEqual(endpoint, Endpoint("example.test", 18812))
        self.assertEqual(str(endpoint), "example.test:18812")

    def test_parses_bracketed_ipv6(self) -> None:
        endpoint = Endpoint.parse("[::1]:18812")
        self.assertEqual(endpoint, Endpoint("::1", 18812))
        self.assertEqual(str(endpoint), "[::1]:18812")

    def test_rejects_invalid_endpoints(self) -> None:
        for value in (
            "",
            "localhost",
            ":18812",
            "localhost:nope",
            "localhost:0",
            "localhost:65536",
            "::1:18812",
        ):
            with self.subTest(value=value), self.assertRaises(EndpointError):
                Endpoint.parse(value)


if __name__ == "__main__":
    unittest.main()
