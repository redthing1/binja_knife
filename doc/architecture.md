# Architecture

The client sends one JSON request per TCP connection. The plugin executes an action against a retained Binary Ninja view and returns data for the client to render.

| Component | Owns |
| --- | --- |
| `src/bnk/` | CLI, transport, and text rendering |
| `plugin/knife/` | Binary Ninja views, sessions, and actions |
| `src/bnk/runtime/` | Optional local installation and process supervision |

The client does not import Binary Ninja. The plugin depends only on Binary Ninja and the standard library and can run independently of the managed runtime.

## Sessions

Opening a file selects a view, waits for analysis, and retains it under a name. An explicit view must match when reusing a session. Saving records the selected view in the database.

Session bookkeeping uses short locks; analysis and requests may overlap. Direct edits and saves share a per-session lock. A session in use cannot close. Plugin maintenance requires no open sessions and blocks new opens until replacement finishes.

## Actions

Direct commands cover common reading, editing, and persistence operations. Composed analysis uses `eval`, `exec`, or `run` in a fresh namespace with `bn`, `bv`, `session`, `args`, and `print`. Scripts can set `result` to return a value.

Binary Ninja objects stay in the plugin. Results contain addresses and names usable by subsequent commands; the client renders bounded lists and multiline code.

## Runtime

The managed runtime runs Binary Ninja under Xvfb. A failed default connection triggers startup; explicit endpoints bypass it. Interrupted requests are never replayed.

Archive installation and plugin updates share staged validation, activation, and rollback. Python plugins are copied; native plugins build through CMake with the installed core's SDK. Metadata records sources, commits, and artifacts. See [runtime setup](runtime.md) for operation.
