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
from bnk.runtime.install import install, plugin_spec, unpack
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
        (self.runtime / "runtime.json").write_text('{"format": 1}')
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

    def test_plugin_manifest_defaults_to_main_and_supports_docker_syntax(self):
        self.assertEqual(plugin_spec("https://example.test/plugin.git"),
                         ("https://example.test/plugin.git", "main", []))
        self.assertEqual(plugin_spec("https://example.test/plugin.git main deps=msgpack,foo"),
                         ("https://example.test/plugin.git", "main", ["msgpack", "foo"]))
        self.assertEqual(plugin_spec("repo deps=msgpack"), ("repo", "main", ["msgpack"]))
        with self.assertRaises(ValueError):
            plugin_spec("repo main unexpected")

    def prepared_archive(self):
        source = self.root / "bundle.tar"
        with tarfile.open(source, "w") as archive:
            item = tarfile.TarInfo("runtime/runtime.json")
            content = b'{"format": 1}'
            item.size = len(content)
            archive.addfile(item, io.BytesIO(content))
        return source

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
             patch("bnk.runtime.install.stop", return_value=False):
            with self.assertRaises(BnkError):
                install(self.prepared_archive(), report=lambda text: None)
        self.assertEqual((self.runtime / "previous").read_text(), "keep")


if __name__ == "__main__":
    unittest.main()
