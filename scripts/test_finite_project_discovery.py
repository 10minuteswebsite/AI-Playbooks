#!/usr/bin/env python3
"""Verify the architect's finite and proportional new-project discovery contract."""

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def main() -> int:
    discovery = (ROOT / "playbooks" / "finite-project-discovery.md").read_text(encoding="utf-8")
    architect = (ROOT / "playbooks" / "software-architect.md").read_text(encoding="utf-8")
    core = (ROOT / "playbooks" / "software-delivery-core.md").read_text(encoding="utf-8")
    bootstrap = (ROOT / "ARCHITECT_BOOTSTRAP.md").read_text(encoding="utf-8")

    required_discovery_rules = (
        "one concise question per interaction",
        "ceilings, not targets",
        "Simple:",
        "Moderate:",
        "Complex or high-risk:",
        "Sufficiency test",
        "Project brief",
        "Architecture blueprint",
        "Do not impose a universal waterfall gate",
    )
    for rule in required_discovery_rules:
        assert rule in discovery, f"missing finite-discovery rule: {rule}"

    for document in (architect, core, bootstrap):
        assert "finite" in document.lower()
        assert "one" in document.lower() and "question" in document.lower()

    assert "finite-project-discovery.md" in architect
    assert "finite-project-discovery.md" in core
    assert "playbooks/finite-project-discovery.md" in bootstrap
    print("Finite project discovery tests passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
