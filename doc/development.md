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
edit -> save -> close -> reopen
exec/run -> patch -> save -> export
```

For the managed runtime, stop any server on port 18812 and run:

```sh
uv run --locked python scripts/check-runtime ./binja-runtime.tar.zst
```

This uses temporary XDG directories and real Binary Ninja processes to check analysis, view selection and persistence, both default plugins, plugin updates, native ABI rejection and rollback, concurrent startup, shutdown, crash recovery, and offline bundle relocation. It requires Git, CMake, and C/C++ compilers for the native fixture. It accepts an original Binja archive or a prepared bundle and cleans up its test server. Set `KNIFE_REPO` to a Git checkout containing the plugin revision under test.

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

## Runtime dependencies

`src/bnk/runtime/defaults/libraries/` records native packages and checksums from an Ubuntu 24.04 snapshot for each supported architecture. Snapshot URLs keep pinned versions available after the live archive removes them. Refresh it with `uv run --script scripts/refresh-runtime-libraries`, review the diff, and run the runtime check above. Installation extracts packages locally without running their setup scripts. Binary Ninja supplies Qt and Python; the host supplies glibc.

Xvfb's compiled `xkbcomp` path is relocated to its private working directory. The patch checks the original string and preserves ELF offsets. Keep this check and the dependency audit when updating packages. Plugin refs default to `main` and resolve separately at installation time.
