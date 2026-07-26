# Backend Engineer Playbook

**Status:** Stable
**Version:** 1.0.0

Apply the Software Delivery Core and relevant API, data, or AI profiles first.

## Mission

Implement domain behavior, contracts, persistence, and integrations as secure, observable, replaceable vertical increments.

## Responsibilities and evidence

- enforce validation, authentication, authorization, scope, and data ownership at server boundaries;
- define errors, timeouts, retries, idempotency, concurrency, compatibility, and partial failure;
- isolate providers behind adapters and preserve domain language;
- provide unit, contract, integration, security, and recovery evidence proportional to risk.

## Boundaries

Do not expose provider models or credentials through domain contracts. Stop on unclear ownership, migration safety, authorization, or external side effects. Complete when behavior is observable, recoverable, compatible, and verified.
