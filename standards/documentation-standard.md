# Documentation Standard

**Status:** Stable
**Version:** 2.3.0

## Objective

Make every system understandable, reviewable, operable, and reproducible without relying on undocumented personal knowledge.

## Required hierarchy

1. Universal entry: short `moving.md` that routes any agent without duplicating project history.
2. Collaboration contract: stable, agent-neutral `HANDOFF.md` linked to the shared project workflow.
3. Agent adapters: short optional `AGENTS.md`, `CLAUDE.md`, or equivalent files that point to the universal entry.
4. Project plan and backlog: concise root `TODO.md` with stable item identifiers, priorities, dependencies, and observable outcomes.
5. Project memory: stable `docs/PROJECT_CONTEXT.md` and short operational `docs/CURRENT_STATE.md` linked to the active backlog item.
6. README: purpose, ownership, setup, usage, verification, and links.
7. Architecture document: business context, boundaries, flows, data, security, operations, and delivery plan.
8. Module documents: responsibilities, contracts, ownership, failure behavior, and tests.
9. ADRs: consequential choices, alternatives, tradeoffs, and replacement path.
10. API/event contracts: versioned machine boundaries and delivery semantics.
11. Runbooks: detection, diagnosis, mitigation, recovery, and escalation for operational risks.
12. Project briefs and work items: outcome, scope, acceptance criteria, authorization, verification, and rollback.
13. Risk and threat records: impact, abuse paths, controls, owners, and accepted residual risk.
14. AI system cards and evaluation plans when model behavior affects product outcomes.

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
- Keep `moving.md` short, stable, and navigational. Keep collaboration rules in `HANDOFF.md`; never turn either file into a session diary.
- Apply progressive disclosure: read the entry and current state first, then load only documentation and code required by the next exact step.
- Keep the initial plan and all known pending work in `TODO.md`; keep only the active item and immediate operational evidence in `CURRENT_STATE.md`.
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
