# Validation

## Automated structural invariants

The dependency-free structural validator checks localized routing precedence,
repository bootstrap contents, `moving.md` semantics, candidate canonicality,
OpenAI agent metadata, and selected scope and authority boundaries. Its mutation
suite proves that known invalid variants are rejected.

This validator is intentionally narrower than a complete Pull Request review.

## Separate PR checks

- run the repository secret scan; structural validation is not a substitute
- inspect the actual diff and changed-file scope
- review dependency changes with the appropriate ecosystem tooling
- run functional and application-specific tests when runtime behavior changes
- inspect deployment configuration and verify that no deploy occurred without authorization
- validate applicable YAML and JSON syntax

## Human review

A reviewer must still evaluate whether the change is coherent, whether the diff
matches the requested scope, whether risks are acceptable, and whether merge or
deployment should be authorized.

## Always
- inspect diff
- check no secrets
- validate scope
- git diff --check when possible
- remote verify if claiming completion

## Application
- run documented test suite
- run task-specific tests
- report current result, not remembered result

## Workflows
- validate syntax
- least privilege
- no secret values
- fixtures when practical
- document manual repo settings

## Before merge recommendation
- CI/checks
- conflicts/mergeability
- changed files
- config/deploy implications
- unresolved comments

## BLOCKED
Use when a required durable completion step cannot be performed.
Never call work complete if push/PR/verification is missing.
