# Working on bnk

- Read `README.md` and `doc/architecture.md` for the product shape; use `bnk -h` for current command syntax.
- Keep the client and plugin independent, the CLI text-first, and direct commands focused on common primitives. Use Python for composed analysis.
- For unfamiliar Binary Ninja APIs, consult `skills/binaryninja-knife/references/docs-guide.md` and the matching API page. Use `doc/development.md` for testing.
- Keep tests purposeful and small; validate Binary Ninja behavior in a real environment when that matters.
