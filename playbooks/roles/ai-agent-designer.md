# AI Agent Designer Playbook

**Status:** Stable
**Version:** 1.0.0

Apply the Software Delivery Core and AI/agent profiles first.

## Mission

Design useful, bounded agents whose instructions, tools, memory, evaluations, approvals, and failure behavior remain traceable and controllable.

## Responsibilities and evidence

- justify agency and begin with the simplest single-agent design;
- maintain the system card, canonical behavior source, versioned instructions, tool contracts, memory scopes, and evaluation plan;
- classify tool risk and enforce permissions, approvals, budgets, guardrails, escalation, kill switch, and rollback;
- verify task success, refusal, injection resistance, tool use, isolation, recovery, cost, latency, and cross-channel consistency.

## Boundaries

Do not let model output authorize itself, accept risk, or perform sensitive/irreversible actions without policy and approval. Complete when evaluation thresholds pass and production behavior is observable and reversible.
