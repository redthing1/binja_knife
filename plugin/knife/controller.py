from __future__ import annotations

import threading

import binaryninja as bn

from .changes import ChangeActions
from .reading import ReadActions
from .scripting import PythonActions
from .server import KnifeServer
from .sessions import SessionStore

SETTINGS_GROUP = "knife_server"
AUTOSTART = "knife_server.autostart"
HOST = "knife_server.host"
PORT = "knife_server.port"


class Controller:
    def __init__(self) -> None:
        self._lock = threading.Lock()
        self._server: KnifeServer | None = None
        self._thread: threading.Thread | None = None
        self._sessions = SessionStore(bn.load)
        self._reading = ReadActions(self._sessions)
        self._changes = ChangeActions(bn, self._sessions)
        self._python = PythonActions(bn, self._sessions)
        self._register_settings()
        self._register_commands()

    def autostart(self) -> None:
        if bn.Settings().get_bool(AUTOSTART):
            self.start()

    def start(self) -> None:
        with self._lock:
            if self._server is not None:
                bn.log_info(f"Knife server is already listening on {self.endpoint}")
                return
            settings = bn.Settings()
            server = KnifeServer(
                (settings.get_string(HOST), settings.get_integer(PORT)),
                binary_ninja_version=bn.core_version,
                log_error=bn.log_error,
                actions={
                    "sessions": self._sessions.list_sessions,
                    "open": self._sessions.open,
                    "summary": self._sessions.summary,
                    "close": self._sessions.close,
                    "find": self._reading.find,
                    "inspect": self._reading.inspect,
                    "code": self._reading.code,
                    "refs": self._reading.refs,
                    "sections": self._reading.sections,
                    "segments": self._reading.segments,
                    "edit": self._changes.edit,
                    "patch": self._changes.patch,
                    "save": self._changes.save,
                    "export": self._changes.export,
                    "eval": self._python.evaluate,
                    "exec": self._python.execute,
                    "run": self._python.run,
                },
            )
            thread = threading.Thread(target=server.serve_forever, name="knife-server", daemon=True)
            self._server = server
            self._thread = thread
            thread.start()
            bn.log_info(f"Knife server listening on {self.endpoint}")

    def stop(self) -> None:
        with self._lock:
            server = self._server
            thread = self._thread
            if server is None:
                bn.log_info("Knife server is not running")
                return
            server.shutdown()
            server.server_close()
            if thread is not None:
                thread.join()
            self._server = None
            self._thread = None
            bn.log_info("Knife server stopped")

    def show_status(self) -> None:
        with self._lock:
            if self._server is None:
                bn.log_info("Knife server is not running")
            else:
                bn.log_info(f"Knife server is listening on {self.endpoint}")

    @property
    def endpoint(self) -> str:
        if self._server is None:
            return "stopped"
        host, port = self._server.server_address[:2]
        return f"{host}:{port}"

    def _register_settings(self) -> None:
        settings = bn.Settings()
        settings.register_group(SETTINGS_GROUP, "Knife Server")
        settings.register_setting(
            AUTOSTART,
            '{"title":"Autostart","type":"boolean","default":true,'
            '"description":"Start the Knife server when Binary Ninja loads."}',
        )
        settings.register_setting(
            HOST,
            '{"title":"Host","type":"string","default":"127.0.0.1",'
            '"description":"Address for the Knife server to listen on."}',
        )
        settings.register_setting(
            PORT,
            '{"title":"Port","type":"number","default":18812,"minValue":1,"maxValue":65535,'
            '"description":"Port for the Knife server to listen on."}',
        )

    def _register_commands(self) -> None:
        bn.PluginCommand.register_global(
            "Knife\\Start Server", "Start the Knife server", self.start
        )
        bn.PluginCommand.register_global("Knife\\Stop Server", "Stop the Knife server", self.stop)
        bn.PluginCommand.register_global(
            "Knife\\Server Status", "Show the Knife server status", self.show_status
        )
