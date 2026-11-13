# Analysis workflow

During sustained reversing, keep the analysis database and working knowledge current as understanding improves. Follow the investigation where the evidence leads and incorporate the user's steering into that work.

## Evidence and confidence

Distinguish observations from interpretations. A field used as an index establishes a constraint; its domain meaning may still be uncertain. Record what supports a proposed name or type and what would settle the remaining question.

Use descriptive names when a role is clear. Where understanding is partial, retain useful placeholders, apply only the known parts of a type, and explain uncertainty in notes or a concise comment. Revisit annotations when new evidence changes the interpretation.

## Database annotations

- Name functions and variables for their roles in the program.
- Recover signatures and data layouts from callers, field accesses, and other uses. Check pointer widths, signedness, and calling conventions against the target platform.
- Prefer reusable named structures, enums, and typedefs when several locations share a layout or meaning.
- Comment on non-obvious behavior, side effects, state transitions, constants, and established offsets.
- Use tags for durable triage and navigation. Inspect existing tag types and reuse a small vocabulary; put detailed explanations in comments or notes.
- Add user references for relationships Binary Ninja missed, including computed and table-driven references. Create missed functions when the code start and platform are supported by evidence.

Inspect before changing an annotation. Verify afterward by querying the stored state and, where relevant, rereading the affected IL, callers, and data uses. A clearer decompilation should remain consistent with the underlying evidence.

Use `edit` for ordinary names, types, and comments. Named type recovery, tags, user references, and function creation are available through Python; check the relevant APIs before using them.

## Working notes

Use the project's existing `notes/` organization. Group findings by subsystem, format, protocol, object layout, or investigation thread. Keep related topics linked and terminology consistent with the database.

A useful note records:

- Established facts with addresses, current symbol names, offsets, or other stable anchors.
- The evidence that supports those facts and why it matters.
- Hypotheses and unresolved questions, clearly distinguished from conclusions.
- Specific next pivots that would advance the investigation.

Summarize command results instead of pasting a transcript. Keep enough context to resume without repeating discovery. A small question may need only an update to an existing note; larger investigations benefit from focused topic files.

## Checkpoints and continuity

Save after a coherent set of annotations or a useful analysis milestone. Use `bnk save analysis.bndb` for the first database and `bnk save` for subsequent checkpoints. When persistence is part of the task, verify that the saved database reopens with the intended view and annotations.

Use `export` when binary bytes are the desired artifact. Coordinate changes to shared views, preserve existing work, and explicitly save or discard changes before closing a dirty session.
