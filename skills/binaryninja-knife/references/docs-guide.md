# Binary Ninja Python API docs

Use this reference before an unfamiliar Binary Ninja Python API call. The mirror exists because method names, object relationships, mutation behavior, and analysis semantics are easy to misremember across releases.

## Version and location

The mirror records its API version in:

- `binja-docs/INDEX.md` records the version and module list;
- `binja-docs/.binja-docs.json` records the generated mirror metadata;
- `binja-docs/*.md` contains one page per `binaryninja` module.

Compare the mirror version with the runtime shown by `bnk status`. If the major/minor release differs, treat the mirror as orientation rather than exact authority and refresh it deliberately.

These pages document Binary Ninja Python. They do not document `bnk` command syntax; use `bnk -h` and leaf help for that.

## Find an API

Search the likely owning module first:

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

Read the signature and the surrounding property or method description. Check whether a value is an iterator, whether an operation is asynchronous, whether a mutation is user or auto state, and whether later reads require analysis to finish.

Once an API has been grounded for the current work, use it normally; repeated calls do not require ritual rereading.

## Refreshing the mirror

The maintainer refreshes the mirror deliberately when the targeted Binary Ninja release changes:

```sh
uv run --script references/binja-docs/sync.py --update-version
```

This adopts the version currently published by the official API site.
