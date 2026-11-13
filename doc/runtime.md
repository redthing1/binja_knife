# Local runtime

```sh
bnk runtime install ./binaryninja-linux.tar.zst
bnk open ./program
```

Supply your own Linux Binary Ninja ZIP or tar archive with bundled Python. Setup requires Linux x86-64 or AArch64, glibc 2.39+, `/bin/sh`, `git`, `uv`, `zstd`, and network access. Installation prepares and checks the runtime before replacing any previous installation, then starts it on `127.0.0.1:18812`.

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

A prepared bundle installs offline on another compatible system of the same architecture with `zstd`. It preserves the application, plugin versions, dependencies, and any license stored in the installation. Logs and analysis sessions are excluded.

## Plugins

Knife and the [default plugins](../src/bnk/runtime/defaults/plugins.manifest) resolve `main` when preparing an original archive. Startup preserves the installed versions. Inspect, add, or explicitly update plugins with:

```sh
bnk runtime plugins
bnk runtime plugins add https://example.org/team/plugin.git
bnk runtime plugins add https://example.org/team/native-plugin.git --build cmake
bnk runtime plugins update plugin
bnk runtime plugins update
```

The inventory shows configured refs, installed commits, artifacts, and current load state. Updates require all sessions to be closed. They stop the runtime, prepare replacements in staging, check that every managed plugin loads, and restart with the new installation. Failures preserve the previous installation and restart it. Validation output is retained beside `bnk runtime logs` as `install.log`.

Python plugins install their repository as a plugin directory. `--ref REF` selects a Git ref; repeat `--dep PACKAGE` for additional dependencies. Plugin `requirements.txt` files and configured dependencies are resolved together into a fresh shared Python package directory whenever Python plugins change.

Native plugins use `--build cmake` and require CMake, a build tool, and the compilers and dependencies required by their project. Bnk checks out the SDK revision named by the installed Binary Ninja's `api_REVISION.txt` and passes `BN_API_PATH`, `BN_INSTALL_DIR`, and `BN_USER_PLUGINS_DIR` to CMake. The project's install rules must put its plugin libraries and resources under `BN_USER_PLUGINS_DIR`; the standard `bn_install_plugin` helper does this for libraries. The SDK is cached by commit. Prepared bundles need no SDK or compiler.

Override the initial plugin list with `bnk runtime install ARCHIVE --plugins PATH`:

```text
<repo> [ref] [deps=a,b] [build=python|cmake]
```

The default ref is `main` and build method is `python`. Blank lines and `#` comments are ignored. An empty manifest installs only Knife. `KNIFE_REPO` overrides the Knife source repository.

## Storage

| Default location | Contents | Override |
| --- | --- | --- |
| `~/.local/share/bnk/runtime` | Application, libraries, plugins | `XDG_DATA_HOME` |
| `~/.local/state/bnk` | Binja profile, logs, process state | `XDG_STATE_HOME` |
| `~/.cache/bnk/packages` | Downloaded native packages | `XDG_CACHE_HOME` |
| `~/.cache/bnk/binaryninja-api` | Native plugin SDKs | `XDG_CACHE_HOME` |

Profile links and settings are regenerated on startup so the runtime can move. The profile is separate from desktop Binary Ninja settings.

## Existing installations

Link or copy [`plugin/`](../plugin/) into Binary Ninja's plugin directory as `knife_server`. It starts the server automatically. Select a remote server with `--connect HOST:PORT`; use `--server-path` for absolute paths visible only to that server.
