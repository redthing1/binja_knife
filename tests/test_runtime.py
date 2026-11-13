from __future__ import annotations

import io
import json
import os
import stat
import tarfile
import tempfile
import unittest
import zipfile
from pathlib import Path
from unittest.mock import patch

from typer.testing import CliRunner

from bnk.cli import app
from bnk.client import BnkError
from bnk.runtime.install import install, unpack
from bnk.runtime.plugins import PluginSpec, plugin_spec
from bnk.runtime.native import library_path, load_manifest
from bnk.runtime.process import stop


class RuntimeTests(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)
        self.env = patch.dict(os.environ, {
            "XDG_DATA_HOME": str(self.root / "data"),
            "XDG_STATE_HOME": str(self.root / "state"),
        })
        self.env.start()
        self.addCleanup(self.env.stop)
        self.runtime = self.root / "data/bnk/runtime"
        self.runtime.mkdir(parents=True)
        (self.runtime / "runtime.json").write_text('{"format": 2}')
        self.runner = CliRunner()

    def test_default_connection_starts_once_before_retry(self):
        error = BnkError("refused", kind="connection", details={"connect_failed": True})
        with patch("bnk.cli.request", side_effect=[error, {"items": []}]) as remote, \
             patch("bnk.runtime.process.ensure_started") as start:
            result = self.runner.invoke(app, ["sessions"])
        self.assertEqual(result.exit_code, 0, result.output)
        start.assert_called_once_with()
        self.assertEqual(remote.call_count, 2)

    def test_explicit_endpoint_and_environment_never_start_a_runtime(self):
        error = BnkError("refused", kind="connection", details={"connect_failed": True})
        for args, env in ((["--connect", "127.0.0.1:18812", "sessions"], {}),
                          (["sessions"], {"BNK_CONNECT": "127.0.0.1:18812"})):
            with self.subTest(args=args, env=env), \
                 patch("bnk.cli.request", side_effect=error) as remote, \
                 patch("bnk.runtime.process.ensure_started") as start:
                result = self.runner.invoke(app, args, env=env)
                self.assertEqual(result.exit_code, 1)
                start.assert_not_called()
                remote.assert_called_once()

    def test_lost_response_does_not_retry_an_edit(self):
        with patch("bnk.cli.request", side_effect=BnkError("lost", kind="connection")) as remote, \
             patch("bnk.runtime.process.ensure_started") as start:
            result = self.runner.invoke(app, ["patch", "0x1000", "90"])
        self.assertEqual(result.exit_code, 1)
        start.assert_not_called()
        remote.assert_called_once()

    def test_uninstalled_client_keeps_existing_connection_behavior(self):
        (self.runtime / "runtime.json").unlink()
        error = BnkError("refused", kind="connection", details={"connect_failed": True})
        with patch("bnk.cli.request", side_effect=error), \
             patch("bnk.runtime.process.ensure_started") as start:
            result = self.runner.invoke(app, ["sessions"])
        self.assertEqual(result.exit_code, 1)
        start.assert_not_called()

    def test_runtime_status_and_logs_do_not_start_server(self):
        with patch("bnk.runtime.process.ensure_started") as start:
            status = self.runner.invoke(app, ["runtime", "status"])
            logs = self.runner.invoke(app, ["runtime", "logs"])
        self.assertEqual(status.exit_code, 0, status.output)
        self.assertIn("stopped", status.output)
        self.assertEqual(logs.exit_code, 0, logs.output)
        start.assert_not_called()

    def test_stale_pid_record_never_signals_an_unowned_process(self):
        state = self.root / "state/bnk"
        state.mkdir(parents=True)
        (state / "supervisor.lock").touch()
        (state / "process.json").write_text(json.dumps({"pid": os.getpid(), "identity": "old"}))
        with patch("bnk.runtime.process.os.kill") as kill:
            self.assertFalse(stop(state))
        kill.assert_not_called()

    def archive(self, name, *, link=None):
        source = self.root / "input.tar"
        with tarfile.open(source, "w") as archive:
            item = tarfile.TarInfo(name)
            if link is not None:
                item.type = tarfile.SYMTYPE
                item.linkname = link
                archive.addfile(item)
            else:
                item.mode = 0o755
                item.size = 5
                archive.addfile(item, io.BytesIO(b"hello"))
        return source

    def test_archive_rejects_path_and_symlink_escape(self):
        for name, link in (("../escaped", None), ("bin/link", "../../escaped")):
            with self.subTest(name=name):
                destination = self.root / "extracted"
                destination.mkdir(exist_ok=True)
                with self.assertRaises(tarfile.FilterError):
                    unpack(self.archive(name, link=link), destination)
                self.assertFalse((self.root / "escaped").exists())

    def test_archive_preserves_executable_permissions(self):
        destination = self.root / "extracted"
        destination.mkdir()
        unpack(self.archive("binaryninja/binaryninja"), destination)
        self.assertTrue(os.access(destination / "binaryninja/binaryninja", os.X_OK))

    def test_zip_rejects_path_escape(self):
        source = self.root / "input.zip"
        with zipfile.ZipFile(source, "w") as archive:
            archive.writestr("../escaped", "bad")
        with self.assertRaises(ValueError):
            unpack(source, self.root / "extracted")
        self.assertFalse((self.root / "escaped").exists())

    def test_zip_preserves_relative_links_and_rejects_external_links(self):
        for target in ("binaryninja", "../../escaped"):
            with self.subTest(target=target):
                source = self.root / "links.zip"
                with zipfile.ZipFile(source, "w") as archive:
                    archive.writestr("bin/binaryninja", "sample")
                    link = zipfile.ZipInfo("bin/link")
                    link.create_system = 3
                    link.external_attr = (stat.S_IFLNK | 0o777) << 16
                    archive.writestr(link, target)
                destination = self.root / ("safe" if target == "binaryninja" else "unsafe")
                if target == "binaryninja":
                    unpack(source, destination)
                    self.assertTrue((destination / "bin/link").is_symlink())
                    self.assertEqual((destination / "bin/link").read_text(), "sample")
                else:
                    with self.assertRaises(ValueError):
                        unpack(source, destination)

    def test_native_manifests_cover_both_runtime_architectures(self):
        for name in ("x86_64", "aarch64"):
            with self.subTest(name=name):
                path, manifest = load_manifest(name)
                self.assertEqual(path.name, f"{name}.json")
                self.assertEqual(manifest["triplet"], f"{name}-linux-gnu")
                self.assertEqual(manifest["platform"], f"linux-{name}")
                self.assertGreater(len(manifest["packages"]), 0)

    def test_unknown_architecture_is_rejected_clearly(self):
        with self.assertRaises(BnkError) as error:
            load_manifest("riscv64")
        self.assertIn("unsupported architecture riscv64", str(error.exception))
        self.assertIn("aarch64", str(error.exception))

    def test_library_path_follows_the_installed_manifest(self):
        native = self.runtime / "native"
        native.mkdir()
        (native / "libraries.json").write_text(json.dumps({"triplet": "aarch64-linux-gnu"}))
        self.assertEqual(
            library_path(self.runtime).split(":"),
            [
                str(self.runtime / "binaryninja"),
                str(native / "usr/lib/aarch64-linux-gnu"),
                str(native / "lib/aarch64-linux-gnu"),
            ],
        )

    def test_library_path_uses_host_triplet_for_old_bundles(self):
        with patch("bnk.runtime.native.machine", return_value="aarch64"):
            self.assertEqual(
                library_path(self.runtime).split(":"),
                [
                    str(self.runtime / "binaryninja"),
                    str(self.runtime / "native/usr/lib/aarch64-linux-gnu"),
                    str(self.runtime / "native/lib/aarch64-linux-gnu"),
                ],
            )

    def test_plugin_manifest_has_explicit_build_and_dependencies(self):
        self.assertEqual(plugin_spec("https://example.test/plugin.git"),
                         PluginSpec("https://example.test/plugin.git"))
        self.assertEqual(plugin_spec("https://example.test/plugin.git main deps=msgpack,foo"),
                         PluginSpec("https://example.test/plugin.git", "main", ["msgpack", "foo"]))
        self.assertEqual(plugin_spec("repo deps=msgpack"), PluginSpec("repo", deps=["msgpack"]))
        self.assertEqual(plugin_spec("repo build=cmake"), PluginSpec("repo", build="cmake"))
        with self.assertRaises(ValueError):
            plugin_spec("repo main unexpected")

    def test_local_plugin_repository_is_recorded_as_an_absolute_path(self):
        from contextlib import chdir
        with chdir(self.root):
            spec = PluginSpec("./data/../data")
        self.assertEqual(spec.repo, str(self.root / "data"))
        self.assertEqual(spec.name, "data")

    def prepared_archive(self):
        source = self.root / "bundle.tar"
        with tarfile.open(source, "w") as archive:
            item = tarfile.TarInfo("runtime/runtime.json")
            content = b'{"format": 2}'
            item.size = len(content)
            archive.addfile(item, io.BytesIO(content))
        return source

    def test_update_preparation_failure_keeps_original_files_and_restarts(self):
        from bnk.runtime.install import change_plugins
        record = {"name": "example", "repo": "example", "ref": "main", "deps": [],
                  "build": "python", "commit": "before", "artifacts": ["plugins/example"]}
        metadata = {"format": 2, "plugins": [record]}
        (self.runtime / "runtime.json").write_text(json.dumps(metadata))
        original = self.runtime / "plugins/example"
        original.mkdir(parents=True)
        (original / "__init__.py").write_text("original")
        with patch("bnk.runtime.install.supervisor_pid", return_value=None), \
             patch("bnk.runtime.install.prepare", side_effect=BnkError("build failed")), \
             patch("bnk.runtime.install.start") as restart:
            with self.assertRaisesRegex(BnkError, "build failed"):
                change_plugins(name="example")
        self.assertEqual((original / "__init__.py").read_text(), "original")
        self.assertEqual(json.loads((self.runtime / "runtime.json").read_text()), metadata)
        restart.assert_called_once()
        self.assertEqual(list((self.root / "data/bnk").glob(".plugins-*")), [])

    def test_plugin_validation_rejects_native_library_that_did_not_load(self):
        from bnk.runtime.plugins import validate_plugins
        (self.runtime / "runtime.json").write_text(json.dumps({"plugins": [
            {"name": "native", "build": "cmake", "artifacts": ["plugins/native.so"]}]}))
        with patch("bnk.runtime.plugins.health", return_value={"native.so": False}), \
             patch("bnk.runtime.plugins.time.monotonic", side_effect=[0, 11]):
            with self.assertRaisesRegex(BnkError, "native"):
                validate_plugins(self.runtime, 12345)

    def test_failed_stop_releases_maintenance(self):
        from bnk.runtime.install import change_plugins
        from knife.sessions import SessionStore
        from tests.test_sessions import FakeView

        binary = self.root / "binary"
        binary.touch()
        sessions = SessionStore(lambda *args, **kwargs: FakeView())
        (self.runtime / "runtime.json").write_text(json.dumps({"format": 2, "plugins": [
            {"name": "example", "repo": "example", "ref": "main", "deps": [],
             "build": "python", "artifacts": ["plugins/example"]}]}))
        with patch("bnk.runtime.install.supervisor_pid", return_value=123), \
             patch("bnk.runtime.install.stop", side_effect=BnkError("stop failed")), \
             patch("bnk.runtime.install.start"), \
             patch("bnk.runtime.install.request", side_effect=lambda endpoint, action, args=None:
                   sessions.maintenance(None, args or {})):
            with self.assertRaisesRegex(BnkError, "stop failed"):
                change_plugins(name="example")
        sessions.open(None, {"path": str(binary)})

    def test_failed_validation_preserves_previous_installation(self):
        (self.runtime / "previous").write_text("keep")
        with patch("bnk.runtime.install.check_platform"), \
             patch("bnk.runtime.install.start", side_effect=BnkError("startup failed")), \
             patch("bnk.runtime.install.stop", return_value=False):
            with self.assertRaises(BnkError):
                install(self.prepared_archive(), report=lambda text: None)
        self.assertEqual((self.runtime / "previous").read_text(), "keep")
        self.assertEqual(list((self.root / "data/bnk").glob(".install-*")), [])

    def test_failed_activation_rolls_back_previous_installation(self):
        (self.runtime / "previous").write_text("keep")
        with patch("bnk.runtime.install.check_platform"), \
             patch("bnk.runtime.install.start", side_effect=[None, BnkError("port occupied")]), \
             patch("bnk.runtime.install.validate_plugins"), \
             patch("bnk.runtime.install.stop", return_value=False):
            with self.assertRaises(BnkError):
                install(self.prepared_archive(), report=lambda text: None)
        self.assertEqual((self.runtime / "previous").read_text(), "keep")


if __name__ == "__main__":
    unittest.main()
