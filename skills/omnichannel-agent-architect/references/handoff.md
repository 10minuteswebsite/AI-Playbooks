# Durable handoff

## moving.md
Keep it short, stable, and navigational. It routes the next agent to the durable collaboration contract, backlog, current state, and other appropriate sources. Do not use it as a mutable operational diary.

## TODO.md
Update when task state changes.

## docs/CURRENT_STATE.md
Update when architecture/runtime/integration/deploy state changes.

## HANDOFF.md
Follow the local repository convention and keep the collaboration contract usable by any supported agent.

Mutable operational state belongs primarily in `HANDOFF.md`, `TODO.md`, and `docs/CURRENT_STATE.md`, not in `moving.md`.

## Git evidence
Before saying complete:
1. intended files included
2. tests
3. commit
4. push
5. remote SHA verify
6. PR
7. correct base branch

## PR evidence
- Summary
- Tests
- Durable handoff
- Risks / limitations
- Remaining work
- Recommended next step
- Deployment

Do not turn durable docs into chat transcripts.
