# binja-knife

a sharp, stateful cli for binary ninja.

`bnk` keeps analyzed binaries open between commands. Use it headlessly or with an existing Binary Ninja installation.

```sh
bnk open ./program
bnk find strings 'parse failed' --refs
bnk inspect 0x401234
bnk code main
bnk save analysis.bndb
```

With one session, commands select it automatically. Use `-s NAME` for several sessions. Run `bnk -h` for commands and `bnk COMMAND -h` for options.

## Install

```sh
uv tool install .
bnk runtime install ./binaryninja-linux.tar.zst
```

Supply your own Linux Binary Ninja archive. The runtime starts automatically when needed. See [runtime setup](doc/runtime.md) for requirements, plugins, bundles, and existing installations.

## Python

Use the Binary Ninja API for composed analysis:

```sh
bnk eval 'len(bv.functions)'
bnk exec 'result = bv.arch.name'
bnk run analysis.py -- arg1 arg2
```

Scripts share the session's `bv`; edits remain available to later commands.

## Agents and development

The [agent skill](skills/binaryninja-knife/SKILL.md) includes API references. Link it with `./scripts/link-skill [SKILL_DIRECTORY]`.

See [development](doc/development.md) for checks and [architecture](doc/architecture.md) for the client/plugin split.
