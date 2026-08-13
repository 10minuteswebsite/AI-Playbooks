#!/usr/bin/env python3
"""Regression checks for the proposed Arquitecto Omnicanal skill in PR #15."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL_ROOT = ROOT / "skills" / "omnichannel-agent-architect"


def read(relative_path: str) -> str:
    return (ROOT / relative_path).read_text(encoding="utf-8")


def require(text: str, fragment: str, source: str) -> None:
    if fragment not in text:
        raise AssertionError(f"{source} is missing required text: {fragment}")


def require_any(text: str, fragments: tuple[str, ...], source: str) -> None:
    if not any(fragment in text for fragment in fragments):
        raise AssertionError(f"{source} is missing one of required texts: {fragments}")


def require_order(text: str, fragments: list[str], source: str) -> None:
    positions = [text.find(fragment) for fragment in fragments]
    if -1 in positions or positions != sorted(positions):
        raise AssertionError(f"{source} does not preserve required order: {fragments}")


def main() -> None:
    skill = read("skills/omnichannel-agent-architect/SKILL.md")
    routing = read(
        "skills/omnichannel-agent-architect/references/repository-routing.md"
    )
    creation = read(
        "skills/omnichannel-agent-architect/references/repository-creation.md"
    )
    handoff = read("skills/omnichannel-agent-architect/references/handoff.md")
    openai = read("skills/omnichannel-agent-architect/agents/openai.yaml")

    require_order(
        skill,
        [
            "`owner/repo` explícito",
            "URL GitHub explícita",
            "Alias o proyecto explícitamente mencionado",
            "Repositorio activo de la tarea/herramienta",
            "Búsqueda GitHub por nombre",
            "Preguntar si sigue existiendo ambigüedad",
        ],
        "SKILL.md routing",
    )
    require(routing, "`continúa con el enrutador`", "repository-routing.md")
    require(routing, "even when another repository is active", "repository-routing.md")
    require(skill, "preguntar antes de actuar", "SKILL.md routing conflict rule")

    for required_path in (
        "README.md",
        "AGENTS.md",
        "moving.md",
        "TODO.md",
        "HANDOFF.md",
        "docs/PROJECT_CONTEXT.md",
        "docs/CURRENT_STATE.md",
        ".github/pull_request_template.md",
        "CLAUDE.md",
        "opencode.json",
        "agent-handoff-check",
    ):
        require(skill, required_path, "SKILL.md new-repository bootstrap")
        require(creation, required_path, "repository-creation.md bootstrap")

    for source_name, source in (("SKILL.md", skill), ("handoff.md", handoff)):
        require(source, "short" if source_name == "handoff.md" else "corto", source_name)
        require(
            source,
            "mutable operational diary" if source_name == "handoff.md" else "diario de sesión",
            source_name,
        )
        require(source, "HANDOFF.md", source_name)
        require(source, "TODO.md", source_name)
        require(source, "docs/CURRENT_STATE.md", source_name)

    for relative_path in (
        "README.md",
        "HANDOFF.md",
        "TODO.md",
        "docs/PROJECT_CONTEXT.md",
        "docs/CURRENT_STATE.md",
    ):
        document = read(relative_path)
        require(document, "PR #15", relative_path)
        if relative_path != "TODO.md":
            require(document.lower(), "merge", relative_path)

    for relative_path in (
        "skills/omnichannel-agent-architect/INSTALL.md",
        "skills/omnichannel-agent-architect/SKILL.md",
    ):
        document = read(relative_path).lower()
        require(document, "candidate canonical", relative_path)
        require_any(
            document,
            ("human-approved merge", "merge aprobado"),
            relative_path,
        )

    todo = read("TODO.md")
    require(todo, "- [ ] **TODO-006", "TODO.md")

    for behavior in (
        "crear",
        "continuar",
        "inspeccionar",
        "revisar",
        "implementar",
        "depurar",
        "migrar",
        "handoff GitHub-first",
        "fuente durable de verdad",
        "sin depender de chats anteriores",
        "Codex, Claude Code y OpenCode",
        "nunca hagas merge ni deploy sin autorización humana",
    ):
        require(openai, behavior, "agents/openai.yaml")

    require(skill, "`10minuteswebsite/agente-redes-frontend` está fuera de alcance", "SKILL.md")
    if "/Users/" in "\n".join(
        path.read_text(encoding="utf-8")
        for path in SKILL_ROOT.rglob("*")
        if path.is_file()
    ):
        raise AssertionError("skill package contains a personal local path")

    print("Omnichannel architect skill checks passed.")


if __name__ == "__main__":
    main()
