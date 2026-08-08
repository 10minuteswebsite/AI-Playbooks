<!-- ai-playbooks-handoff:v3 -->
# Universal Agent Handoff

This contract applies to OpenCode and its selected models. Legacy adapters may point here, but switching platforms is not part of the current workflow.

## Source-of-truth hierarchy

1. The user's current explicit request.
2. Repository-local instructions and `docs/AI_WORKFLOW.md`.
3. `docs/PROJECT_CONTEXT.md` for durable product and technical facts.
4. `docs/CURRENT_STATE.md` for short-lived operational state.
5. `TODO.md` for the development plan and complete known backlog.
6. Git and GitHub for detailed history, diffs, reviews, checks, and publication evidence.

Conversation history is optional context and must never be required for continuation. Changing models inside OpenCode does not change project state.

## Continuity rules

- Read progressively: begin with `moving.md` and `docs/CURRENT_STATE.md`, then open only the files needed for the next exact step.
- Preserve working behavior, user changes, configuration, decisions, and scope unless the current task authorizes a change.
- Separate verified facts, assumptions, decisions, blockers, and unperformed checks.
- Do not copy conversations, full diffs, large code blocks, or Git-recoverable history into handoff documents.
- Complete and verify one focused increment at a time. Record material decisions in ADRs instead of hiding them in chat.
- Record newly discovered work in `TODO.md` without silently adding it to the active scope. `docs/CURRENT_STATE.md` must identify the active `TODO-NNN` item when work is in progress.
- Use repository-native commands and policies. Never assume a tool, model, vendor, or agent-specific feature is available.

## Active interaction contract

- Never become silent, idle, or stop at a plan, partial result, progress report, or statement of intent while useful safe work remains.
- Do not assign routine technical management to the user. Continue autonomously when the answer can be discovered or the choice is safe, reversible, and within scope.
- Every interaction has exactly two valid terminal states:
  1. **Finished:** the requested outcome is complete; say **“Ya terminé”** / **“Finished”** and provide verification evidence.
  2. **Human input required:** useful independent work is exhausted; state the exact blocker and ask one concise question that only the user can answer.
- Waiting is valid only after asking that blocking question. Never wait silently or imply that the user must guess what to do next.

## Mandatory session close

Before ending every substantive work session:

1. leave the repository in a stable state when possible;
2. run verification proportional to the change;
3. review the final diff and preserve unrelated work;
4. update `TODO.md` with newly discovered, reprioritized, blocked, or recently completed work;
5. update `docs/CURRENT_STATE.md` with completed work, the active `TODO-NNN` item, decisions, blockers, verification results, important files, and one next exact safe step;
6. commit and publish verified work according to `docs/AI_WORKFLOW.md`, or record the exact publication blocker;
7. ensure the next agent can continue without the previous conversation.

Never mark a check as passed unless it actually ran. Never mark the session complete while `CURRENT_STATE.md` is stale.
