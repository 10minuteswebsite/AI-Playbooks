# Documentation Standard

**Status:** Stable
**Version:** 1.0.0

## Objective

Make every system understandable, reviewable, operable, and reproducible without relying on undocumented personal knowledge.

## Required hierarchy

1. README: purpose, ownership, setup, usage, verification, and links.
2. Architecture document: business context, boundaries, flows, data, security, operations, and delivery plan.
3. Module documents: responsibilities, contracts, ownership, failure behavior, and tests.
4. ADRs: consequential choices, alternatives, tradeoffs, and replacement path.
5. API/event contracts: versioned machine boundaries and delivery semantics.
6. Runbooks: detection, diagnosis, mitigation, recovery, and escalation for operational risks.

## Writing rules

- Start with the outcome and audience.
- Separate verified facts, assumptions, decisions, and open questions.
- Use domain language; isolate vendor terms to integration documentation.
- Prefer concise headings, tables, diagrams, and examples over long narrative.
- Use synthetic data only. Never include secrets or real personal information.
- Link to a source of truth instead of duplicating volatile information.
- Date and assign an owner to documents whose accuracy is operationally important.

## Decision threshold

Create an ADR when a choice is costly to reverse, crosses domains, changes a public contract, affects security/privacy, introduces a provider dependency, or carries meaningful operational risk. Routine implementation details do not need ADRs.

## Change discipline

- Update documentation in the same change as behavior.
- Preserve history; supersede decisions instead of silently rewriting them.
- Mark drafts and placeholders explicitly.
- Review affected contracts and diagrams whenever boundaries change.
- Include verification evidence and unresolved risk in the change description.

## Definition of done

Documentation is complete when it reflects actual behavior, identifies ownership and boundaries, explains important decisions, contains no sensitive data, links relevant contracts and tests, and enables another qualified person to operate or change the system safely.
