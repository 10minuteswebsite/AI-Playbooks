# Documentation Standard

**Status:** Stable
**Version:** 2.1.0

## Objective

Make every system understandable, reviewable, operable, and reproducible without relying on undocumented personal knowledge.

## Required hierarchy

1. Agent adapters: short `AGENTS.md` and `CLAUDE.md` files that point to one shared project workflow.
2. Project memory: stable `docs/PROJECT_CONTEXT.md` and short operational `docs/CURRENT_STATE.md`.
3. README: purpose, ownership, setup, usage, verification, and links.
4. Architecture document: business context, boundaries, flows, data, security, operations, and delivery plan.
5. Module documents: responsibilities, contracts, ownership, failure behavior, and tests.
6. ADRs: consequential choices, alternatives, tradeoffs, and replacement path.
7. API/event contracts: versioned machine boundaries and delivery semantics.
8. Runbooks: detection, diagnosis, mitigation, recovery, and escalation for operational risks.
9. Project briefs and work items: outcome, scope, acceptance criteria, authorization, verification, and rollback.
10. Risk and threat records: impact, abuse paths, controls, owners, and accepted residual risk.
11. AI system cards and evaluation plans when model behavior affects product outcomes.

## Writing rules

- Start with the outcome and audience.
- Separate verified facts, assumptions, decisions, and open questions.
- Use domain language; isolate vendor terms to integration documentation.
- Prefer concise headings, tables, diagrams, and examples over long narrative.
- Use synthetic data only. Never include secrets or real personal information.
- Link to a source of truth instead of duplicating volatile information.
- Date and assign an owner to documents whose accuracy is operationally important.
- Write plain-language summaries before technical detail so non-programmers can review decisions and evidence.
- Keep instructions close to the scope they govern: universal rules in standards, project-type rules in profiles, and provider details in adapters.
- Do not duplicate shared workflow policy between agent adapters. Keep stable facts in project context and volatile session state in current state.
- Make every active current-state document contain one concrete next step that does not depend on conversation history.

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
