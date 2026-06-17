from __future__ import annotations

try:
    import binaryninja as bn
except ModuleNotFoundError:
    bn = None

from .constants import PLUGIN_NAME


def register_plugin_commands(bn_module) -> None:
    from .controller import controller
    from .log import info

    bn_module.PluginCommand.register(
        f"{PLUGIN_NAME}\\Start server",
        f"Start the {PLUGIN_NAME} RPyC server.",
        controller.start_server,
        controller.can_start_server,
    )

    bn_module.PluginCommand.register(
        f"{PLUGIN_NAME}\\Stop server",
        f"Stop the {PLUGIN_NAME} RPyC server.",
        controller.stop_server,
        controller.can_stop_server,
    )

    bn_module.PluginCommand.register(
        f"{PLUGIN_NAME}\\Status",
        f"Show {PLUGIN_NAME} status (host/port/running/sessions).",
        controller.show_status,
    )

    info("plugin loaded")


if bn is not None:
    register_plugin_commands(bn)
