from __future__ import annotations

import binaryninja as bn

from .constants import PLUGIN_NAME
from .controller import controller
from .log import info


bn.PluginCommand.register(
    f"{PLUGIN_NAME}\\Start server",
    f"Start the {PLUGIN_NAME} RPyC server.",
    controller.start_server,
    controller.can_start_server,
)

bn.PluginCommand.register(
    f"{PLUGIN_NAME}\\Stop server",
    f"Stop the {PLUGIN_NAME} RPyC server.",
    controller.stop_server,
    controller.can_stop_server,
)

bn.PluginCommand.register(
    f"{PLUGIN_NAME}\\Status",
    f"Show {PLUGIN_NAME} status (host/port/running/sessions).",
    controller.show_status,
)

info("plugin loaded")
