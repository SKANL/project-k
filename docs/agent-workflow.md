# Agent Workflow

This repo should be worked on with evidence-first discipline. Future agents must
ground themselves in the current tree before planning or editing.

## Start Of Task

1. Read `AGENTS.md`.
2. Inspect the files relevant to the request.
3. Check manifests and runtime files before Python work:
   - `.python-version`
   - `pyproject.toml`
   - dependency files if they exist
4. Ensure the project virtual environment exists and is active before Python
   commands or Python-dependent repo work:
   - create it with `uv venv --python 3.12.10` if `.venv` is missing;
   - activate it with `.venv\Scripts\activate` on Windows PowerShell.
5. Report mismatches between intended direction and repo reality.

## Planning Standard

Every plan should identify:

- goal and success criteria;
- audience affected: non-technical user, technical user, or both;
- files or modules likely to change;
- behavior that must stay invariant;
- cost, privacy, security, network, and filesystem implications;
- tests or checks that will prove the result.

For documentation-only changes, keep the plan short and verify truthfulness,
file presence, and absence of incomplete markers.

## Edit Standard

- Read a file before editing it.
- Edit one coherent unit at a time.
- Avoid unrelated refactors.
- For refactoring tasks, follow the dedicated seven-phase workflow in
  `docs/refactoring-policy.md`.
- Preserve public behavior unless the request explicitly changes it.
- Keep names direct and specific.
- Remove dead code rather than comment it out.
- Do not create a framework until the repo has repeated real cases that need it.

## Verification Standard

Use the narrowest command that proves the claim, then broaden only when the
change affects shared behavior. Before completion:

- verify changed files exist;
- scan docs for incomplete markers and false implementation claims;
- run focused tests when code changes;
- run `python -m compileall .` from the active `.venv` for Python projects
  unless blocked;
- report any command that could not be run and why.

## Reporting Standard

End work with:

- files changed;
- behavior impact;
- verification commands and results;
- known risks or follow-up work.

Do not claim tests pass, builds succeed, or behavior is preserved without fresh
verification evidence.
