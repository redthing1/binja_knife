from __future__ import annotations

import json
import threading
from typing import Optional

import binaryninja as bn

from .constants import (
    DEFAULT_HOST,
    DEFAULT_PORT,
    DEFAULT_TIMEOUT,
    PLUGIN_NAME,
    SETTINGS_GROUP,
    SETTING_AUTOSTART,
    SETTING_HOST,
    SETTING_PORT,
    SETTING_TIMEOUT,
)
from .log import err, info, warn
from .service import (
    SESSIONS,
    KnifeServerService,
    clear_root_view,
    set_root_view_for_start,
    validate_service_imports,
)


class _ServerState:
    def __init__(self) -> None:
        self.thread: Optional[threading.Thread] = None
        self.server = None
        self.host = DEFAULT_HOST
        self.port = DEFAULT_PORT
        self.timeout = DEFAULT_TIMEOUT

    def running(self) -> bool:
        return (
            self.thread is not None
            and self.thread.is_alive()
            and self.server is not None
        )


STATE = _ServerState()


def _register_settings() -> None:
    settings = bn.Settings()
    if not settings.register_group(SETTINGS_GROUP, PLUGIN_NAME):
        return

    ignore_scopes = ["SettingsProjectScope", "SettingsResourceScope"]

    def reg(name: str, spec: dict) -> None:
        full = f"{SETTINGS_GROUP}.{name}"
        if settings.contains(full):
            return
        settings.register_setting(full, json.dumps(spec))

    reg(
        SETTING_AUTOSTART,
        {
            "title": "Auto Start",
            "description": "Automatically start the server when Binary Ninja opens",
            "type": "boolean",
            "default": False,
            "ignore": ignore_scopes,
        },
    )
    reg(
        SETTING_HOST,
        {
            "title": "TCP Listen Host",
            "description": "Interface the server should listen on",
            "type": "string",
            "default": DEFAULT_HOST,
            "ignore": ignore_scopes,
        },
    )
    reg(
        SETTING_PORT,
        {
            "title": "TCP Listen Port",
            "description": "TCP port the server should listen on",
            "type": "number",
            "minValue": 1,
            "maxValue": 65535,
            "default": DEFAULT_PORT,
            "ignore": ignore_scopes,
        },
    )
    reg(
        SETTING_TIMEOUT,
        {
            "title": "Request Timeout (seconds)",
            "description": "Timeout for synchronous RPyC requests in seconds",
            "type": "number",
            "minValue": 0,
            "maxValue": 86400,
            "default": DEFAULT_TIMEOUT,
            "ignore": ignore_scopes,
        },
    )


def _start_thread(host: str, port: int, timeout: int) -> None:
    import rpyc.utils.server  # type: ignore

    protocol_config = {
        "allow_public_attrs": True,
        "allow_all_attrs": True,
        "allow_getattr": True,
        "allow_setattr": True,
        "allow_delattr": True,
        "allow_pickle": True,
        "sync_request_timeout": None if timeout == 0 else timeout,
    }

    server = rpyc.utils.server.ThreadedServer(
        KnifeServerService,
        hostname=host,
        port=port,
        protocol_config=protocol_config,
    )
    STATE.server = server
    info(f"server started on {host}:{port} (timeout={timeout}s)")
    try:
        server.start()
    finally:
        info("server thread exiting")


class Controller:
    def __init__(self) -> None:
        _register_settings()
        self._maybe_autostart()

    def _maybe_autostart(self) -> None:
        settings = bn.Settings()
        key = f"{SETTINGS_GROUP}.{SETTING_AUTOSTART}"
        try:
            if settings.contains(key) and settings.get_bool(key):
                self.start_server(None)
        except Exception:
            pass

    def can_start_server(self, _bv) -> bool:
        return not STATE.running()

    def can_stop_server(self, _bv) -> bool:
        return STATE.running()

    def start_server(self, bv) -> None:
        if STATE.running():
            warn("server already running")
            return

        import_error = validate_service_imports()
        if import_error:
            err(f"cannot start: {import_error}")
            bn.show_message_box(
                PLUGIN_NAME,
                f"Failed to import required dependency (rpyc).\\n\\n{import_error}\\n\\n"
                "If you installed via the plugin manager, try restarting Binary Ninja. "
                "If developing via symlink, install rpyc into the Binary Ninja Python environment.",
                bn.MessageBoxButtonSet.OKButtonSet,
                bn.MessageBoxIcon.ErrorIcon,
            )
            return

        settings = bn.Settings()
        host = settings.get_string(f"{SETTINGS_GROUP}.{SETTING_HOST}") or DEFAULT_HOST
        port = int(
            settings.get_integer(f"{SETTINGS_GROUP}.{SETTING_PORT}") or DEFAULT_PORT
        )
        timeout = int(
            settings.get_integer(f"{SETTINGS_GROUP}.{SETTING_TIMEOUT}") or DEFAULT_TIMEOUT
        )

        STATE.host = host
        STATE.port = port
        STATE.timeout = timeout

        if bv is not None:
            set_root_view_for_start(bv)
        else:
            clear_root_view()

        thread = threading.Thread(
            target=_start_thread, args=(host, port, timeout), daemon=True
        )
        STATE.thread = thread
        thread.start()

    def stop_server(self, _bv) -> None:
        if not STATE.running():
            warn("server not running")
            return
        try:
            STATE.server.close()
        except Exception as exc:
            err(f"error closing server: {exc}")
        try:
            if STATE.thread:
                STATE.thread.join(timeout=3.0)
        except Exception:
            pass
        STATE.server = None
        STATE.thread = None
        info("server stopped")

    def show_status(self, _bv) -> None:
        running = STATE.running()
        sessions = SESSIONS.list_names()
        msg = (
            f"running={running} host={STATE.host} port={STATE.port} timeout={STATE.timeout}s "
            f"sessions={len(sessions)} {sessions}"
        )
        info(msg)


controller = Controller()
