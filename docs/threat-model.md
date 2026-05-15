# Core v0 Threat Model

Core v0 is a dry-run router. It classifies a task, estimates the safest route,
and prints policy impact. It performs no privileged action: no LLM call, cloud
API call, browser use, shell execution, MCP call, ACP delegation, A2A exchange,
automation creation, filesystem read, or filesystem write.

## Assets

- user task text passed through CLI arguments;
- route decision metadata: category, confidence, target, cost, privacy, required
  permissions, warnings, and next step;
- JSON output consumed by future tools or user interfaces;
- future provider configuration, credentials, local model endpoints, and tool
  permissions;
- user trust in whether Project-K actually executed anything.

## Trust Boundaries

- CLI arguments are untrusted user input.
- Human-readable output is advisory and must not be interpreted as execution.
- JSON output is a machine-readable contract but still represents a dry-run
  decision only.
- Future provider, MCP, ACP, A2A, filesystem, browser, shell, and automation
  integrations cross stronger trust boundaries and must add explicit policy
  gates before execution.
- Future config and secret storage must be treated as privileged input.

## Attacker-Controlled Input

The task string can include prompt injection, misleading instructions, fake
system messages, paths, URLs, secrets, or commands. Core v0 must treat all of it
as text to classify, not as instructions to execute.

## Security Invariants

- Core v0 must not execute commands or tools.
- Core v0 must not read, list, write, move, delete, or upload user files.
- Core v0 must not contact the network or cloud providers.
- Core v0 must not require or print secrets.
- Core v0 output must state when a route is a future execution candidate rather
  than an action already performed.
- Risk flags must be conservative when a task implies files, network, cloud,
  automation, or external agents.

## Failure Modes

- The router underestimates privacy, cost, network, or filesystem risk.
- A downstream UI or script treats a dry-run decision as completed execution.
- A prompt-injection string influences future tool selection without policy
  validation.
- Ambiguous text is routed to a powerful tool instead of asking for
  clarification.
- JSON consumers rely on unstable field names or infer extra guarantees from
  the contract.

## Required Controls Before Future Execution

- permission gates for filesystem, shell, browser, network, MCP, ACP, A2A, and
  automation actions;
- path normalization and scope containment for local file operations;
- explicit provider and model selection before cloud use;
- secret loading from environment or secure config, never from docs or prompts;
- audit summaries that list what was read, written, sent, or delegated;
- tests proving that dry-run mode remains non-executing.

## Core v0 Review Checklist

- Does the route decision truthfully say no execution happened?
- Are cost, privacy, network, filesystem, and confirmation flags conservative?
- Is ambiguous or risky work routed to human clarification?
- Does JSON preserve the stable output keys?
- Can future execution be added behind clear policy gates instead of hidden side
  effects?
