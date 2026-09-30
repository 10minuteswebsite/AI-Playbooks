# MCP USAGE GUIDANCE

## OBJETIVO

El MCP no debe limitarse a exponer funcionalidades. Debe enseñar al agente cuándo usar cada capacidad, en qué orden y para qué objetivo del usuario.

La meta es evitar que un cliente como Muse vea muchas tools pero no sepa cómo convertir la intención del usuario en una acción.

## ARQUITECTURA

### 1. Server Instructions

Define instrucciones globales del servidor MCP:

- qué resuelve la plataforma
- cómo interpretar intenciones
- qué workflows principales existen
- qué proponer cuando el usuario no sabe por dónde comenzar

Ejemplo:

```text
This MCP manages real-estate marketing workflows.

When the user expresses a goal instead of naming a tool, map the goal to the appropriate workflow.

If the user wants more leads, propose lead-generation.
If the user wants to launch advertising, propose campaign-launch.
If the user wants to follow up existing leads, propose lead-followup.

Do not ask the user to choose among raw tools unless technically necessary.
Guide the user by business objective.
```

### 2. Tool Descriptions

Cada tool debe explicar cuándo usarla, no solo qué ejecuta.

Formato recomendado:

```text
Purpose:
When to use:
Do not use when:
Required context:
Expected result:
Related next actions:
```

Ejemplo:

```text
create_campaign

Purpose:
Creates a marketing campaign.

When to use:
Use when the user wants to launch, duplicate or configure a campaign.

Do not use when:
The user only wants analytics or contact management.

Typical workflow:
inspect_account → create_campaign → configure_audience → publish_campaign
```

### 3. MCP Prompts

Publica prompts para los casos de uso principales:

`launch_campaign`

`generate_real_estate_leads`

`follow_up_leads`

`create_listing_funnel`

`analyze_campaign`

Cada prompt debe convertir un objetivo en un workflow.

Ejemplo:

```text
Goal: Generate real-estate leads

1. Inspect available context.
2. Determine property, market and audience.
3. Recommend the appropriate workflow.
4. Ask only for missing required information.
5. Execute tools in sequence.
6. Confirm the result.
7. Suggest the logical next action.
```

### 4. Skills

Si el cliente soporta la extensión:

`io.modelcontextprotocol/skills`

publica Skills para workflows complejos.

Ejemplo de `SKILL.md`:

```yaml
---
name: lead-generation
description: Use when the user wants to generate, capture or qualify new leads using the platform.
---
```

Contenido:

```text
# Lead Generation

Trigger intents:
want more leads
capture prospects
run lead ads
generate buyer leads
generate seller leads

Workflow:
1. Inspect existing configuration.
2. Determine campaign objective.
3. Collect only missing required inputs.
4. Select the correct tools.
5. Execute them in dependency order.
6. Validate completion.
7. Recommend the next relevant action.

Never:
Ask the user to select raw MCP tools.
Invent configuration values.
Execute destructive actions without required confirmation.
```

Skills son una extensión del MCP. No asumas que todos los clientes las soportan.

## COMPATIBILIDAD

El diseño debe funcionar aunque Muse NO soporte Skills.

Prioridad:

```text
SERVER INSTRUCTIONS
↓
TOOL DESCRIPTIONS
↓
PROMPTS
↓
SKILLS when supported
```

Las reglas críticas nunca deben existir solo dentro de un Skill.

## MODELO DE DECISIÓN

Correcto:

```text
USER INTENT
↓
USE CASE
↓
WORKFLOW
↓
REQUIRED CONTEXT
↓
TOOLS
↓
VALIDATION
↓
NEXT ACTION
```

Incorrecto:

```text
USER
↓
LIST OF TOOLS
↓
GUESS
```

## CATÁLOGO DE USE CASES

Usa este formato:

```text
USE_CASE_ID
User intents
When to propose
Required information
Workflow
Tools involved
Success condition
Next suggested actions
```

## PRUEBAS OBLIGATORIAS

Prueba desde un cliente que no conozca tu plataforma:

```text
"I want more clients."
"I want to advertise a property."
"I have 200 leads and want to follow them up."
"I don't know what to do. What can this platform help me with?"
```

El agente debe orientar y proponer un workflow concreto.

Si solo enumera tools, la implementación NO está terminada.

## RESULTADO ESPERADO

El MCP debe comportarse como:

`capabilities + operating manual + workflows`

y no solamente como:

`API endpoints exposed as tools`
