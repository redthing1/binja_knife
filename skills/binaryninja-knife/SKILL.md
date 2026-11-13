---
name: binaryninja-knife
description: Drive Binary Ninja through bnk retained sessions and use version-matched API references for custom analysis.
---

# Binary Ninja Knife

Use `bnk -h` for commands and `bnk COMMAND -h` for options. Commands operate on retained Binary Ninja views; headless use is supported.

## Open and select

```sh
bnk open ./program
bnk summary
bnk open ./other-program -s other
```

With one session, commands select it automatically. With several, use `-s NAME` or `BNK_SESSION`. Reopening a path reuses its session; an unused name creates an independent view.

Use `open PATH --list-views` to discover view types and `--view NAME` for a specific choice. An explicit view must match on reuse. Saving preserves the selected view.

Paths normally resolve on the client. Use `--server-path` for absolute paths visible only to the plugin and `--connect HOST:PORT` for another server.

For a local runtime, use `bnk runtime install ARCHIVE`. Ordinary commands start it as needed. `runtime status`, `logs`, and `plugins` inspect its state; close sessions before changing plugins. See [runtime setup](https://github.com/redthing1/binja_knife/blob/main/doc/runtime.md) for installation and updates.

## Read and edit

```sh
bnk find strings 'parse failed' --refs
bnk inspect 0x401234
bnk refs 0x401234
bnk code main
bnk code main --level mlil --ssa
```

Results provide addresses and names for subsequent commands. `sections` and `segments` show mappings; `inspect --vars` shows variables. `code` defaults to HLIL; a name reads the whole function and an address focuses on that location. `refs --from` follows outgoing references.

```sh
bnk edit parse_packet --name parse_request
bnk edit parse_request --type 'bool parse_request(Request *req)'
bnk edit parse_request::len --name length --type size_t
bnk save analysis.bndb
```

Use `function::#IDENTIFIER` when variable names collide. `patch` changes bytes; `save` preserves analysis and `export` writes binary bytes. Save or explicitly discard changes before closing a dirty session.

## Python and API references

Use Python for composed or specialized analysis:

```sh
bnk eval 'len(bv.functions)'
bnk exec 'result = bv.arch.name'
bnk run analysis.py -- arg1 arg2
```

Each request gets `bn`, `bv`, `session`, `args`, a request-local `print`, and an optional final `result`. Edits remain in the view. `run` sends local source; `run --server` reads a plugin-visible script.

Before using unfamiliar Binary Ninja APIs, read [references/docs-guide.md](references/docs-guide.md) and the relevant module page. Check the reference version against `bnk status` and confirm signatures, mutation behavior, and analysis completion.
