# Binary Ninja Python API docs

Consult the included API documentation before writing or running Binary Ninja Python. Use documented calls rather than guessing from memory.

## Find and verify an API

The paths below are relative to the skill directory. Search the likely owning module first:

```sh
rg -n "get_code_refs\\(" references/binja-docs/binaryview.md
rg -n "set_user_type\\(" references/binja-docs/function.md
rg -n "from_identifier\\(" references/binja-docs/variable.md
```

If the owner is unclear, search the mirror:

```sh
rg -n "TagType\\b" references/binja-docs/*.md
```

Useful starting pages:

- `binaryview.md` — views, loading, sections, segments, symbols, references, data, comments, tags, and persistence;
- `function.md` — functions, types, variables, comments, callers/callees, and IL access;
- `highlevelil.md`, `mediumlevelil.md`, `lowlevelil.md` — IL trees, instructions, variables, and mappings;
- `types.md` and `typeparser.md` — types and declaration parsing;
- `variable.md` — variable identity, storage, naming, and typing;
- `filemetadata.md` and `database.md` — files, databases, undo, and save state;
- `mainthread.md` and `interaction.md` — GUI-sensitive work.

Read the relevant API entries, and reuse what you have already checked during the task. Look up additional APIs as needed.

If the included docs do not cover an API, consult the matching installed SDK source or official API documentation before using it. For `bnk` command syntax, use `bnk -h` and leaf help.

Recheck failed calls against the docs. Verify an API difference before diagnosing a version mismatch.

## Runtime and reference versions

The reference version and module list are recorded in `binja-docs/INDEX.md` and `binja-docs/.binja-docs.json`. Module pages are under `binja-docs/*.md`.

Compare the mirror version with the runtime shown by `bnk status`. If the major/minor release differs, treat the mirror as orientation rather than exact authority and refresh it deliberately.

## Refreshing the mirror

The maintainer refreshes the mirror deliberately when the targeted Binary Ninja release changes:

```sh
uv run --script references/binja-docs/sync.py --update-version
```

This adopts the version currently published by the official API site.
