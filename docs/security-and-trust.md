# Security And Trust

Project-K's value depends on local-first control, transparent cloud escalation,
and careful tool execution. Security guidance must be concrete and repo-scoped,
but this document is not a full threat model for future product surfaces. Update
it when real product surfaces exist.

## Trust Boundaries

Treat these as trust boundaries:

- user input and prompts;
- local files and directories;
- shell commands and subprocesses;
- browser or desktop automation;
- MCP servers and external tools;
- ACP-connected agents;
- future A2A peer agents;
- cloud model providers;
- API keys, OAuth tokens, credentials, and local config files;
- generated artifacts and workflow memory.

## Local-First Defaults

Default to local execution for private, repetitive, low-risk, or low-value work.
Before using network or cloud providers, document:

- what data is sent;
- why local execution is insufficient;
- expected cost class;
- provider or API key required;
- fallback when the provider is unavailable.

## Filesystem Rules

Tools that read or write files must describe their scope. Write operations should
prefer generated copies or explicit output directories over modifying originals.
Risky writes require confirmation or a policy gate.

Path handling must prevent accidental writes outside intended roots when a safe
root is configured. Never trust user-provided paths without normalization and
containment checks.

## Secrets

Never commit secrets. Never print full secrets in logs, errors, docs, or test
fixtures. Redact keys with names containing values such as `api_key`, `token`,
`authorization`, `password`, `secret`, or credential-specific variants.

Environment-variable docs may name required variables but must not include real
values.

## Tool And Agent Execution

Any tool, workflow, or agent bridge must declare:

- permission level: read-only, local write, network, cloud, shell, or destructive;
- required secrets or connections;
- expected input and output;
- failure behavior;
- user confirmation needs;
- audit trail or summary users can inspect.

Specialized agents should be delegated only the context and tools needed for
their task. Avoid all-to-all agent access unless there is a concrete workflow
that needs it and a policy layer controls it.

## Protocol Guidance

MCP is the preferred early protocol for exposing tools, resources, and prompts.
Validate MCP server trust, capabilities, and permission scope before use.

ACP is the preferred early bridge for delegating coding tasks to existing agents.
Treat ACP agents as powerful external executors. Show the user which agent is
being invoked and what workspace or files it may affect.

A2A is future-facing interoperability. Do not add A2A as a required dependency
until Project-K needs peer agent discovery, agent cards, task exchange, or
cross-organization delegation.

## Security Review Standard

For security-sensitive changes, identify:

- attacker-controlled input;
- privileged action or sink;
- preconditions;
- guards and policy checks;
- evidence from tests, reproduction, or static trace.

Do not claim a vulnerability exists or is fixed without evidence.
