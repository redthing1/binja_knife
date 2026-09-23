---
name: binaryninja-knife
description: Drive Binary Ninja through the bnk CLI using retained headless sessions, and consult version-matched Binary Ninja API docs when working with unfamiliar APIs.
---

# Binary Ninja Knife

Use `bnk` to work with Binary Ninja from the command line. The Binary Ninja plugin owns retained `BinaryView` sessions, so short client commands operate on the same analyzed state.

## Start with the CLI

Run `bnk -h` for the implemented command map and `bnk COMMAND -h` for exact syntax. Use the available commands as shown rather than guessing command names or options.

The workbench is organized by intent:

- connection and sessions: `status`, `version`, `open`, `sessions`, `summary`, `close`;
- understanding: `find`, `inspect`, `code`, `refs`, `sections`, `segments`;
- common changes: `edit`, `patch`, `undo`, `redo`, `save`, `export`;
- unrestricted Binary Ninja Python: `eval`, `exec`, `run`.

Commands return concise text designed for the operation.

## Sessions and paths

With one ready session, view commands select it automatically. With several, use `-s NAME` or `BNK_SESSION`.

```sh
bnk open ./program
bnk summary

bnk open ./other-program -s other
bnk summary -s other
```

Binary, database, and export paths are ultimately used by the Binary Ninja plugin. An ordinary path is first resolved and validated by the client, which is convenient when both sides share paths. Use `--server-path` for an absolute path visible only to Binary Ninja, such as a different container mount:

```sh
bnk open /targets/program --server-path -s program
```

Opening the same path normally reuses its retained session. An explicit unused name may intentionally open an independent view of the same path. Several sessions and requests may coexist in one Binary Ninja process; do not assume a container-per-session model.

Headless use is normal; a GUI is not assumed.

## Follow evidence directly

The ordinary reading loop is intentionally short:

```sh
bnk summary
bnk sections
bnk segments
bnk find strings 'parse failed' --refs
bnk refs 0x401020
bnk inspect 0x400800
bnk code 0x400800
bnk code main
bnk code main --level mlil --ssa
bnk code main --at 0x400800
```

`summary` gives compact view and analysis orientation, including useful inventory counts. `sections` shows logical regions; `segments` shows virtual ranges, file mappings, and permissions.

`find` lists strings, functions, or symbols without a query and filters them when a query is supplied; exact bytes require a pattern. A result address or name is meant to feed directly into `inspect`, `refs`, `code`, or `edit`.

`inspect` keeps the requested address visible and shows containing instruction, string, or data anchors when relevant. `code FUNCTION` reads a function from the start; `code ADDRESS` focuses on that instruction, including addresses inside its bytes. HLIL is the default, with MLIL, LLIL, and native disassembly available through `--level`. `refs` keeps exact-address results separate from any referenced containing anchor. `refs --from` reads an instruction site or a whole named function, including possible call sites without resolved targets; at a numeric function entry it shows both scopes separately.

Function inspection shows parameters and a local count. Use `bnk inspect main --vars` for a bounded variable inventory, or inspect a specific `main::variable`. Exact `function::#IDENTIFIER` targets remain available when names collide.

Use `edit` for ordinary durable annotations and `patch` for raw bytes:

```sh
bnk edit parse_packet --name parse_request
bnk edit parse_request --type 'bool parse_request(Request *req)'
bnk edit 0x401234 --comment 'rejects malformed length'
bnk edit parse_request::len --name length --type size_t
bnk patch 0x401234 '90 90'
bnk undo
bnk save analysis.bndb
bnk export patched.bin
```

Comments report whether they were stored in function or view scope. `save` preserves analysis in a BNDB, while `export` writes current binary bytes.

## Use Python for real programs

Do not force composed, specialized, or uncommon work through direct commands. Use the unrestricted scripting surface:

```sh
bnk eval 'len(bv.functions)'
bnk exec 'print(bv.entry_point); result = bv.arch.name'
bnk exec - < analysis_snippet.py
bnk run analysis.py -- arg1 arg2
bnk run /mounted/analysis.py --server -- arg1
```

Each request receives a fresh namespace with `bn`, the selected `bv`, `session`, `args`, request-local `print`, and an optional final value named `result`. A normal `run` transmits local source and needs no shared filesystem; `--server` reads the path on Binary Ninja's side. Scripts are unrestricted and changes remain in the retained view.

## Binary Ninja API documentation

The bundled documentation mirrors the Binary Ninja 5.3 Python API. Before writing a script that uses an unfamiliar Binary Ninja API—or changing bnk's plugin—read [references/docs-guide.md](references/docs-guide.md) and search the relevant vendored module page. Use it to confirm names, signatures, return values, and mutation behavior instead of guessing from memory.

CLI syntax comes from `bnk -h`; Binary Ninja Python semantics come from the bundled API docs.
