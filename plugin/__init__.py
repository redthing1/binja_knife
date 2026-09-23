from __future__ import annotations

import traceback

import binaryninja as bn

from .knife.controller import Controller

controller = Controller()

try:
    controller.autostart()
except Exception:
    bn.log_error(f"Knife server failed to start:\n{traceback.format_exc()}")
