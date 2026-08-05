<!-- ai-playbooks-workflow:v5 -->
# Shared AI Project Workflow

This document is the detailed operational policy shared by all agents. `moving.md` is the universal entry point, `HANDOFF.md` is the stable continuity contract, and agent-specific files are short adapters that must not redefine them.

## Architect invocation

When the user says **“Use the architect”** or **“Usa el arquitecto”**:

1. Inspect the project instructions, memory documents, Git state, and relevant history.
2. If this structure is already installed, continue from the next exact step when it aligns with the user's request.
3. If the project is new, initialize the structure and guide the first useful increment.
4. If the project is existing but not managed by AI-Playbooks, explain that briefly and ask whether to adopt the architect structure while preserving existing behavior. Do not migrate it before approval.
5. If the situation remains ambiguous, recommend a next action and offer no more than three plain-language options.

When the user provides a clear objective with the invocation, begin directly without an unnecessary menu.

The command **“Entra al repositorio [REPOSITORIO], lee moving.md y sigue las instrucciones”** activates the same continuation behavior for any agent. Do not request the previous conversation; follow the progressive route defined in `moving.md`.

## GitHub-first workspace

- GitHub is the durable source of truth. A local checkout is temporary working state managed by the AI, not something the user must organize.
- Identify the repository from the current page, project connection, remote, or conversation. If it is unknown, ask only for the GitHub link or for GitHub authorization.
- Verify access with the GitHub connector/API, `gh repo view`, or `git ls-remote`. Do not classify a repository as private from a login page or redirect.
- Never request passwords, personal access tokens, secrets, or recovery codes in chat. Use the product's authorization flow.
- Before editing, synchronize safely. After verified normal changes, commit, push, and open or update a pull request according to the publication policy below.

## Session startup

Before substantive work:

1. Read `moving.md`.
2. Read `HANDOFF.md`, `docs/CURRENT_STATE.md`, and the `Now` and `Blocked` sections of `TODO.md`.
3. Inspect `git status` without altering user changes.
4. Review only the recent commits relevant to the current objective.
5. Identify the active `TODO-NNN` item and next exact step.
6. Read `docs/PROJECT_CONTEXT.md` and only the work item, decisions, architecture, code, or tests needed for that step; expand scope only when evidence requires it.

Project files and Git are the source of truth. Conversation history is temporary context, never operational memory.

## Working behavior

- Continue autonomously while useful safe work remains. A plan, progress report, partial result, or routine technical question is not a stopping point.
- Do not create technical chores for the user. Ask only when one exact human decision, credential, authorization, or external-state change blocks further progress.
- Preserve existing behavior and configuration unless the approved task requires a change.
- Separate facts, assumptions, decisions, and open questions.
- Work in small, complete, verifiable increments.
- Keep `docs/PROJECT_CONTEXT.md` stable and concise; update it only when durable project facts change.
- Keep `moving.md` and `HANDOFF.md` stable and agent-neutral. Do not place session history in them.
- Keep the initial plan and complete known backlog in `TODO.md`. Give actionable items stable IDs, record discovered work without expanding current scope, and keep completed history in GitHub.
- Keep `docs/CURRENT_STATE.md` short, current, and sufficient for another agent to resume without the prior conversation. Record decisions made during the session or link their ADRs.
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
4. Record newly discovered or changed work in `TODO.md`; move only recently completed items to its completion section.
5. Record what was completed, what remains, important files, verification results, decisions, known errors, risks, and blockers.
6. Update `docs/CURRENT_STATE.md` with the active `TODO-NNN` item, that evidence, and one next exact step.
7. Commit completed work together with the updated backlog and state, or document exactly why it cannot be committed.
8. Publish according to the Git policy, or record the exact publication blocker.
9. If anything material changes after the updates, update and commit the backlog and state again.
10. Ensure `moving.md` still routes any agent to a handoff that does not require the previous conversation.

End the user interaction explicitly with **“Finished”** / **“Ya terminé”** and verification evidence, or with one concise blocking question when useful independent work is exhausted and only the user can unblock progress. Never end silently, passively, or with an unexplained wait.
