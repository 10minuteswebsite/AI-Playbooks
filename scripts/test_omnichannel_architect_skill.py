#!/usr/bin/env python3
"""Structural validator and mutation tests for the Omnichannel Architect skill.

This check validates deterministic, repository-local invariants, including the
candidate and post-merge canonicality states. It intentionally does not replace
the repository secret scan, diff/dependency review, functional testing,
deployment review, or human review of the pull request.
The merge state is inferred from durable repository evidence, not a temporal phrase.
Candidate fixtures intentionally model an unmerged proposal without changing the skill package.
"""

from __future__ import annotations

import re
import shutil
import tempfile
from dataclasses import dataclass
from pathlib import Path
from typing import Callable


ROOT = Path(__file__).resolve().parents[1]
SKILL = Path("skills/omnichannel-agent-architect/SKILL.md")
ROUTING = Path("skills/omnichannel-agent-architect/references/repository-routing.md")
CREATION = Path("skills/omnichannel-agent-architect/references/repository-creation.md")
HANDOFF = Path("skills/omnichannel-agent-architect/references/handoff.md")
VALIDATION = Path("skills/omnichannel-agent-architect/references/validation.md")
OPENAI = Path("skills/omnichannel-agent-architect/agents/openai.yaml")


class ValidationError(AssertionError):
    """A structural invariant is missing or contradictory."""


def read(root: Path, relative_path: Path | str) -> str:
    return (root / relative_path).read_text(encoding="utf-8")


def section(text: str, heading: str, source: str) -> str:
    """Return one Markdown section, including its nested subsections."""
    lines = text.splitlines(keepends=True)
    headings: list[tuple[int, int, str]] = []
    in_fence = False
    for index, line in enumerate(lines):
        if re.match(r"^\s*(```|~~~)", line):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        match = re.match(r"^(?P<marks>#+)\s+(?P<title>.+?)\s*$", line)
        if match:
            headings.append((index, len(match.group("marks")), match.group("title")))
    selected = next((item for item in headings if item[2] == heading), None)
    if selected is None:
        raise ValidationError(f"{source}: missing section {heading!r}")
    start, level, _ = selected
    end = next(
        (index for index, next_level, _ in headings if index > start and next_level <= level),
        len(lines),
    )
    return "".join(lines[start:end])


def require(text: str, fragment: str, source: str) -> None:
    if fragment not in text:
        raise ValidationError(f"{source}: missing required text {fragment!r}")


def require_regex(text: str, pattern: str, source: str) -> None:
    if not re.search(pattern, text, re.IGNORECASE | re.MULTILINE):
        raise ValidationError(f"{source}: missing required pattern {pattern!r}")


def forbid_regex(text: str, pattern: str, source: str) -> None:
    match = re.search(pattern, text, re.IGNORECASE | re.MULTILINE)
    if match:
        line = text.count("\n", 0, match.start()) + 1
        raise ValidationError(f"{source}:{line}: forbidden pattern {pattern!r}")


def require_order(text: str, patterns: list[str], source: str) -> None:
    positions: list[int] = []
    for pattern in patterns:
        match = re.search(pattern, text, re.IGNORECASE)
        if not match:
            raise ValidationError(f"{source}: missing ordered pattern {pattern!r}")
        positions.append(match.start())
    if positions != sorted(positions) or len(set(positions)) != len(positions):
        raise ValidationError(f"{source}: semantic precedence is out of order")


def validate_routing(root: Path) -> None:
    skill_routing = section(read(root, SKILL), "2. Resolución de repositorios", str(SKILL))
    reference_rules = section(read(root, ROUTING), "Rules", str(ROUTING))
    ordered = [
        r"owner/repo.*expl[ií]cit",
        r"URL GitHub.*expl[ií]cit",
        r"alias o proyecto.*expl[ií]cit",
        r"repositorio activo.*solamente cuando.*no existe.*intenci[oó]n expl[ií]cita",
        r"b[uú]squeda GitHub",
        r"preguntar.*ambig",
    ]
    require_order(skill_routing, ordered, f"{SKILL} routing section")
    require_order(
        reference_rules,
        [
            r"explicit owner/repo",
            r"explicit GitHub URL",
            r"alias or project explicitly named",
            r"active tool repository only when.*no repository/project intent",
            r"GitHub search",
            r"ambiguous mapping.*ask",
        ],
        f"{ROUTING} Rules section",
    )
    require(skill_routing, "continúa con el enrutador", f"{SKILL} routing section")


