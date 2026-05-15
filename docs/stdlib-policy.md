# Python Standard Library Policy

Project-K targets Python `3.12.10` as the intended runtime. Agents must check the
actual `.python-version` and `pyproject.toml` before Python changes and report
any mismatch.

Agents must work from the project virtual environment before Python commands or
Python-dependent repo work. If `.venv` is missing, create it with
`uv venv --python 3.12.10`; on Windows PowerShell activate it with
`.venv\Scripts\activate`.

Use the standard library to simplify real code, not to decorate it. A stdlib
module belongs in the code only when it removes existing complexity, improves
correctness, or makes intent clearer.

## Evaluation Rule

Before adding or refactoring around a stdlib module:

1. Search for the concrete problem it solves.
2. Identify the file and code pattern.
3. Decide whether the stdlib version is simpler than the existing code.
4. Confirm it fits the current architecture.
5. Apply one library at a time and verify after each change.

If no real case exists, do not introduce the module.

## Library Fit Guide

- `dataclasses`: use for simple data records that currently have repetitive
  initialization, comparison, or representation logic.
- `pathlib`: use when code manipulates filesystem paths with strings or
  `os.path` in a way that would become clearer as `Path` operations.
- `functools`: use for real caching, partial application, ordering helpers, or
  wrappers. Prefer clear loops over `reduce` unless reduction is the clearest
  expression.
- `tomllib`: use to read TOML configuration in Python `3.11+`; Project-K's
  intended `3.12.10` supports it without fallback.
- `graphlib`: use for dependency ordering or DAG execution when a real graph
  exists.
- `heapq`: use for priority queues when repeated sorting or minimum extraction
  exists.
- `secrets`: use for tokens, IDs, passwords, or any security-sensitive random
  value. Do not use `random` for secrets.
- `shutil`: use for file and directory copies, moves, archiving, or disk
  operations that are currently hand-written.
- `textwrap`: use for readable multi-line text, indentation, dedentation, or
  wrapping when manual newline formatting is noisy.
- `itertools`: use for iterator composition, combinations, grouping, chaining,
  or flattening when it makes loops clearer.

## Output Contract

For each evaluated library, report:

- library name;
- case found with file reference, or `none`;
- verdict: integrate, discard, or partial;
- change applied, or `not applicable`;
- impact on clarity, safety, or maintainability.

End with a summary table listing every evaluated library and its verdict.
