---
name: binaryninja-knife
description: Use Binary Ninja through bnk for interactive analysis, database annotation, and custom Python workflows.
---

# Binary Ninja Knife

Use `bnk` to investigate binaries and improve their analysis. Named sessions retain a BinaryView between commands; saving a BNDB preserves the analysis on disk. Headless sessions are ordinary workspaces.

## Interface

| Surface | Commands | Purpose |
| --- | --- | --- |
| Sessions | `sessions`, `open`, `summary`, `close` | Retain, select, and inspect a workspace |
| Reading | `find`, `inspect`, `code`, `refs`, `sections`, `segments` | Find anchors, follow evidence, and read IL |
| Changes | `edit`, `patch`, `save`, `export` | Annotate, change bytes, and persist work |
| Python | `eval`, `exec`, `run` | Custom queries, related edits, and reusable passes |
| Connection and setup | `status`, `version`, `runtime` | Inspect the endpoint and manage a local runtime |

Use `bnk -h` for the command map and `bnk COMMAND -h` for exact syntax.

## References

- [Analysis workflow](references/workflow.md): read before beginning analysis. Covers annotation quality, confidence, notes, and checkpoints.
- [Python API patterns](references/python-api.md): read before Binary Ninja scripting. Covers execution context, target resolution, IL traversal, and verified mutations.
- [API documentation guide](references/docs-guide.md): read before scripting, then consult the included module pages for the APIs the script uses.
- [Runtime setup](https://github.com/redthing1/binja_knife/blob/main/doc/runtime.md): consult for installation, plugins, and remote endpoints.

Check the APIs used by `eval`, `exec`, and scripts in the included docs before execution. Reuse what you have already checked during the task.

## First moves

1. Run `bnk sessions` and reuse existing work on the target.
2. If needed, open it with `bnk open PATH -s NAME`. Let normal analysis finish.
3. Check `bnk summary -s NAME` for the path, view, architecture, platform, and analysis state.

With one ready session, commands select it automatically. With several, use `-s NAME` or `BNK_SESSION`. Use `open PATH --list-views` and `--view NAME` to choose a view; a separately named session can hold an independent interpretation for comparison.

Paths normally resolve on the client. `--server-path` accepts an absolute path visible only to the plugin; `--connect HOST:PORT` selects another server.

## Analysis workflow

For non-trivial reversing, improve two artifacts together:

- **BNDB:** names, types, comments, tags, user references, and recovered functions.
- **Notes:** evidence and open questions organized by subsystem or topic.

The working loop is:

1. Pick a question and a concrete anchor: a string, symbol, address, table, reference, or observed behavior.
2. Follow relevant references and functions with `find`, `inspect`, `refs`, and `code`.
3. Record findings and uncertainty; improve the database as the evidence supports it.
4. Verify conclusions and edits against the affected code and its callers or data uses.
5. Save the database at meaningful checkpoints.

Carry returned addresses and names into subsequent commands. Keep notes synchronized when names or conclusions change.

## IL choice and analysis gaps

Start with HLIL for function behavior. Use MLIL, LLIL, or disassembly when they answer a specific question about data flow, registers, instructions, lifting, or misleading decompiler output.

If HLIL is unavailable or implausible, inspect analysis state, skip reasons, function boundaries, and platform assumptions. Normal analysis can finish while individual functions are automatically skipped for complexity. Investigate relevant gaps individually and use the available representation where appropriate.

## Working practices

Keep investigation targeted. Searches, references, and inexpensive inventories help select useful functions before generating IL. Use result limits for exploration, then expand relevant results when the question requires complete coverage.

Avoid massive, unbounded sweeps over every function's HLIL, MLIL, or LLIL: they can be extremely slow. Give broader passes a concrete purpose, filter candidates, work in bounded groups, and retain useful results.

Inspect current state before editing and resolve ambiguous targets. Use evidence-backed names and types; keep hypotheses explicit. After type or boundary changes, wait for analysis as needed and recheck the resulting interpretation. Keep writes to a shared view sequential.

Use direct commands for common queries and edits, and Python for composed analysis or API-only operations. Python requests receive a fresh namespace; changes to the retained view persist.

Keep output focused and save large result sets in project artifacts. `save` preserves analysis; `export` writes binary bytes. Preserve the user's retained workspace and close temporary sessions when finished.