def validate_creation(root: Path) -> None:
    skill_creation = section(read(root, SKILL), "13. Proyectos nuevos", str(SKILL))
    reference_bootstrap = section(read(root, CREATION), "Bootstrap", str(CREATION))
    unconditional = (
        "README.md",
        "AGENTS.md",
        "moving.md",
        "TODO.md",
        "HANDOFF.md",
        "docs/PROJECT_CONTEXT.md",
        "docs/CURRENT_STATE.md",
        ".github/pull_request_template.md",
    )
    for source, text in (
        (f"{SKILL} new-project section", skill_creation),
        (f"{CREATION} Bootstrap section", reference_bootstrap),
    ):
        for path in unconditional:
            require(text, path, source)
        for path in ("CLAUDE.md", "opencode.json"):
            require_regex(
                text,
                rf"{re.escape(path)}.*(cuando|when) (app?li\w*|correspond\w*)",
                source,
            )
        require_regex(
            text,
            r"agent-handoff-check.*(cuando|when).*(correspond|apli|standard)",
            source,
        )


def validate_moving(root: Path) -> None:
    skill_handoff = section(read(root, SKILL), "8. Handoff durable obligatorio", str(SKILL))
    skill_moving = section(skill_handoff, "`moving.md`", f"{SKILL} handoff section")
    reference_moving = section(read(root, HANDOFF), "moving.md", str(HANDOFF))
    reference_all = read(root, HANDOFF)
    for source, text, adjectives in (
        (f"{SKILL} moving.md section", skill_moving, ("corto", "estable", "navegacional")),
        (f"{HANDOFF} moving.md section", reference_moving, ("short", "stable", "navigational")),
    ):
        for adjective in adjectives:
            require(text.lower(), adjective, source)
        require_regex(text, r"(no usar|do not use).*(diario|diary)", source)

    for destination in ("HANDOFF.md", "TODO.md", "docs/CURRENT_STATE.md"):
        require(skill_handoff, destination, f"{SKILL} handoff section")
        require(reference_all, destination, str(HANDOFF))
    require_regex(
        skill_handoff,
        r"estado operativo mutable[\s\S]*HANDOFF\.md[\s\S]*TODO\.md[\s\S]*docs/CURRENT_STATE\.md",
        f"{SKILL} handoff section",
    )
    require_regex(
        reference_all,
        r"Mutable operational state belongs[\s\S]*HANDOFF\.md[\s\S]*TODO\.md[\s\S]*docs/CURRENT_STATE\.md[\s\S]*not in `moving\.md`",
        str(HANDOFF),
    )
    # These affirmative formulations turn moving.md into mutable session memory.
    forbidden = (
        r"moving\.md\s+(?:must|should|debe|incluye|contains|registra|records).*(?:current state|estado actual)",
        r"moving\.md\s+(?:must|should|debe|incluye|contains|registra|records).*(?:completed work|trabajo completado)",
        r"moving\.md\s+(?:must|should|debe|incluye|contains|registra|records).*(?:operational risks|riesgos operativos)",
        r"moving\.md\s+(?:must|should|debe|incluye|contains|registra|records).*(?:PRs?|commits?).*(?:history|historial|log|registro)",
        r"(?:use|usar) `?moving\.md`?.*(?:work diary|session diary|diario de trabajo|diario de sesi[oó]n)",
    )
    combined = f"{skill_handoff}\n{reference_all}"
    for pattern in forbidden:
        forbid_regex(combined, pattern, "moving.md policy")


