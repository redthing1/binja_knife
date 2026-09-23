# Development

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```sh
uv sync --locked
uv run --locked bnk -h
```

Run the pure client, transport, server, and session suite with:

```sh
uv run --locked python -m unittest discover -s tests -t . -v
```

Test discovery begins at `tests/` so an ordinary Python environment does not import Binary Ninja. These tests cover behavior owned by bnk: framing, session state, CLI shape, rendering, concurrency, and the fresh scripting namespace.

Binary Ninja semantics must also be checked in a real matching environment. Use a few complete retained journeys rather than recreating Binary Ninja with mocks:

```text
summary -> sections -> segments
open -> find strings --refs -> inspect -> code
edit -> undo -> redo -> save -> close -> reopen
exec/run -> patch -> undo -> save -> export
```

The plugin metadata currently targets Binary Ninja build 9757, and the repository skill carries the matching 5.3 API documentation.

Build both distributions with:

```sh
uv build
```

## Source layout

```text
src/bnk/   CLI, endpoint parsing, protocol, client, and text rendering
plugin/    self-contained Binary Ninja plugin and retained session state
tests/     pure tests that do not import Binary Ninja
skills/    agent guidance and the version-matched Binary Ninja API mirror
doc/       public project documentation
```

Keep the CLI and plugin independent. The plugin may use Binary Ninja and the standard library; the client may use Typer and the standard library. Keep tests behavioral and small. Add a direct command only when a recurring workflow is materially better than a short Binary Ninja script.
