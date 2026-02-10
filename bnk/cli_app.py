from __future__ import annotations

from typing import Optional

import typer


CONTEXT_SETTINGS = {"help_option_names": ["-h", "--help"]}


def make_app(*, name: Optional[str] = None, help: Optional[str] = None) -> typer.Typer:
    return typer.Typer(
        name=name,
        help=help,
        add_completion=False,
        no_args_is_help=True,
        context_settings=CONTEXT_SETTINGS,
        pretty_exceptions_short=True,
        pretty_exceptions_show_locals=False,
    )