def validate_canonicality(root: Path) -> None:
    install = read(root, "skills/omnichannel-agent-architect/INSTALL.md")
    readme = read(root, "README.md")
    context = read(root, "docs/PROJECT_CONTEXT.md")
    todo = read(root, "TODO.md")
    current_state = read(root, "docs/CURRENT_STATE.md")
    post_merge = bool(
        re.search(r"PR #15\s+(?:was human-approved and )?merged into `main`", readme, re.I)
        and re.search(r"PR #15\s+is merged into `main`", current_state, re.I)
        and re.search(r"^- \[[xX]\] \*\*TODO-006\b", todo, re.M)
    )
    if post_merge:
        for source, text in (("README.md", readme), ("INSTALL.md", install), ("docs/PROJECT_CONTEXT.md", context)):
            require_regex(text, r"skills/omnichannel-agent-architect/", source)
            require_regex(text, r"(?:canonical|can[oó]nica).*(?:main|source|fuente)", source)
        require_regex(install, r"(?:now|ahora)\s+the\s+canonical\s+skill\s+source|canonical\s+skill\s+source;", "INSTALL.md")
        require_regex(install, r"PR #15.*(?:merged|fusionado).*`main`", "INSTALL.md")
        require_regex(todo, r"^- \[[xX]\] \*\*TODO-006\b", "TODO.md")
    else:
        require_regex(todo, r"^- \[ \] \*\*TODO-006\b", "TODO.md")
        if re.search(r"^- \[[xX]\].*TODO-006\b", todo, re.MULTILINE):
            raise ValidationError("TODO.md: TODO-006 cannot be completed before the merge evidence")
        for source, text in (("INSTALL.md", install), ("docs/PROJECT_CONTEXT.md", context)):
            require_regex(text, r"(?:candidate|proposed).*canonical", source)
            require_regex(text, r"(?:becomes?|vuelve).*can[oó]nic[ao].*(?:after.*human-approved.*merge|despu[eé]s.*merge aprobado)", source)
        forbid_regex(
            "\n".join((readme, install, context, todo)),
            r"(?:is|es|ahora es|now)\s+(?:the |la )?effective\s+canonical|(?:is|es|ahora es|now)\s+(?:the |la )?canonical\s+source.*(?:main|effective)",
            "pre-merge canonicality policy",
        )
    package = "\n".join(
        path.read_text(encoding="utf-8")
        for path in sorted((root / "skills/omnichannel-agent-architect").rglob("*"))
        if path.is_file()
    )
    forbid_regex(
        package,
        r"(?:draft\s+)?\b(?:branch|rama|PR|pull request)\b.{0,50}\b(?:is|es|becomes?|se vuelve)\b.{0,20}(?:the |la )?(?:effective )?(?:canonical|can[oó]nic[ao])",
        "skill canonicality policy",
    )
    open_items = re.findall(r"^- \[ \].*TODO-006\b", todo, re.MULTILINE)
    completed_items = re.findall(r"^- \[[xX]\].*TODO-006\b", todo, re.MULTILINE)
    if len(open_items) > 1 or len(completed_items) > 1 or (open_items and completed_items):
        raise ValidationError("TODO.md: TODO-006 cannot be open and completed simultaneously")


def yaml_scalar(text: str, key: str, source: str) -> str:
    match = re.search(rf"^\s*{re.escape(key)}:\s*(.+?)\s*$", text, re.MULTILINE)
    if not match:
        raise ValidationError(f"{source}: missing YAML key {key!r}")
    value = match.group(1).strip()
    if len(value) < 2 or value[0] != value[-1] or value[0] not in "\"'":
        raise ValidationError(f"{source}: {key!r} must be a quoted scalar")
    return value[1:-1]


def validate_openai(root: Path) -> None:
    prompt = yaml_scalar(read(root, OPENAI), "default_prompt", str(OPENAI))
    for capability in (
        "crear", "continuar", "inspeccionar", "revisar", "implementar", "depurar", "migrar", "handoff"
    ):
        require_regex(prompt, rf"\b{capability}\b", f"{OPENAI} default_prompt")
    for constraint in (
        r"GitHub.*fuente durable",
        r"reconstruye.*estado",
        r"sin depender de chats anteriores",
        r"Codex.*Claude Code.*OpenCode",
        r"nunca.*merge.*sin autorizaci[oó]n humana",
        r"nunca.*deploy.*sin autorizaci[oó]n humana",
    ):
        require_regex(prompt, constraint, f"{OPENAI} default_prompt")


SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
    "AWS access key": re.compile(r"\bAKIA[0-9A-Z]{16}\b"),
    "secret assignment": re.compile(
        r"(?i)\b(?:api[_-]?key|client[_-]?secret|password)\s*[:=]\s*['\"][^'\"<>]{12,}['\"]"
    ),
}


def validate_security(root: Path) -> None:
    skill = read(root, SKILL)
    routing = read(root, ROUTING)
    excluded = section(routing, "Excluded", str(ROUTING))
    require(skill, "`10minuteswebsite/agente-redes-frontend` está fuera de alcance", str(SKILL))
    require(excluded, "`10minuteswebsite/agente-redes-frontend`", f"{ROUTING} Excluded section")
    require_regex(excluded, r"No modificar salvo autorizaci[oó]n expl[ií]cita", f"{ROUTING} Excluded section")
    security = section(read(root, SKILL), "14. Seguridad y autoridad humana", str(SKILL))
    require_regex(security, r"merge sin autorizaci[oó]n", f"{SKILL} security section")
    require_regex(security, r"desplegar sin autorizaci[oó]n", f"{SKILL} security section")

    for path in sorted((root / "skills/omnichannel-agent-architect").rglob("*")):
        if not path.is_file():
            continue
        text = path.read_text(encoding="utf-8")
        if "/Users/mariodavila" in text:
            raise ValidationError(f"{path.relative_to(root)}: personal path found")
        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(text):
                raise ValidationError(f"{path.relative_to(root)}: possible embedded {name}")


