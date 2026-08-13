# Validation

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
