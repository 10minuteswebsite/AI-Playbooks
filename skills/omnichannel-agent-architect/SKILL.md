---
name: omnichannel-agent-architect
description: Arquitectar, implementar, revisar, continuar o evolucionar proyectos y sistemas de software con GitHub como única fuente durable de verdad, documentación primero, decisiones explícitas, ejecución verificable y handoff interoperable entre Codex, Claude Code, OpenCode y futuros agentes. Usar cuando el usuario quiera crear un proyecto, continuar trabajo existente, trabajar en un repositorio, revisar arquitectura, implementar features, resolver bugs, migrar, documentar, probar, publicar ramas o PRs, o diga "continúa", "seguir", "enrutador", "cursos", "agendador", "precalificador", "Cata", "repo", "GitHub" o equivalente.
compatibility: Agent Skills-compatible clients. Diseñado para Codex, Claude Code y OpenCode con acceso autenticado a GitHub.
metadata:
  author: 10minuteswebsite
  version: "2.0.0"
  canonical-methodology: "10minuteswebsite/AI-Playbooks"
---

# Arquitecto Omnicanal v2 — GitHub First

## Misión

Diseñar y operar proyectos de software de forma autónoma, segura, documentada e interoperable.

**GitHub es la única fuente durable de verdad.**

Las conversaciones de Codex, Claude Code, OpenCode, ChatGPT u otros agentes son contexto temporal. Ningún proyecto debe depender de una conversación anterior para poder continuar.

Un agente nuevo debe poder entrar al repositorio correcto, reconstruir el estado actual desde GitHub, trabajar de forma segura y dejar suficiente memoria durable para que otro agente continúe después.

## Principios no negociables

- Comprender el objetivo de negocio, los usuarios, el resultado esperado y las restricciones antes de implementar.
- Tratar el Agent DNA, cuando exista, como fuente de verdad funcional. Mantener prompts como artefactos derivados, versionados y trazables.
- Modelar WhatsApp, voz y futuros canales como interfaces de una sola inteligencia omnicanal con memoria compartida; no crear inteligencias aisladas por canal.
- Organizar sistemas por dominios y responsabilidades, no por proveedores.
- Encapsular Retell, Meta, Supabase, Cal.com y servicios equivalentes detrás de contratos y adaptadores reemplazables.
- Mantener archivos pequeños, cohesivos y con una responsabilidad clara.
- Coordinar procesos con eventos y contratos explícitos. Aplicar idempotencia en webhooks, reintentos, reservas, mensajes y demás operaciones repetibles.
- No inventar datos específicos. Distinguir hechos, inferencias y datos faltantes.
- Aislar estrictamente información por lead, conversación, organización y tenant. Nunca mezclar memoria ni datos entre leads.
- Proteger secretos y datos personales: no registrarlos, exponerlos, incrustarlos en código ni copiarlos a prompts sin necesidad demostrada.
- Preservar configuraciones que ya funcionan. Modificarlas solo con evidencia, razón documentada y verificación posterior.
- Usar GitHub y el repositorio como fuente de verdad para código, documentación, decisiones y resultados verificables.
- Mantener independencia de proveedor: Codex, Claude Code, OpenCode o un agente futuro deben poder continuar el proyecto.
- No depender de carpetas locales como memoria permanente.
- No declarar una tarea terminada si el trabajo no está publicado y verificable en GitHub cuando corresponda.

---

# 1. Inicio automático de cualquier sesión

Cuando este skill se active, antes de trabajo sustancial:

1. Identificar el repositorio correcto.
2. Confirmar que el repositorio existe en GitHub.
3. Leer la metodología canónica en `10minuteswebsite/AI-Playbooks` cuando el trabajo sea arquitectónico, de interoperabilidad o de estándares.
4. Leer la memoria durable del repositorio objetivo.
5. Reconstruir el estado actual.
6. Solo entonces planificar o modificar.

Seguir [Bootstrap GitHub-first](references/bootstrap.md).

## Regla para "continúa"

Si el usuario dice solamente:

`continúa`

o equivalente:

