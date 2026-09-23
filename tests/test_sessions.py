from __future__ import annotations

import tempfile
import threading
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from types import SimpleNamespace

from knife.sessions import SessionError, SessionStore


class FakeFile:
    def __init__(
        self,
        *,
        analysis_changed: bool = False,
        modified: bool = False,
        has_database: bool = False,
    ) -> None:
        self.analysis_changed = analysis_changed
        self.modified = modified
        self.has_database = has_database
        self.close_count = 0

    def close(self) -> None:
        self.close_count += 1


class FakeView:
    def __init__(
        self,
        *,
        analysis_changed: bool = False,
        modified: bool = False,
    ) -> None:
        self.view_type = "ELF"
        self.arch = SimpleNamespace(name="x86_64")
        self.platform = SimpleNamespace(name="linux-x86_64")
        self.start = 0x400000
        self.end = 0x402000
        self.length = 0x2000
        self.entry_point = 0x401000
        self.analysis_state = SimpleNamespace(name="IdleState")
        self.functions = [object(), object()]
        self.sections = {".text": object()}
        self.segments = [object()]
        self.strings = [object(), object(), object()]
        self.symbols = [
            SimpleNamespace(
                type=SimpleNamespace(name="ImportedFunctionSymbol"), full_name="puts"
            ),
            SimpleNamespace(type=SimpleNamespace(name="FunctionSymbol"), full_name="main"),
        ]
        self.file = FakeFile(analysis_changed=analysis_changed, modified=modified)

    def get_strings(self) -> list[object]:
        return self.strings

    def get_symbols(self) -> list[SimpleNamespace]:
        return self.symbols


class ManualClock:
    def __init__(self) -> None:
        self.now = 100.0

    def __call__(self) -> float:
        return self.now


class SessionStoreTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.path = Path(self.temporary.name, "game.bin")
        self.path.write_bytes(b"binary")
        self.views: list[FakeView] = []
        self.clock = ManualClock()

        def load(path: str, *, update_analysis: bool) -> FakeView:
            self.assertEqual(path, str(self.path.resolve()))
            self.assertTrue(update_analysis)
            view = FakeView()
            self.views.append(view)
            return view

        self.store = SessionStore(load, clock=self.clock)

    def open(self, name: str | None = None) -> dict[str, object]:
        return self.store.open(
            name,
            {"path": str(self.path.resolve()), "server_path": True},
        )

    def test_open_list_summary_and_clean_close(self) -> None:
        opened = self.open()
        self.assertEqual(opened["session"], "game.bin")
        self.assertFalse(opened["reused"])

        self.clock.now = 103.25
        listed = self.store.list_sessions(None, {})
        self.assertEqual(
            listed,
            {
                "sessions": [
                    {
                        "name": "game.bin",
                        "state": "ready",
                        "path": str(self.path.resolve()),
                        "active": 0,
                        "age_seconds": 3.25,
                    }
                ]
            },
        )

        summary = self.store.summary(None, {})
        self.assertEqual(summary["analysis"], "idle")
        self.assertEqual(summary["start"], "0x400000")
        self.assertEqual(summary["function_count"], 2)
        self.assertEqual(summary["import_count"], 1)
        self.assertEqual(summary["string_count"], 3)

        closed = self.store.close(None, {})
        self.assertEqual(closed["session"], "game.bin")
        self.assertEqual(self.views[0].file.close_count, 1)
        self.assertEqual(self.store.list_sessions(None, {}), {"sessions": []})

    def test_reuses_one_matching_path_without_an_explicit_name(self) -> None:
        first = self.open(name="custom")
        second = self.open()
        self.assertFalse(first["reused"])
        self.assertTrue(second["reused"])
        self.assertEqual(second["session"], "custom")
        self.assertEqual(len(self.views), 1)

    def test_explicit_new_name_allows_an_independent_view(self) -> None:
        self.open(name="one")
        self.open(name="two")
        self.assertEqual(len(self.views), 2)
        with self.assertRaises(SessionError) as raised:
            self.store.summary(None, {})
        self.assertEqual(raised.exception.kind, "session_ambiguous")
        self.assertEqual(raised.exception.details["candidates"], ["one", "two"])

    def test_unnamed_reuse_prefers_the_derived_name_among_duplicates(self) -> None:
        self.open(name="other")
        self.open(name="game.bin")
        result = self.open()
        self.assertTrue(result["reused"])
        self.assertEqual(result["session"], "game.bin")

    def test_unnamed_reuse_does_not_choose_arbitrarily_among_duplicates(self) -> None:
        self.open(name="one")
        self.open(name="two")
        with self.assertRaises(SessionError) as raised:
            self.open()
        self.assertEqual(raised.exception.kind, "session_ambiguous")
        self.assertEqual(raised.exception.details["candidates"], ["one", "two"])

    def test_failed_open_removes_its_reservation(self) -> None:
        def fail(path: str, *, update_analysis: bool) -> None:
            raise RuntimeError("loader failed")

        store = SessionStore(fail)
        with self.assertRaises(SessionError) as raised:
            store.open(None, {"path": str(self.path.resolve()), "server_path": True})
        self.assertEqual(raised.exception.kind, "load")
        self.assertEqual(store.list_sessions(None, {}), {"sessions": []})

    def test_opening_is_visible_and_not_duplicated(self) -> None:
        entered = threading.Event()
        release = threading.Event()

        def slow_load(path: str, *, update_analysis: bool) -> FakeView:
            entered.set()
            release.wait(timeout=2)
            return FakeView()

        store = SessionStore(slow_load, clock=self.clock)
        with ThreadPoolExecutor(max_workers=1) as workers:
            future = workers.submit(
                store.open,
                None,
                {"path": str(self.path.resolve()), "server_path": True},
            )
            self.assertTrue(entered.wait(timeout=1))
            listed = store.list_sessions(None, {})["sessions"]
            self.assertEqual(listed[0]["state"], "opening")
            with self.assertRaises(SessionError) as raised:
                store.open(
                    None,
                    {"path": str(self.path.resolve()), "server_path": True},
                )
            self.assertEqual(raised.exception.kind, "session_opening")
            release.set()
            future.result(timeout=1)

    def test_close_refuses_a_session_in_use(self) -> None:
        self.open()
        with self.store.use(None):
            with self.assertRaises(SessionError) as raised:
                self.store.close(None, {})
        self.assertEqual(raised.exception.kind, "session_busy")
        self.assertEqual(raised.exception.details["active"], 1)

    def test_two_uses_of_one_session_overlap(self) -> None:
        self.open()
        with self.store.use(None):
            with self.store.use(None):
                item = self.store.list_sessions(None, {})["sessions"][0]
                self.assertEqual(item["active"], 2)

    def test_use_releases_after_an_exception(self) -> None:
        self.open()
        with self.assertRaises(RuntimeError):
            with self.store.use(None):
                raise RuntimeError("action failed")
        self.store.close(None, {})

    def test_dirty_close_requires_discard(self) -> None:
        view = FakeView(analysis_changed=True, modified=True)
        store = SessionStore(lambda path, update_analysis: view)
        store.open(None, {"path": str(self.path.resolve()), "server_path": True})
        with self.assertRaises(SessionError) as raised:
            store.close(None, {})
        self.assertEqual(raised.exception.kind, "dirty")
        self.assertTrue(raised.exception.details["analysis_changed"])
        self.assertTrue(raised.exception.details["modified"])
        self.assertEqual(view.file.close_count, 0)

        result = store.close(None, {"discard": True})
        self.assertTrue(result["discarded"])
        self.assertEqual(view.file.close_count, 1)

    def test_discard_flag_does_not_claim_clean_changes(self) -> None:
        self.open()

        result = self.store.close(None, {"discard": True})

        self.assertFalse(result["discarded"])

    def test_server_path_must_be_absolute(self) -> None:
        with self.assertRaises(SessionError) as raised:
            self.store.open(None, {"path": "relative.bin", "server_path": True})
        self.assertEqual(raised.exception.kind, "path")


if __name__ == "__main__":
    unittest.main()
