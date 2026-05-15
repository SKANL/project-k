# Refactoring Policy

Project-K favors radical simplification when behavior can be preserved. This
policy turns simplification work into an explicit seven-phase workflow.

## Thompson Standard

The success metric is not how much code changes. It is how much accidental
complexity disappears while users observe the same behavior.

Guiding rule: each line that does not exist is a failure mode that cannot
happen.

The north star is the same project, with the same public behavior, but easier
for a new developer to understand and change with confidence.

Signals of success:

- fewer files without lost functionality;
- fewer lines without lost clarity;
- fewer dependencies without lost cohesion;
- names that do not need comments to explain them;
- functions small enough to understand in one view when practical.

Fewer lines, files, or dependencies are only wins when behavior and clarity are
preserved.

## Non-Negotiable Reminders

- Read before touching. Open every file you will edit or judge.
- Functional invariance is mandatory. If behavior might change, stop and ask.
- Refactor one file at a time. Finish the full change and verification for that
  file before moving on.
- Process every relevant module in scope before reporting completion.
- After each change, verify imports, references, and affected dependencies.
- Do not simplify for style. Every simplification must reduce real complexity.
- Preserve the architecture currently established by the repo and approved
  design; simplify inside it, not against it.

## Phase 1: Accidental Complexity Inventory

Read the current project state and identify what exists but should not.

### Dead Code

Look for:

- functions defined but never called;
- variables declared but never used;
- imports unused in the file;
- conditional branches that cannot execute;
- comments that explain code that no longer exists.

Action: delete when justified. Do not move, archive, or comment out dead code.
If deletion is uncertain, keep it and document the proof gap.

### Duplication

Look for:

- identical or nearly identical logic in multiple places;
- copied functions with different names but the same behavior;
- constants with the same value defined in multiple files.

Action: consolidate into one source of truth when doing so reduces coupling and
keeps behavior unchanged.

### Premature Abstraction

Look for:

- classes or interfaces with one real implementation;
- indirection layers that add no flexibility;
- wrappers that only delegate without transforming anything;
- design patterns applied by habit rather than need.

Action: collapse the abstraction and write the direct code when current evidence
shows no real variation.

### Over-Engineering

Look for:

- configuration that never changes but is parameterized;
- plugin systems with only one actual plugin or no near-term plugin need;
- factories that always create the same type;
- inheritance where plain composition or a function is clearer.

Action: simplify to the real case, not the imagined case.

## Phase 2: KISS Per Module

Apply this checklist to each module or file in scope:

- Does each function do one complete thing? If it does two, consider splitting
  it. If it does half a thing, consider merging it with the caller or callee.
- Does the file, class, function, or variable name say what it does without
  reading its body?
- Does a function exceed roughly 20-25 lines? Review whether it can be split. If
  not, justify why keeping it whole is clearer.
- Does logic exceed three indentation levels? Try flattening with early returns,
  guard clauses, or clearer decomposition.
- Does a function have more than three or four parameters? Consider a small data
  object only if it reduces call-site complexity, or remove optional parameters
  that do not represent real variation.
- Does a comment explain what the code does instead of why it exists? Prefer a
  clearer name or structure; keep comments for intent, tradeoffs, or constraints.

## Phase 3: SOLID Without Dogma

Apply design principles only when they reduce complexity in this repo.

- Single Responsibility: split a class or module only when it has more than one
  real reason to change.
- Open/Closed: add an extension point only when adding real functionality would
  otherwise require cascading edits.
- Liskov Substitution: remove inheritance when a subclass breaks the parent
  contract, ignores required parameters, or raises behavior the parent contract
  does not permit.
- Interface Segregation: split broad interfaces when implementers do not need
  all methods, or remove the interface if there is only one implementation.
- Dependency Inversion: introduce an abstraction only when there is more than
  one plausible implementation, or when it materially improves testing or
  isolation.

If applying a principle makes the code harder to understand, do not apply it.

## Phase 4: Dependency Decoupling

Build a current dependency map from imports and real call paths. Identify:

- import cycles;
- modules that know too much about other modules;
- dependencies pointing outward from core logic to infrastructure, I/O, or
  framework code.

For each unnecessary coupling, choose the simplest valid cut:

1. Move code into the module that actually needs it.
2. Pass the required data as a parameter instead of importing a module.
3. Extract shared logic into a small dependency-free module.

Dependencies should point inward toward business logic and stable contracts, not
outward toward infrastructure. Do not introduce a dependency-inversion layer
unless the benefit is concrete.

## Phase 5: Renaming

Rename only when the new name is objectively clearer in the current project.

Rename candidates include:

- generic names: `manager`, `handler`, `util`, `helper`, `data`, `info`, `obj`,
  `temp`;
- names that do not describe the current responsibility;
- non-standard abbreviations such as `usr`, `cfg`, `proc`, or `mgr`;
- names inconsistent with the repo's naming style.

The new name should make the explanatory comment unnecessary.

For each rename, report:

- current name;
- proposed or applied name;
- symbol type: file, folder, class, function, method, or variable;
- affected files;
- one-line reason.

## Phase 6: Structural Consolidation

After deletions and simplifications, evaluate structure again:

- Are there files now so small that they should merge with a cohesive neighbor?
- Are there folders with one file that no longer justify a directory?
- Are there modules that became nearly empty after dead code removal?

Merge only small, cohesive units. Do not merge large files or unrelated
responsibilities. Fewer files with clearer purpose are better than more files
with weak boundaries.

## Phase 7: Functional Invariance Verification

Before closing, check every change:

- Is the module's public behavior identical?
- Do imports in other files still resolve?
- Do affected references still point to the right names?
- Do existing tests, if present, still pass?
- Would a user notice any difference? The expected answer is no.

If a check fails, revert the change or document exactly why it could not be
simplified safely.

If something looks removable but cannot be proven safe, do not delete it. If a
code comment is needed to keep the uncertainty visible, use `# CANDIDATO A
ELIMINAR` with a short justification. Also include the evidence needed to decide
later in the report.

## Required Refactor Report

Deliver refactoring work in this exact order:

1. `INVENTARIO DE COMPLEJIDAD ACCIDENTAL`
   - Group by dead code, duplication, premature abstraction, over-engineering,
     and dependency issues.
   - Include file and line references when available.
2. `CAMBIOS APLICADOS`
   - For each change: file, change type, what was removed or simplified, and
     why behavior stayed equivalent.
3. `RENOMBRADOS`
   - Table with original name, new name, symbol type, affected files, and
     reason.
4. `CONSOLIDACIONES`
   - Files or folders merged, and why the result is more cohesive.
5. `VIOLACIONES SOLID CORREGIDAS`
   - Principle, violation, correction, and file.
6. `MÉTRICAS DE REDUCCIÓN`
   - Lines removed, files removed or merged, imports removed, functions
     consolidated.
7. `VERIFICACIÓN DE INVARIANCIA`
   - Explicit confirmation that public behavior did not change, or documented
     exceptions and reversions.
8. `CIERRE — "La navaja de Thompson aplicada"`
   - One line for each design decision that became unnecessary.
