from __future__ import annotations

import json
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

plugins_app = typer.Typer(help="Install, update, and inspect runtime plugins.", invoke_without_command=True,
                          add_completion=False, context_settings={"help_option_names": ["-h", "--help"]})
app.add_typer(plugins_app, name="plugins")


@plugins_app.callback()
def plugins(context: typer.Context) -> None:
    """Show desired sources, installed versions, and current load state."""
    if context.invoked_subcommand:
        return
    from bnk.runtime.plugins import health, running
    from bnk.runtime.process import supervisor_pid
    try:
        metadata = json.loads((runtime_dir() / "runtime.json").read_text())
        loaded = health() if supervisor_pid(state_dir()) is not None else None
        for item in metadata["plugins"]:
            state = "stopped" if loaded is None else "running" if running(item, loaded) else "failed or unrecognized"
            typer.echo(f"{item['name']}  {state}\n  source  {item['repo']} @ {item['ref']}\n"
                       f"  commit  {item['commit']} ({item['build']})")
            if item.get("api_commit"):
                typer.echo(f"  api     {item['api_commit']}")
            typer.echo("  files   " + ", ".join(item["artifacts"]))
    except (BnkError, OSError, ValueError) as error:
        _fail(error)


@plugins_app.command("add")
def plugins_add(
    repo: Annotated[str, typer.Argument(help="Plugin Git repository.")],
    ref: Annotated[str, typer.Option(help="Git ref to resolve.")] = "main",
    build: Annotated[str, typer.Option(help="Build method: python or cmake.")] = "python",
    deps: Annotated[list[str] | None, typer.Option("--dep", help="Additional Python dependency; repeatable.")] = None,
) -> None:
    """Install and validate a plugin."""
    from bnk.runtime.plugins import PluginSpec
    from bnk.runtime.install import change_plugins
    try:
        change_plugins(spec=PluginSpec(repo, ref, deps or [], build), report=lambda text: typer.echo(text, err=True))
        typer.echo("Plugin ready.")
    except (BnkError, OSError, ValueError) as error:
        _fail(error)


@plugins_app.command("update")
def plugins_update(name: Annotated[str | None, typer.Argument(help="Installed name; omit to update all.")] = None) -> None:
    """Update one plugin or all configured refs."""
    from bnk.runtime.install import change_plugins
    try:
        change_plugins(name=name, report=lambda text: typer.echo(text, err=True))
        typer.echo("Plugins ready.")
    except (BnkError, OSError, ValueError) as error:
        _fail(error)


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