def validate_scope_description(root: Path) -> None:
    validation = read(root, VALIDATION)
    require_regex(validation, r"Automated structural invariants", str(VALIDATION))
    require_regex(validation, r"Separate PR checks", str(VALIDATION))
    require_regex(validation, r"Human review", str(VALIDATION))
    for item in ("secret", "diff", "dependenc", "functional", "deploy"):
        require_regex(validation, item, str(VALIDATION))


def validate_repository(root: Path) -> None:
    validate_routing(root)
    validate_creation(root)
    validate_moving(root)
    validate_canonicality(root)
    validate_openai(root)
    validate_security(root)
    validate_scope_description(root)


@dataclass(frozen=True)
class Mutation:
    name: str
    path: Path
    mutate: Callable[[str], str]


def replace_once(old: str, new: str) -> Callable[[str], str]:
    def mutation(text: str) -> str:
        if text.count(old) != 1:
            raise AssertionError(f"mutation fixture expected exactly one occurrence of {old!r}")
        return text.replace(old, new, 1)

    return mutation


MUTATIONS = (
    Mutation(
        "routing-active-before-explicit-alias",
        SKILL,
        replace_once(
            "3. Alias o proyecto explícitamente mencionado por el usuario.\n4. Repositorio activo de la tarea/herramienta, solamente cuando no existe una intención explícita.",
            "3. Repositorio activo de la tarea/herramienta, solamente cuando no existe una intención explícita.\n4. Alias o proyecto explícitamente mencionado por el usuario.",
        ),
    ),
    Mutation(
        "bootstrap-remove-handoff",
        SKILL,
        replace_once(
            "- `TODO.md`\n- `HANDOFF.md`\n- `docs/PROJECT_CONTEXT.md`",
            "- `TODO.md`\n- `docs/PROJECT_CONTEXT.md`",
        ),
    ),
    Mutation(
        "bootstrap-remove-project-context",
        CREATION,
        replace_once("- docs/PROJECT_CONTEXT.md\n", ""),
    ),
    Mutation(
        "moving-becomes-mutable-state-log",
        HANDOFF,
        replace_once(
            "Keep it short, stable, and navigational. It routes the next agent to the durable collaboration contract, backlog, current state, and other appropriate sources. Do not use it as a mutable operational diary.",
            "Keep it short, stable, and navigational. It routes the next agent to the durable collaboration contract, backlog, current state, and other appropriate sources. Do not use it as a mutable operational diary. moving.md must contain current state, completed work, operational risks, PR/commit history, and a session diary.",
        ),
    ),
    Mutation(
        "premature-canonicality",
        Path("skills/omnichannel-agent-architect/INSTALL.md"),
        replace_once(
            "That directory is now the canonical skill source; future changes happen there first",
            "That Draft PR branch is now the effective canonical skill source; future changes happen there first",
        ),
    ),
    Mutation(
        "todo-006-open-and-completed",
        Path("TODO.md"),
        lambda text: text + "\n- [x] **TODO-006 — Publish the canonical Arquitecto Omnicanal skill**\n",
    ),
    Mutation(
        "openai-remove-debug-capability",
        OPENAI,
        replace_once(", depurar", ""),
    ),
    Mutation(
        "remove-human-merge-prohibition",
        OPENAI,
        replace_once("nunca hagas merge ni deploy sin autorización humana", "nunca hagas deploy sin autorización humana"),
    ),
    Mutation(
        "frontend-repo-enters-scope",
        ROUTING,
        replace_once("No modificar salvo autorización explícita.", "Repositorio activo dentro del alcance normal."),
    ),
    Mutation(
        "introduce-personal-path",
        Path("skills/omnichannel-agent-architect/INSTALL.md"),
        lambda text: text + "\nInstall from `/Users/mariodavila/private-skill`.\n",
    ),
)


def replace_all(text: str, replacements: list[tuple[str, str]]) -> str:
    for old, new in replacements:
        if old not in text:
            raise AssertionError(f"state fixture expected text {old!r}")
        text = text.replace(old, new)
    return text


