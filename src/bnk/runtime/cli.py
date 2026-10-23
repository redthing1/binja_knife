from __future__ import annotations

import tarfile
import zipfile
from collections import deque
from pathlib import Path
from typing import Annotated, Never

import typer

from bnk.client import BnkError
from bnk.runtime.paths import log_path, runtime_dir, state_dir

app = typer.Typer(
    help="Install and manage the local Binary Ninja runtime.",
    no_args_is_help=True,
    add_completion=False,
    context_settings={"help_option_names": ["-h", "--help"]},
)


def _fail(error: Exception) -> Never:
    typer.echo(f"error: {error}", err=True)
    raise typer.Exit(1)


@app.command()
def install(
    archive: Annotated[Path, typer.Argument(help="Your Binja archive or a prepared runtime bundle.")],
    plugins: Annotated[Path | None, typer.Option(help="Plugin manifest (defaults follow main).")] = None,
    license_file: Annotated[Path | None, typer.Option(help="License file if absent from the archive.")] = None,
) -> None:
    """Install, check, and start a local runtime."""
    from bnk.runtime.install import install as install_runtime
    try:
        destination = install_runtime(archive, plugins=plugins, license_file=license_file,
                                      report=lambda text: typer.echo(text, err=True))
        typer.echo(f"Runtime ready at {destination}")
    except (BnkError, OSError, ValueError, tarfile.TarError, zipfile.BadZipFile) as error:
        _fail(error)


@app.command()
def status() -> None:
    """Show installation and process state without starting anything."""
    from bnk.runtime.process import probe, supervisor_pid
    if not (runtime_dir() / "runtime.json").is_file():
        typer.echo("No local runtime installed. Use bnk runtime install ARCHIVE.")
        return
    pid = supervisor_pid(state_dir())
    state = "stopped" if pid is None else "ready" if probe() else "starting or restarting"
    typer.echo(f"runtime  {runtime_dir()}\nstate    {state}\nlog      {log_path()}")
    if pid is not None:
        typer.echo(f"pid      {pid}")


@app.command()
def logs(
    lines: Annotated[int, typer.Option("--lines", "-n", min=1, help="Number of recent lines.")] = 80,
) -> None:
    """Show recent runtime output."""
    try:
        with log_path().open(errors="replace") as handle:
            typer.echo("".join(deque(handle, maxlen=lines)), nl=False)
    except FileNotFoundError:
        typer.echo("No runtime log yet.")
    except OSError as error:
        _fail(error)


@app.command()
def stop() -> None:
    """Stop the runtime, discarding its in-memory sessions."""
    from bnk.runtime.process import lock, stop as stop_runtime
    try:
        with lock(state_dir()):
            stopped = stop_runtime()
        typer.echo("Runtime stopped." if stopped else "Runtime is already stopped.")
    except (BnkError, OSError) as error:
        _fail(error)


@app.command()
def pack(
    archive: Annotated[Path, typer.Argument(help="Destination .tar.zst (includes the bundled license).")],
) -> None:
    """Package the installed runtime for offline installation elsewhere."""
    from bnk.runtime.install import pack as pack_runtime
    try:
        pack_runtime(archive)
        typer.echo(f"Packed {archive}")
    except (BnkError, OSError, ValueError, tarfile.TarError) as error:
        _fail(error)
