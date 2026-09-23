# binja-knife

a sharp, stateful cli for binary ninja.

`bnk` keeps analyzed binaries alive between commands, turning the shell into a fast, continuous reversing workspace.

- retained, named sessions—headless by default
- focused tools for exploring and changing a binary
- unrestricted Binary Ninja Python when the workflow needs more

```sh
bnk open ./program
bnk summary
bnk find strings 'parse failed' --refs
bnk inspect 0x401234
bnk code main
```

With one open session, commands select it automatically. Use `-s NAME` when you want several.

## quick start

Install the client:

```sh
uv tool install .
bnk -h
```

Link or copy [`plugin/`](plugin/) into Binary Ninja's plugin directory as `knife_server`. The Knife Server starts automatically and works equally well headlessly, in a container, or alongside the GUI.

When the client and Binary Ninja see different filesystems, pass an absolute plugin-visible path with `--server-path`.

## full power, close at hand

The direct commands cover the everyday loop: orienting to the binary, reading its sections and segments, finding evidence, following references, reading IL, making common edits, patching bytes, and saving the result. `bnk -h` is the compact map.

For everything else, `eval`, `exec`, and `run` expose the real Binary Ninja Python API without giving up the retained session:

```sh
bnk eval 'len(bv.functions)'
bnk exec 'print(bv.entry_point); result = bv.arch.name'
bnk run analysis.py -- arg1 arg2
```

## agents

The repository includes an [agent skill](skills/binaryninja-knife/SKILL.md) with the matching Binary Ninja 5.3 API reference. Run `./scripts/link-skill` to link it into `~/.agents/skills/rt1_tools/`, or pass another skill directory.

## develop

Development notes live in [`doc/development.md`](doc/development.md). For the small client/plugin split, see [`doc/architecture.md`](doc/architecture.md).