def run_canonicality_state_tests(root: Path) -> list[str]:
    """Exercise candidate and post-merge canonicality as semantic states."""
    cases = {
        "candidate-state-canonical-claim": (False, [
            ("PR #15 was human-approved and merged into `main`.", "PR #15 proposes the skill for `main`."),
        ]),
        "candidate-state-todo-completed": (False, [
            ("PR #15 is merged into `main`", "PR #15 is awaiting human-approved merge into `main`"),
        ]),
        "candidate-state-correct": (True, [
            ("PR #15 was human-approved and merged into `main`.", "PR #15 proposes the skill for `main`."),
            ("PR #15 is merged into `main`", "PR #15 is awaiting human-approved merge into `main`"),
            ("- [x] **TODO-006", "- [ ] **TODO-006"),
            ("That directory is now the canonical skill source; future changes happen there first", "That directory is the proposed canonical skill source. It becomes canonical after the human-approved merge"),
            ("canonical shared skill source merged by PR #15", "candidate canonical shared skill source proposed by PR #15"),
            ("PR #15 established `skills/omnichannel-agent-architect/` as the single source shared by the three supported agent clients.", "PR #15 proposes `skills/omnichannel-agent-architect/` as the candidate canonical source. It becomes canonical after the human-approved merge."),
        ]),
        "post-merge-canonical-state": (True, []),
        "post-merge-candidate-only": (False, [
            ("That directory is now the canonical skill source; future changes happen there first", "That directory is the proposed candidate skill source; it remains pending merge"),
        ]),
    }
    results: list[str] = []
    with tempfile.TemporaryDirectory(prefix="omnichannel-canonicality-") as temp:
        for name, (should_pass, replacements) in cases.items():
            fixture = Path(temp) / name
            shutil.copytree(root, fixture, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            if replacements:
                for relative in ("README.md", "TODO.md", "docs/CURRENT_STATE.md", "docs/PROJECT_CONTEXT.md", "skills/omnichannel-agent-architect/INSTALL.md"):
                    path = fixture / relative
                    text = path.read_text(encoding="utf-8")
                    applicable = [(old, new) for old, new in replacements if old in text]
                    path.write_text(replace_all(text, applicable), encoding="utf-8")
            try:
                validate_canonicality(fixture)
            except ValidationError:
                if should_pass:
                    raise AssertionError(f"canonicality state {name!r} was rejected")
                results.append(name)
            else:
                if not should_pass:
                    raise AssertionError(f"canonicality state {name!r} was incorrectly accepted")
                results.append(name)
    return results


def run_mutations(root: Path) -> list[tuple[str, str]]:
    results: list[tuple[str, str]] = []
    with tempfile.TemporaryDirectory(prefix="omnichannel-validator-") as temp:
        fixture = Path(temp) / "repo"
        for mutation in MUTATIONS:
            if fixture.exists():
                shutil.rmtree(fixture)
            shutil.copytree(root, fixture, ignore=shutil.ignore_patterns(".git", "__pycache__"))
            target = fixture / mutation.path
            target.write_text(mutation.mutate(target.read_text(encoding="utf-8")), encoding="utf-8")
            try:
                if mutation.name == "moving-becomes-mutable-state-log":
                    mutated_moving = section(
                        read(fixture, HANDOFF), "moving.md", f"{HANDOFF} moving.md section"
                    ).lower()
                    for adjective in ("short", "stable", "navigational"):
                        require(mutated_moving, adjective, "moving.md mutation preservation")
                validate_repository(fixture)
            except ValidationError as error:
                if mutation.name == "moving-becomes-mutable-state-log":
                    if "moving.md policy" not in str(error):
                        raise AssertionError(
                            "moving-becomes-mutable-state-log was rejected for a reason "
                            f"other than mutable moving.md policy: {error}"
                        ) from error
                results.append((mutation.name, str(error)))
            else:
                raise AssertionError(
                    f"mutation {mutation.name!r} was incorrectly accepted by the validator"
                )
    return results


def main() -> int:
    validate_repository(ROOT)
    print("Structural validation passed for the real repository content.")
    results = run_mutations(ROOT)
    for name, reason in results:
        print(f"MUTATION DETECTED: {name}: {reason}")
    print(f"Mutation testing passed: {len(results)}/{len(MUTATIONS)} invalid variants rejected.")
    state_results = run_canonicality_state_tests(ROOT)
    print(f"Canonicality state tests passed: {len(state_results)}/5 candidate/post-merge cases.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