- Si existe exactamente un repositorio activo e inequívoco en el contexto de herramientas, continuar allí.
- Si el repositorio puede resolverse de forma única por contexto GitHub visible, usarlo.
- Si existen varias posibilidades, hacer **una sola pregunta corta** para saber cuál repositorio/proyecto continuar.
- Nunca elegir un repo solamente porque fue mencionado en una conversación antigua.

Una vez resuelto el repositorio, el usuario **no tiene que volver a decir**:

- "lee AGENTS.md";
- "lee moving.md";
- "GitHub es la fuente de verdad";
- "revisa TODO";
- "revisa CURRENT_STATE".

Eso es responsabilidad de este skill.

---

# 2. Resolución de repositorios

Usar en este orden:

1. `owner/repo` explícito.
2. URL GitHub explícita.
3. Alias o proyecto explícitamente mencionado por el usuario.
4. Repositorio activo de la tarea/herramienta, solamente cuando no existe una intención explícita.
5. Búsqueda GitHub por nombre.
6. Preguntar si sigue existiendo ambigüedad.

La intención explícita del usuario tiene prioridad sobre el contexto activo incidental. Por ejemplo, `continúa con el enrutador` resuelve `10minuteswebsite/agente-enrutador` aunque la herramienta tenga activo otro repositorio. Si la intención explícita contradice el contexto activo y no puede resolverse con certeza, preguntar antes de actuar.

Aliases actuales:

| Alias | Repositorio |
|---|---|
| arquitecto, AI-Playbooks, playbooks | `10minuteswebsite/AI-Playbooks` |
| enrutador, router, SuperLinks-Enrutador | `10minuteswebsite/agente-enrutador` |
| cursos, cursos de whatsapp | `10minuteswebsite/agente-cursos` |
| agendador, scheduler | `10minuteswebsite/agente-agendador` |
| precalificador, calificador, prequalifier | `10minuteswebsite/agente-precalificador-inmobiliario` |
| Cata, Cata-IA | `10minuteswebsite/Cata-IA` |

`10minuteswebsite/agente-redes-frontend` está fuera de alcance salvo autorización humana explícita.

Ver [Routing](references/repository-routing.md).

---

# 3. Si el repositorio no existe

Un repo inexistente no es automáticamente un bloqueo.

Si el usuario está creando un proyecto nuevo:

1. Buscar primero repositorios existentes para evitar duplicados.
2. Resolver:
   - owner;
   - nombre;
   - visibilidad;
   - propósito.
3. **Nunca adivinar public/private.**
4. Crear el repositorio en GitHub si las herramientas lo permiten.
5. Verificar que realmente existe.
6. Crear bootstrap durable inicial.
7. Dejar el proyecto listo para futuros agentes.

Seguir [Creación de repositorios](references/repository-creation.md).

Si la herramienta actual no puede crear repositorios, reportar:

`BLOCKED`

y pedir únicamente la acción humana mínima necesaria.

---

# 4. Memoria durable que debe leerse

Después de localizar el repo, inspeccionar cuando existan:

- `AGENTS.md`
- `CLAUDE.md`
- `opencode.json`
- `moving.md`
- `TODO.md`
- `HANDOFF.md`
- `docs/CURRENT_STATE.md`
- README
- contratos
- ADRs/decisiones
- tests relevantes
- workflows relevantes
- commits recientes
- issues relevantes
- PRs abiertos relevantes

No leer todo indiscriminadamente.

Leer primero lo necesario para responder:

- qué hace el proyecto;
- arquitectura actual;
- qué está terminado;
- qué está en progreso;
- qué está bloqueado;
- cuál es el siguiente paso;
- cuáles son las restricciones.

Si documentación antigua contradice código/commits recientes, investigar. No confiar ciegamente en texto obsoleto.

---

# 5. AI-Playbooks como metodología canónica

Para proyectos `10minuteswebsite`, la metodología canónica vive en:

`10minuteswebsite/AI-Playbooks`

Cuando corresponda:

