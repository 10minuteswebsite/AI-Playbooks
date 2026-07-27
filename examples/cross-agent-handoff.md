# Example: Claude and Codex Handoff

## User invocation

The user says only:

> Usa el arquitecto. Quiero una página que muestre el estado del servicio.

## Claude begins

Claude reads the project adapters, shared workflow, project context, current state, Git status, and relevant commits. It creates a work item for a synthetic health endpoint, documents the contract, and updates `docs/CURRENT_STATE.md`:

- completed: architecture and contract;
- active objective: deliver the health endpoint;
- important files: contract and work item;
- verification: documentation validation passed;
- next exact step: implement the endpoint and its contract test.

Claude commits and pushes the completed documentation increment. It does not copy the conversation into the handoff.

## Codex continues

The user opens Codex and says only:

> Usa el arquitecto.

Codex detects a managed project, reads the same shared memory, confirms Git state, and implements the documented next step. It runs the contract test, reviews the diff, updates current state, commits, pushes, and opens or updates the pull request.

## Claude resumes

The user later returns to Claude and again says:

> Usa el arquitecto.

Claude reads that implementation and tests are complete. If the change is normal, reversible, and all checks pass, it may complete the approved automatic merge. It then records no active work and identifies the next product decision without requiring either previous conversation.

## Evidence

`python3 scripts/test_project_handoff.py` reproduces this lifecycle with temporary new, legacy, and conflicting projects. It verifies that legacy files are preserved, adoption requires approval, both agents share one workflow, active state has a concrete next step, and continuation does not depend on chat history.
