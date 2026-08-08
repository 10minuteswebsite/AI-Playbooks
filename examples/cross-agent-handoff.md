# Example: OpenCode Session and Model Continuity

This example retains its historical filename for links already shared. The current workflow uses one OpenCode project; changing models inside that project does not require copying conversations or performing a platform handoff.

## User invocation

The user says:

> Usa el arquitecto. Quiero una página que muestre el estado del servicio.

## OpenCode begins

OpenCode loads `opencode.json`, follows the canonical bootstrap, reads `moving.md`, `HANDOFF.md`, `docs/CURRENT_STATE.md`, the active `TODO.md` item, and only the relevant files. It creates or updates the work item for a synthetic health endpoint and records the exact next step.

## Change models without losing state

The user may select another model in the same OpenCode project. The model reads the same repository state and continues from the recorded next step. No conversation export, platform switch, or repeated project explanation is needed.

## Start a new OpenCode session

The user can say:

> Entra al repositorio [REPOSITORIO], lee moving.md y sigue las instrucciones.

OpenCode recovers the work from GitHub, verifies Git state, loads only the necessary context, implements the documented step, runs the relevant checks, updates current state, and publishes according to repository policy.

## Evidence

`python3 scripts/test_project_handoff.py` verifies that a managed project recovers its active task from repository memory without conversation history. Legacy `AGENTS.md` and `CLAUDE.md` files remain preserved for compatibility but are not required by this workflow.
