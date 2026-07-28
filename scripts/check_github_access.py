#!/usr/bin/env python3
"""Verify GitHub repository access without guessing its visibility."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
from urllib.parse import urlparse


def repository_slug(value: str) -> str:
    candidate = value.strip().removesuffix(".git")
    if candidate.startswith("git@github.com:"):
        candidate = candidate.split(":", 1)[1]
    elif "://" in candidate:
        parsed = urlparse(candidate)
        if parsed.hostname != "github.com":
            raise ValueError("Only github.com repository URLs are supported")
        candidate = parsed.path.strip("/")
    if candidate.count("/") != 1:
        raise ValueError("Expected a GitHub repository as owner/name or a github.com URL")
    return candidate


def command_succeeds(command: list[str]) -> bool:
    return subprocess.run(command, capture_output=True, text=True, check=False).returncode == 0


def verify(value: str) -> tuple[bool, str]:
    slug = repository_slug(value)
    url = f"https://github.com/{slug}.git"
    if command_succeeds(["git", "ls-remote", "--exit-code", url, "HEAD"]):
        return True, f"Git access verified for {slug}."
    if shutil.which("gh") and command_succeeds(["gh", "repo", "view", slug, "--json", "nameWithOwner"]):
        return True, f"Authenticated GitHub access verified for {slug}."
    return False, (
        f"Access to {slug} could not be verified. This does not prove the repository is private. "
        "Connect or authorize GitHub, confirm the repository link, and try again. "
        "Do not paste credentials or tokens into chat."
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repository", help="GitHub owner/name or repository URL")
    args = parser.parse_args()
    try:
        accessible, message = verify(args.repository)
    except ValueError as error:
        print(error)
        return 2
    print(message)
    return 0 if accessible else 3


if __name__ == "__main__":
    sys.exit(main())
