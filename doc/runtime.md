# Local runtime

```sh
bnk runtime install ./binaryninja-linux.tar.zst
bnk open ./program
```

Supply your own Linux Binary Ninja ZIP or tar archive with bundled Python. Setup requires Linux x86-64, glibc 2.39+, `/bin/sh`, `git`, `uv`, `zstd`, and network access. Installation prepares and checks the runtime before replacing any previous installation, then starts it on `127.0.0.1:18812`.

Use `--license-file PATH` if the archive lacks a license. `BN_LICENSE` takes precedence at startup and is not saved to disk.

## Operation

```sh
bnk runtime status
bnk runtime logs
bnk runtime stop
```

Ordinary commands start the installed runtime when needed. Explicit `--connect` or `BNK_CONNECT` endpoints bypass automatic startup. Runtime `status` and `logs` only inspect it.

Binary Ninja runs under a private Xvfb display and stays alive between commands, within the lifetime of the surrounding environment. Crashes restart with bounded backoff. Save work with `bnk save` before stopping or replacing the runtime; in-memory sessions are lost on shutdown or crash. Run `bnk runtime stop` before reinstalling.

## Portable bundles

```sh
bnk runtime pack ./binja-runtime.tar.zst
bnk runtime install ./binja-runtime.tar.zst
```

A prepared bundle installs offline on another compatible system with `zstd`. It preserves the application, plugin versions, dependencies, and any license stored in the installation. Logs and analysis sessions are excluded.

## Plugins

Knife and the [default plugins](../src/bnk/runtime/defaults/plugins.manifest) follow `main` when preparing an original archive. Resolved commits are recorded in `runtime.json`. Override the plugin list with `--plugins PATH`:

```text
<repo_url> [ref] [deps=<dependency1,dependency2,...>]
```

The default ref is `main`. Blank lines and `#` comments are ignored. An empty manifest installs only Knife. Dependencies and plugin `requirements.txt` files are installed into the bundled Python's private package directory. `KNIFE_REPO` overrides the Knife source repository.

## Storage

| Default location | Contents | Override |
| --- | --- | --- |
| `~/.local/share/bnk/runtime` | Application, libraries, plugins | `XDG_DATA_HOME` |
| `~/.local/state/bnk` | Binja profile, logs, process state | `XDG_STATE_HOME` |
| `~/.cache/bnk/packages` | Downloaded native packages | `XDG_CACHE_HOME` |

Profile links and settings are regenerated on startup so the runtime can move. The profile is separate from desktop Binary Ninja settings.

## Existing installations

Link or copy [`plugin/`](../plugin/) into Binary Ninja's plugin directory as `knife_server`. It starts the server automatically. Select a remote server with `--connect HOST:PORT`; use `--server-path` for absolute paths visible only to that server.