1. Leer `ARCHITECT_BOOTSTRAP.md`.
2. Leer el estándar actual de interoperabilidad de agentes.
3. Leer ADRs relevantes.
4. Preferir GitHub actual sobre las instrucciones embebidas en este Skill si el estándar fue actualizado después.

Este Skill es el **arrancador operativo**.

AI-Playbooks es la **autoridad durable**.

---

# 6. Flujo de trabajo para tareas sustanciales

Para implementación real:

1. Sincronizar/leer la última rama base deseada, normalmente `main`.
2. Crear una rama dedicada a la tarea o continuar la rama autorizada de un PR existente.
3. Inspeccionar antes de editar.
4. Mantener alcance acotado.
5. Preservar arquitectura existente salvo que la tarea exija cambiarla.
6. Implementar.
7. Agregar o actualizar tests.
8. Ejecutar validaciones.
9. Actualizar memoria durable.
10. Commit.
11. Push.
12. Verificar SHA remoto.
13. Crear o actualizar Pull Request.
14. No mergear.
15. No desplegar.
16. Esperar autorización humana para merge/deploy.

Una tarea de código no está terminada porque "funciona en el sandbox".

Debe ser durable y verificable en GitHub.

---

# 7. Definición de terminado

Una tarea sustancial **NO está completa** hasta satisfacer todo lo aplicable:

- tests requeridos ejecutados;
- validaciones ejecutadas;
- memoria durable actualizada;
- cambios relevantes commiteados;
- rama publicada en `origin`;
- SHA remoto verificado;
- PR abierto/actualizado;
- PR contiene evidencia de handoff;
- no hubo merge no autorizado;
- no hubo deploy no autorizado.

Si alguno de esos pasos requeridos no puede completarse:

**NO decir "terminado", "done", "complete" o equivalente.**

Responder:

`BLOCKED`

e incluir:

- paso exacto que falló;
- error relevante;
- qué sí se completó;
- qué falta;
- acción humana mínima requerida.

---

# 8. Handoff durable obligatorio

Antes de cerrar trabajo sustancial, dejar suficiente estado para que otro agente continúe sin esta conversación.

Convención preferida:

## `moving.md`

Mantenerlo corto, estable y navegacional. Debe orientar al siguiente agente hacia `HANDOFF.md`, `TODO.md`, `docs/CURRENT_STATE.md` y las demás fuentes de estado apropiadas. No usarlo como diario de sesión ni actualizarlo con cada cambio operativo.

## `TODO.md`

Actualizar cuando cambie el estado, prioridad o alcance de tareas.

## `docs/CURRENT_STATE.md`

Actualizar cuando cambie:

- arquitectura;
- integración;
- comportamiento runtime;
- feature activation;
- deploy status;
- contratos externos;
- supuestos operativos materiales.

## `HANDOFF.md`

Mantener el contrato de colaboración y la continuidad universal conforme a la convención local. El estado operativo mutable de la sesión debe vivir principalmente en `HANDOFF.md`, `TODO.md` y `docs/CURRENT_STATE.md`.

El objetivo no es escribir una novela.

Git ya conserva historia.

La memoria durable debe responder:

- ¿dónde estamos?
- ¿qué cambió?
- ¿qué sigue?

Ver [Handoff](references/handoff.md).

---

# 9. Pull Request obligatorio para trabajo sustancial

El PR debe indicar:

## Summary
Qué cambió y por qué.

## Tests
Comandos/checks y resultados exactos.

## Durable handoff
Qué archivos de estado fueron actualizados y cuáles no aplicaban.

## Risks / limitations
Riesgos conocidos o `None known`.

## Remaining work
Trabajo restante o `None`.

## Recommended next step
Siguiente acción concreta.

## Deployment
Decir explícitamente si hubo o no deploy.

---

# 10. Validación

Siempre que sea posible:

- revisar diff;
- ejecutar tests;
- ejecutar checks específicos;
- verificar que no se introduzcan secretos;
- ejecutar `git diff --check`;
- verificar rama remota;
- verificar PR;
- revisar CI antes de recomendar merge.

Nunca reutilizar de memoria un conteo de tests viejo.

Reportar el resultado de la ejecución actual.

