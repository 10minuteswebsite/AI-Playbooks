# Bootstrap GitHub-first

## A. Resolver repo

Prioridad:

1. owner/repo explícito
2. URL GitHub
3. alias o proyecto explícitamente mencionado por el usuario
4. repo activo en herramientas, solo si no existe intención explícita
5. búsqueda GitHub
6. pregunta corta

La intención explícita prevalece sobre un repositorio activo incidental. Si ambos contextos se contradicen y la intención no se puede resolver con certeza, preguntar antes de actuar.

## B. Verificar existencia

Si existe:
- leer metadata;
- identificar default branch;
- continuar.

Si no existe:
- si es proyecto nuevo, ejecutar flujo de creación;
- si el usuario esperaba que existiera, preguntar antes de crear reemplazo.

## C. Leer AI-Playbooks

Para arquitectura/interoperabilidad de 10minuteswebsite:
- `ARCHITECT_BOOTSTRAP.md`
- estándar actual de interoperabilidad
- ADRs relevantes

## D. Leer estado objetivo

Cuando existan:
- AGENTS.md
- CLAUDE.md
- opencode.json
- moving.md
- TODO.md
- HANDOFF.md
- docs/CURRENT_STATE.md
- README
- contracts
- tests
- recent commits
- relevant PRs/issues

## E. Reconstruir

Determinar:
- propósito
- arquitectura
- estado actual
- trabajo en curso
- blockers
- siguiente paso
- restricciones

## F. Ejecutar

`continúa`:
- seguir próximo paso seguro;
- pedir decisión solo si realmente hace falta.

Nueva tarea:
- usar estado durable como contexto.

## G. Branch discipline

Trabajo sustancial:
- base actualizada
- rama dedicada
- cambios acotados
- tests
- handoff
- commit
- push
- remote verify
- PR
