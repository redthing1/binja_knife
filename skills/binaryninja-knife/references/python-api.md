# Python API patterns

Use Python for custom correlation, reusable passes, and operations beyond the direct commands. Keep each pass tied to a question and a selected set of targets.

## Execution

```sh
bnk eval 'len(bv.functions)'
bnk exec - < analysis.py
bnk run analysis.py -- arg1 arg2
```

Code runs in the selected session with `bn`, `bv`, `session`, `args`, and a request-local `print`. `session` contains the session name and path. `args` holds the supplied strings; `__file__` identifies the script.

Each invocation has a fresh Python namespace. Edits to the retained BinaryView remain available to later commands. `eval` returns its expression value; `exec` and `run` return `result` when set. `run` transmits local source; `run --server` reads a plugin-visible path.

Return concise findings or before/after summaries using addresses, names, and type text. Bound displayed collections and write large results to project files.

## Resolve targets and traverse IL

Use integer addresses internally and distinguish a function entry from an interior address:

- `bv.get_function_at(addr)` finds a function starting exactly there.
- `bv.get_functions_containing(addr)` finds functions whose bodies contain it.
- Name lookups may return several matches; resolve ambiguity before mutation.

Iterating a `HighLevelILFunction` yields basic blocks. Use its `instructions` iterator for instructions and `root.lines` for rendered structured text. Select functions before requesting their IL.

For references, distinguish incoming uses of an address from targets referenced by an instruction. Confirm the direction and code/data scope of the API being used.

## Mutate and verify

Inspect the existing annotation, apply the intended user change, and query the result. Some mutations are asynchronous or change later analysis. Use `update_analysis_and_wait()` when the following verification needs updated analysis.

For example, a script applying a recovered signature can check target identity and report the result:

```python
matches = bv.get_functions_by_name(args[0])
if len(matches) != 1:
    raise ValueError("expected one function; resolve the target first")
func = matches[0]
before = str(func.type)
func.set_user_type(args[1])
bv.update_analysis_and_wait()
result = {
    "address": hex(func.start),
    "before": before,
    "after": str(func.type),
}
```

Supply a complete C declaration, including the function name. Verify its consequences in the affected code and save with `bnk save` at a checkpoint.

For unfamiliar calls, use the [documentation guide](docs-guide.md). The [BinaryView](binja-docs/binaryview.md), [Function](binja-docs/function.md), and [IL](binja-docs/highlevelil.md) references cover target lookup, annotations, and traversal. Check user/auto behavior and analysis requirements, and reuse the APIs already grounded for the investigation.
