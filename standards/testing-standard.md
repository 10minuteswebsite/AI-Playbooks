# Testing and Verification Standard

**Status:** Stable
**Version:** 1.0.0

## Objective

Produce proportionate evidence that a change meets its acceptance criteria without breaking critical behavior.

## Risk levels

- **Low:** local, reversible, no sensitive data, no external side effect.
- **Medium:** shared users, persistent data, authentication, integrations, or operational impact.
- **High:** regulated or highly sensitive data, payments, safety, irreversible actions, critical infrastructure, or autonomous high-impact decisions.

The project risk assessment may raise but must not silently lower the required level.

## Required layers

Every change requires static checks available to the stack, focused automated tests, diff review, and a reproducible acceptance check. Add by boundary and risk:

- unit tests for domain rules and deterministic transformations;
- contract tests for APIs, schemas, events, adapters, tools, and AI outputs;
- integration tests for persistence and external boundaries;
- end-to-end tests for critical user journeys;
- security tests for authorization, scope, malformed input, and abuse paths;
- reliability tests for retry, duplicate, timeout, partial failure, concurrency, and recovery;
- regression evaluations for model, prompt, retrieval, memory, or tool changes.

## Test quality

Tests must be deterministic where possible, independent, readable, fast enough for their feedback loop, and tied to behavior rather than implementation details. Use synthetic or explicitly authorized data. A flaky test is a defect, not evidence.

## Quality gate

Before completion:

1. run formatting/lint and type or schema validation;
2. build or package the changed artifact when applicable;
3. run affected automated tests;
4. exercise the critical acceptance path;
5. run security and dependency checks appropriate to risk;
6. review the final diff and generated artifacts;
7. report exact checks, results, skipped checks, and residual risk.

Never weaken, skip, or delete a failing check merely to make a change pass without documenting and approving the reason.
