# Local runtime

```sh
bnk runtime install ./binaryninja-linux.tar.zst
bnk open ./program
```

Supply a Linux Binary Ninja ZIP or tar archive with bundled Python. Setup requires x86-64 or AArch64, glibc 2.39+, `sh`, Git, uv, zstd, and network access.

Use `--license-file PATH` if the archive lacks a license. `BN_LICENSE` overrides it at startup without being saved.

## Operation

```sh
bnk runtime status
bnk runtime logs
bnk runtime stop
```

Ordinary commands start the runtime as needed. Binary Ninja runs under Xvfb and restarts after crashes. Save before stopping; shutdown discards in-memory sessions. Stop the runtime before reinstalling.

Use `bnk open PATH --list-views` to inspect view types and `--view NAME` to choose one. Saved databases retain that choice.

## Plugins

```sh
bnk runtime plugins
bnk runtime plugins add REPO
bnk runtime plugins add REPO --build cmake
bnk runtime plugins update NAME
```

`REPO` accepts a Git URL or local checkout. Inventory shows installed names, sources, commits, and load state. Omit `NAME` to update all plugins. Close all sessions before changing plugins; replacements are validated before activation.

[Default plugins](../src/bnk/runtime/defaults/plugins.manifest) resolve `main` during installation and explicit updates. Startup preserves installed versions. Use `--ref REF` to pin an added plugin.

Python plugins install as directories. Their `requirements.txt` files and any `--dep PACKAGE` options resolve together in the bundled Python environment.

Native builds require CMake and the project's compilers and dependencies. Bnk supplies `BN_API_PATH`, `BN_INSTALL_DIR`, and `BN_USER_PLUGINS_DIR` using the SDK pinned by `api_REVISION.txt`. Install rules must target `BN_USER_PLUGINS_DIR`; Binary Ninja's `bn_install_plugin` helper supports this.

To customize initial setup, pass `--plugins FILE` with manifest entries:

```text
<repo> [ref] [deps=a,b] [build=python|cmake]
```

Blank lines and comments are ignored. An empty manifest installs only Knife.

## Bundles and storage

```sh
bnk runtime pack ./runtime.tar.zst
bnk runtime install ./runtime.tar.zst
```

Bundles install offline on compatible systems of the same architecture. They include plugins, dependencies, and any stored license; logs and analysis sessions are excluded.

| Default path | Contents | Override |
| --- | --- | --- |
| `~/.local/share/bnk/runtime` | Application and plugins | `XDG_DATA_HOME` |
| `~/.local/state/bnk` | Profile, logs, process state | `XDG_STATE_HOME` |
| `~/.cache/bnk` | Native packages and SDKs | `XDG_CACHE_HOME` |

## Existing installations

Link or copy [`plugin/`](../plugin/) into Binary Ninja's plugin directory as `knife_server`; the server starts automatically.

Use `--connect HOST:PORT` or `BNK_CONNECT` for another endpoint. These bypass local startup. When filesystems differ, `--server-path` accepts an absolute path visible to the plugin.
