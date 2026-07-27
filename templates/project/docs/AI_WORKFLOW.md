<!-- ai-playbooks-workflow:v1 -->
# Shared AI Project Workflow

This document is the single source of truth for operational behavior shared by Codex and Claude Code. Agent-specific files are short adapters and must not redefine this workflow.

## Architect invocation

When the user says **“Use the architect”** or **“Usa el arquitecto”**:

1. Inspect the project instructions, memory documents, Git state, and relevant history.
2. If this structure is already installed, continue from the next exact step when it aligns with the user's request.
3. If the project is new, initialize the structure and guide the first useful increment.
4. If the project is existing but not managed by AI-Playbooks, explain that briefly and ask whether to adopt the architect structure while preserving existing behavior. Do not migrate it before approval.
5. If the situation remains ambiguous, recommend a next action and offer no more than three plain-language options.

When the user provides a clear objective with the invocation, begin directly without an unnecessary menu.

## Session startup

Before substantive work:

1. Read the permanent project instructions in `AGENTS.md` or `CLAUDE.md`.
2. Read `docs/PROJECT_CONTEXT.md`.
3. Read `docs/CURRENT_STATE.md`.
4. Inspect `git status` without altering user changes.
5. Review only the recent commits relevant to the current objective.
6. Identify active work and the next exact step.
7. Read only the files needed for that step; expand scope only when evidence requires it.

Project files and Git are the source of truth. Conversation history is temporary context, never operational memory.

## Working behavior

- Preserve existing behavior and configuration unless the approved task requires a change.
- Separate facts, assumptions, decisions, and open questions.
- Work in small, complete, verifiable increments.
- Keep `docs/PROJECT_CONTEXT.md` stable and concise; update it only when durable project facts change.
- Keep `docs/CURRENT_STATE.md` short, current, and sufficient for another agent to resume without the prior conversation.
- Store architecture in `docs/architecture/`, decisions in `docs/decisions/`, and active delivery records in `docs/work-items/`.
- Do not paste conversations, large code blocks, full diffs, or information that Git can provide into memory documents.

## Git and publication policy

When an increment is complete and relevant checks pass:

1. Review the final diff and preserve unrelated user changes.
2. Update `docs/CURRENT_STATE.md` before committing.
3. Create a focused commit automatically.
4. Push the branch to GitHub automatically when an authenticated remote is available.
5. Open or update a pull request automatically.
6. Merge automatically only when the change is normal, reversible, all required checks pass, no conflicts or unresolved review issues remain, and repository policy permits it.

Require human approval before merging changes involving security boundaries, sensitive or personal data, payments, production infrastructure or deployment, destructive operations, meaningful cost, access expansion, acceptance of material risk, or another sensitive/irreversible effect.

If commit, push, pull request, or merge cannot be completed, document the exact reason and next action in `docs/CURRENT_STATE.md`.

## Session close and handoff

Before ending:

1. Leave the project stable when possible.
2. Run relevant verification.
3. Review the final diff.
4. Commit completed work, or document exactly why it cannot be committed.
5. Update `docs/CURRENT_STATE.md` last.
6. Record what was completed and what remains.
7. Record important files and tests with results.
8. Record known errors, risks, and blockers.
9. Write one next exact step that another agent can execute.
10. Ensure the handoff does not require the previous conversation.

End the user interaction explicitly with **“Finished”** / **“Ya terminé”**, or with one concise question when a decision only the user can make blocks further safe progress.
