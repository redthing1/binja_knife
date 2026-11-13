from __future__ import annotations

import unittest
from types import SimpleNamespace

from knife.loading import ViewLoader
from knife.sessions import SessionError


class LoadingTests(unittest.TestCase):
    def loader(self, *, saved=False, selected=None, choices=("Raw", "ELF")):
        self.closed = self.analyzed = 0

        def close():
            self.closed += 1

        def analyze():
            self.analyzed += 1

        def metadata(key):
            if selected is None:
                raise KeyError(key)
            return selected

        raw = SimpleNamespace(available_view_types=[SimpleNamespace(name=n) for n in choices],
                              query_metadata=metadata)
        file = SimpleNamespace(raw=raw, has_database=saved, existing_views=choices, close=close)
        views = {n: SimpleNamespace(view_type=n, file=file, update_analysis_and_wait=analyze) for n in choices}
        file.get_view_of_type = views.get
        bn = SimpleNamespace(load=lambda path, update_analysis: views["Raw"])
        return ViewLoader(bn)

    def test_saved_analysis_is_selected_instead_of_raw(self):
        loader = self.loader(saved=True)
        self.assertEqual(loader("sample.bndb").view_type, "ELF")
        self.assertEqual(self.analyzed, 1)
        self.assertEqual(self.closed, 0)

    def test_saved_selection_and_explicit_override(self):
        loader = self.loader(saved=True, selected="Custom", choices=("Raw", "ELF", "Custom"))
        self.assertEqual(loader("sample.bndb").view_type, "Custom")
        self.assertEqual(loader("sample.bndb", view_type="ELF").view_type, "ELF")

    def test_ambiguity_and_unavailable_view_close_file(self):
        loader = self.loader(choices=("Raw", "ELF", "Custom"))
        for requested in (None, "Missing"):
            with self.assertRaises(SessionError) as error:
                loader("sample", view_type=requested)
            self.assertEqual(error.exception.kind, "view")
        self.assertEqual(self.closed, 2)
        self.assertEqual(self.analyzed, 0)

    def test_discovery_does_not_analyze_or_retain_file(self):
        loader = self.loader()
        self.assertEqual(loader("sample", list_views=True), {"views": ["ELF", "Raw"]})
        self.assertEqual(self.analyzed, 0)
        self.assertEqual(self.closed, 1)