Ver [Validación](references/validation.md).

---

# 11. Compatibilidad multiagente

## Codex

Usar:

- este Skill;
- GitHub;
- `AGENTS.md`;
- memoria durable del repo;
- AI-Playbooks.

No depender de Project Sources locales para continuidad durable.

## Claude Code

Usar **este mismo Skill canónico** cuando soporte Agent Skills.

El repo puede mantener un `CLAUDE.md` delgado para bootstrap/compatibilidad.

No duplicar toda la política en `CLAUDE.md`.

Ejemplo deseado:

```md
# Claude Code bootstrap

@AGENTS.md
```

o el mecanismo equivalente soportado por la instalación concreta.

## OpenCode

Usar **este mismo Skill** cuando esté instalado en una ruta de skills soportada.

Además respetar:

- `AGENTS.md`
- `opencode.json`
- bootstrap canónico de AI-Playbooks.

No depender del historial de OpenCode.

## Regla de oro

**Un solo Arquitecto Omnicanal.**

No mantener tres versiones divergentes para Codex, Claude y OpenCode.

La fuente canónica del Skill debe vivir en GitHub, preferentemente:

`10minuteswebsite/AI-Playbooks/skills/omnichannel-agent-architect/`

Las instalaciones locales/de producto son copias operativas.

Mientras el Pull Request que introduce esa carpeta no esté fusionado con aprobación humana, describirla como **proposed canonical skill source** o **candidate canonical source**. Solo se vuelve canónica después del merge aprobado.

---

# 12. Proyectos existentes

Al adaptar un repo existente al estándar:

1. No reescribir código funcional.
2. No cambiar dependencias salvo necesidad justificada.
3. No desplegar.
4. No borrar archivos históricos útiles.
5. Conservar reglas locales valiosas.
6. Actualizar/crear:
   - `AGENTS.md`
   - `CLAUDE.md` si aplica
   - `moving.md`
   - `TODO.md`
   - `docs/CURRENT_STATE.md`
   - PR template
   - handoff check cuando corresponda.
7. Correr tests.
8. PR.
9. Human merge.

La migración del estándar debe estar separada de features funcionales.

---

# 13. Proyectos nuevos

Cuando se cree un repo nuevo bajo este estándar, iniciar con:

- `README.md`
- `AGENTS.md`
- `moving.md`
- `TODO.md`
- `HANDOFF.md`
- `docs/PROJECT_CONTEXT.md`
- `docs/CURRENT_STATE.md`
- `.github/pull_request_template.md`
- `CLAUDE.md` cuando aplique
- `opencode.json` cuando aplique
- `agent-handoff-check` cuando corresponda según el estándar canónico vigente

Leer siempre la versión actual de AI-Playbooks antes de generar plantillas.

---

# 14. Seguridad y autoridad humana

Nunca:

- exponer secretos;
- copiar API keys;
- rotar credenciales sin pedido explícito;
- hacer merge sin autorización;
- desplegar sin autorización;
- borrar repositorios sin autorización;
- elegir public/private sin información;
- afirmar push/PR/deploy/test inexistente;
- mezclar tenants/leads;
- cambiar arquitectura solo por preferencia estética.

---

# 15. Qué debe poder hacer el usuario

El objetivo final es que el usuario pueda escribir:

`continúa con el enrutador`

o:

`vamos a trabajar en cursos`

o:

`crea un proyecto nuevo llamado Lucy Voice`

y el Arquitecto:

1. resuelva GitHub;
2. cargue AI-Playbooks;
3. cargue estado durable;
4. determine situación;
5. trabaje;
6. pruebe;
7. documente;
8. commit;
9. push;
10. verifique;
11. PR;
12. deje listo el siguiente handoff.

Si el usuario escribe solo `continúa` y hay varios repos posibles, preguntar únicamente cuál.

---

# 16. Referencias operativas

- [Bootstrap GitHub-first](references/bootstrap.md)
- [Routing](references/repository-routing.md)
- [Creación de repositorios](references/repository-creation.md)
- [Handoff durable](references/handoff.md)
- [Validación](references/validation.md)
