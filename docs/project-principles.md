# Project Principles

Project-K is a local-first, hybrid multiagent system in formation. The project
should stay useful for two audiences from the beginning:

- non-technical users who need guided tasks, understandable approvals, and useful
  everyday outcomes;
- technical users who want to inspect, extend, replace, and automate the system.

The project should begin with a terminal interface and keep the core independent
enough to support later interfaces such as desktop, web, or service mode.

## Product Philosophy

Project-K should not compete by being another general agent that promises to do
everything. Its strongest direction is an operating layer that coordinates local
models, cloud models, tools, workflows, and specialized agents.

The local side should do the cheap and routine work: routing, classification,
summarization, context preparation, privacy filtering, validation, repetitive
execution, and workflow memory. The cloud side should be optional and reserved
for work that justifies its cost or requires stronger reasoning.

## Useful Over Impressive

Prefer durable utility over short-lived demos. A feature is valuable when it
helps users repeatedly save time, reduce cost, keep data private, or produce a
reliable outcome.

Daily utility should come from:

- guided workflows instead of raw prompts;
- visible cost and privacy tradeoffs;
- local document, file, project, and knowledge work;
- safe delegation to specialized tools and agents;
- repeatable workflows that get cheaper after the first run.

## Protocol Direction

MCP should be treated as the early standard for tools, resources, prompts, and
external data access.

ACP should be treated as the early bridge to existing coding agents and agentic
developer tools such as Claude Code, OpenCode, Codex, Gemini CLI, Goose, and
similar systems where adapters exist.

A2A should be treated as strategic compatibility for later agent-to-agent
interoperability. Do not make it a required MVP dependency unless a concrete
workflow needs peer agent discovery, agent cards, task exchange, or cross-system
delegation.

## Non-Static Documentation

This documentation describes direction and operating rules. It must not be used
as evidence that a capability has shipped. Agents must inspect code and tests
before making implementation claims.
