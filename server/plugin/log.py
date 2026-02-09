from __future__ import annotations

from binaryninja import log_debug, log_error, log_info, log_warn

from .constants import LOGGER_NAME


def info(msg: str) -> None:
    log_info(msg, logger=LOGGER_NAME)


def warn(msg: str) -> None:
    log_warn(msg, logger=LOGGER_NAME)


def err(msg: str) -> None:
    log_error(msg, logger=LOGGER_NAME)


def dbg(msg: str) -> None:
    log_debug(msg, logger=LOGGER_NAME)
