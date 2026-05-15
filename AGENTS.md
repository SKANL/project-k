# Project-K Agent Guide

Project-K is a living local-first and hybrid multiagent project. Do not treat
the current repository shape as a fixed product spec. Treat the documents in
`docs/` as operating policies for future work.

## Required Grounding

Before proposing or changing behavior:

1. Inspect the current files, manifests, entry points, tests, and relevant docs.
2. Report any mismatch between the user's request and repository reality.
3. Prefer evidence from the repo over memory from earlier conversations.
4. Do not infer shipped capabilities from product direction documents.

Current intended runtime target is Python `3.12.10`. Always check
`.python-version` and `pyproject.toml` before Python work, and call out any
version mismatch before changing code.

Always activate the project virtual environment before running Python commands,
tests, scripts, package operations, or repo work that depends on Python:
`.venv\Scripts\activate` on Windows PowerShell. If `.venv` is missing, create it
with `uv venv --python 3.12.10` before continuing.

## Product Direction

Project-K should evolve toward a useful local-first agent operating layer:

- local models handle routine, private, cheap, repetitive, and verification work;
- cloud models are optional escalation for high-value cognitive work;
- users see cost, privacy, network, filesystem, and security consequences before
  risky execution;
- technical users can extend providers, tools, workflows, and agent bridges;
- non-technical users should get guided tasks instead of raw infrastructure.

This direction is not a claim that these features already exist.

## Working Rules

- Activate `.venv` before Python-dependent work.
- Read before touching. Open every file you will modify.
- Preserve observable behavior unless the user explicitly asks for behavior
  change.
- Change one coherent unit at a time.
- Keep edits small, reversible, and explainable.
- Prefer deletion and simplification over new abstraction.
- Add abstraction only when it removes real complexity or enables a concrete
  extension point already needed by the task.
- Keep documentation true over impressive.
- Never add secrets, API keys, tokens, credentials, or private local paths.

## Cost, Privacy, And Security Notes

Any change involving agents, tools, network, cloud providers, filesystem writes,
MCP, ACP, A2A, browser automation, shell execution, RAG, memory, or external APIs
must explicitly document:

- whether it runs local-only, networked, or cloud-backed;
- what user data may leave the machine;
- what files may be read or written;
- what secrets or environment variables are required;
- what confirmation or policy gate is needed before execution;
- how failures degrade without paid providers.

## Refactoring Standard

Use the seven-phase workflow in `docs/refactoring-policy.md` for simplification
work. Functional invariance is mandatory. If you cannot prove a removal or
rename preserves behavior, do not make it. Mark the uncertainty in the report
and ask for direction. Simplification tasks must use the exact report order from
`docs/refactoring-policy.md`.

## Python Standard Library Standard

Use `docs/stdlib-policy.md` before introducing or refactoring around Python
stdlib modules such as `dataclasses`, `pathlib`, `functools`, `tomllib`,
`graphlib`, `heapq`, `secrets`, `shutil`, `textwrap`, or `itertools`.
Use a stdlib feature only when it simplifies real code already present.

## Preferred Workflow

1. Read: inspect the relevant repo state.
2. Inventory: list complexity, risks, interfaces, and constraints.
3. Plan: explain the smallest safe change.
4. Edit: change one unit at a time.
5. Verify: run focused checks and read their output.
6. Summarize: report files changed, behavior impact, verification, and open
   risks.

## Verification

Before claiming work is complete, run the strongest practical verification for
the change. Documentation-only changes still require file existence checks,
incomplete-marker scans, and a lightweight Python compile check when Python
files are present.
