# Architecture: <System or Initiative>

**Status:** Draft | Approved | Superseded
**Owner:** <name/team>
**Last updated:** YYYY-MM-DD
**Related ADRs:** <links>

## 1. Executive summary

Explain the business problem, proposed outcome, and why this work matters in plain language.

## 2. Goals and success measures

- Business goal:
- Users:
- Observable outcome:
- Metrics:
- Acceptance criteria:

## 3. Scope

### In scope

- <item>

### Out of scope

- <item>

## 4. Context

- Existing system:
- Constraints:
- Assumptions:
- Unknowns:
- Working configurations to preserve:

## 5. Requirements

### Functional

| ID | Requirement | Priority | Verification |
|---|---|---|---|
| F-01 | | | |

### Non-functional

| Area | Requirement | Target | Verification |
|---|---|---|---|
| Availability | | | |
| Performance | | | |
| Security/privacy | | | |
| Scale | | | |
| Recovery | | | |

## 6. Domain model and boundaries

Describe domains, responsibilities, ownership, and explicit exclusions. Avoid provider-based boundaries.

| Domain/module | Responsibility | Owns | Does not own |
|---|---|---|---|
| | | | |

## 7. Proposed architecture

Include a component diagram and explain the main request, event, and data flows. Identify synchronous and asynchronous boundaries.

## 8. Data and memory

- Data ownership and lifecycle:
- Organization/tenant isolation:
- User/resource/purpose scoping:
- Retention, deletion, and audit:
- AI model, prompt, retrieval, and memory governance when applicable:

## 9. Contracts and events

Link API/event contracts. Define versioning, idempotency, retry, ordering, timeout, and compatibility behavior.

## 10. Integrations

| Capability | Contract/port | Current adapter | Replacement path | Failure behavior |
|---|---|---|---|---|
| | | | | |

## 11. Security and privacy

Document authentication, authorization, least privilege, secret management, sensitive-data handling, audit, abuse controls, and threat mitigations.

## 12. Reliability and operations

- Failure modes and recovery:
- Observability and alerts:
- Capacity and scaling:
- Deployment and rollback:
- Backup and disaster recovery:

## 13. Delivery plan

List small vertical increments, each with value, dependencies, acceptance criteria, and verification.

## 14. Alternatives and decisions

Summarize considered alternatives and link ADRs for consequential decisions.

## 15. Risks and open questions

| Risk/question | Impact | Mitigation/owner | Due date |
|---|---|---|---|
| | | | |
