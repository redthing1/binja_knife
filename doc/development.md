# Development

Requires Python 3.11+ and [uv](https://docs.astral.sh/uv/).

```sh
uv sync --locked
uv run --locked bnk -h
uv run --locked python -m unittest discover -s tests -t . -v
```

The pure suite tests client, transport, and session behavior without importing Binary Ninja. Check API semantics in a matching Binary Ninja environment, including complete edit/save/reopen workflows.

## Runtime checks

With port 18812 free:

```sh
uv run --locked python scripts/check-runtime ./binaryninja-linux.tar.zst
```

The check uses temporary XDG directories and tests analysis, persistence, plugin updates, native load rejection, process recovery, and offline bundles. It requires Git, CMake, and C/C++ compilers. Original archives and prepared bundles are accepted.

`KNIFE_REPO` selects the Git repository used for Knife; setup resolves its `main` branch.

## Build

```sh
uv build
```

## Native dependencies

`src/bnk/runtime/defaults/libraries/` pins Ubuntu 24.04 packages and checksums for each supported architecture. Refresh with:

```sh
uv run --script scripts/refresh-runtime-libraries
```

Review the manifest diff and run the runtime check. Packages are extracted without running setup scripts. Binary Ninja supplies Qt and Python; the host supplies glibc. Preserve the Xvfb relocation and dependency checks when updating packages.
