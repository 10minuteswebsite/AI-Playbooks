# Repository routing

## Canonical

- AI-Playbooks / arquitecto / playbooks -> `10minuteswebsite/AI-Playbooks`

## Active

- enrutador / router / SuperLinks-Enrutador -> `10minuteswebsite/agente-enrutador`
- cursos / cursos de whatsapp -> `10minuteswebsite/agente-cursos`
- agendador / scheduler -> `10minuteswebsite/agente-agendador`
- precalificador / calificador / prequalifier -> `10minuteswebsite/agente-precalificador-inmobiliario`
- Cata / Cata-IA -> `10minuteswebsite/Cata-IA`

## Excluded

`10minuteswebsite/agente-redes-frontend`

No modificar salvo autorización explícita.

## Rules

- explicit owner/repo beats every other source
- explicit GitHub URL beats aliases and active tool context
- an alias or project explicitly named by the user beats incidental active tool context
- use the active tool repository only when the user expressed no repository/project intent
- ambiguous mapping -> ask
- if explicit intent conflicts with active context and cannot be resolved with certainty -> ask before acting
- `continúa con el enrutador` -> `10minuteswebsite/agente-enrutador`, even when another repository is active
- bare "continúa" with ambiguous repo -> ask
- never route from stale chat memory alone
- verify current repo existence before work
