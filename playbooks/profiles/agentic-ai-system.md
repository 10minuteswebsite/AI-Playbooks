# Agentic AI System Profile

**Status:** Stable
**Version:** 1.0.0

Use when a model plans or controls a multi-step workflow, selects tools, changes external state, or delegates work.

## Justify agency

Use an agent only when deterministic automation is too brittle for the workflow's ambiguity. Start with one agent and the fewest tools. Add multiple agents only when separate responsibilities measurably improve quality, security, or operability.

## Required artifacts

- AI system card and evaluation plan;
- inventory of model, instructions, tools, data sources, memory, and connectors;
- contract and owner for every tool;
- threat model covering untrusted content, prompt injection, goal hijacking, tool misuse, identity, supply chain, data leakage, and unexpected code execution;
- deployment, monitoring, incident, kill-switch, and rollback plan.

## Tool and action controls

Classify every tool as read-only, reversible write, sensitive, or irreversible. Enforce least privilege, tenant/user scope, structured inputs, output validation, timeouts, rate limits, and audit events. Require human approval for sensitive or irreversible actions unless an explicit risk decision delegates them.

Set budgets for steps, retries, duration, tokens, and money. Stop safely and hand control to a person when a budget, confidence threshold, or policy boundary is reached.

## Evaluation and operations

- test success, refusal, escalation, tool selection, tool arguments, recovery, and termination;
- include prompt injection, hostile tool output, stale memory, permission failure, duplicates, and provider failure;
- trace decisions and tool calls without storing secrets or unnecessary personal data;
- release gradually, monitor user outcomes and safety signals, and maintain a tested kill switch;
- convert production failures into versioned evaluation cases.

## Protocols and connectors

Treat MCP and equivalent protocols as replaceable integration mechanisms. For remote MCP, follow the current authorization specification, validate token audience, prohibit token passthrough, store tokens securely, and restrict the enabled tool catalog.
