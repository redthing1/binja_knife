import unittest


class ServerImportTests(unittest.TestCase):
    def test_server_package_imports_without_binaryninja(self) -> None:
        import server

        self.assertTrue(hasattr(server, "plugin"))

    def test_server_plugin_package_imports_without_binaryninja(self) -> None:
        import server.plugin

        self.assertIsNone(server.plugin.bn)


if __name__ == "__main__":
    unittest.main()
