import unittest

from bnk_serverlib.registry import Tool, _build_tool_map, list_tools


def _noop(**_kwargs):
    return None


class RegistryTests(unittest.TestCase):
    def test_tool_names_are_unique(self) -> None:
        names = [tool["name"] for tool in list_tools()]

        self.assertEqual(len(names), len(set(names)))

    def test_duplicate_tool_registration_fails(self) -> None:
        tools = (
            Tool(name="duplicate", fn=_noop, doc="first"),
            Tool(name="duplicate", fn=_noop, doc="second"),
        )

        with self.assertRaisesRegex(RuntimeError, "duplicate"):
            _build_tool_map(tools)


if __name__ == "__main__":
    unittest.main()
