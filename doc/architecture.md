# Architecture

Bnk has two deliberately small sides:

```text
Typer client
  -> one request over TCP
  -> Binary Ninja plugin
  -> one named action
  -> purpose-built text
```

The client owns command-line parsing, connection handling, and presentation. It does not import Binary Ninja.

The plugin owns Binary Ninja objects and retained sessions. It is self-contained apart from Binary Ninja and the Python standard library; it does not import the client package.

Plugin actions follow the visible workbench rather than mirroring Binary Ninja's class tree: reading, common changes and persistence, and unrestricted Python. Specialized analysis stays in Python instead of accumulating wrapper commands.

## Sessions

`open` loads and analyzes a `BinaryView`, then retains it under a readable name. A command selects an explicit session, `BNK_SESSION`, or the sole ready session.

Several sessions and requests may coexist in one Binary Ninja process. Session bookkeeping uses short state locks but does not serialize Binary Ninja operations globally. Opening the same path normally reuses its session; an explicit unused name may create an independent view.

One narrow per-session lock groups a direct `edit` or `patch` into a coherent Binary Ninja undo entry and keeps save/undo history changes from interleaving. Reading and unrestricted Python do not pass through an operation lane.

## Transport

Each TCP connection carries one private newline-delimited JSON exchange; Binary Ninja objects stay in the plugin, and CLI commands render purpose-built text.

## Deployment

The command model does not depend on deployment topology. Client and plugin may run natively, in one container, or across a reachable host/container boundary. `--connect` selects the endpoint. Binary, database, and export paths are used by the plugin; the client normally resolves and validates them first, while `--server-path` accepts an absolute path visible only to the plugin.

The plugin starts its server automatically through three Binary Ninja settings: autostart, host, and port.

## Presentation and extension

The client renders each operation directly. Addresses and target identities remain usable as the next command. Inspection retains the requested address alongside containing anchors; code can focus on an instruction or show a whole function. Multiline code remains multiline, and bounded results say when more exists.

`eval`, `exec`, and `run` execute in a fresh namespace containing `bn`, `bv`, `session`, `args`, a request-local `print`, and the optional final value `result`. Client-side scripts send their source; `run --server` reads an explicit plugin-visible path. Script changes use normal Binary Ninja authority and remain in the retained view.
