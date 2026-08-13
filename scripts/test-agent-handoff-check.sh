#!/usr/bin/env bash
set -euo pipefail

tmp="$(mktemp -d)"
trap 'rm -rf "$tmp"' EXIT
cp scripts/agent-handoff-check.sh "$tmp/check.sh"
cd "$tmp"
git init -q
git config user.email test@example.invalid
git config user.name test
touch README.md
git add README.md
git commit -qm base
mkdir -p src docs
touch src/change.js HANDOFF.md TODO.md docs/CURRENT_STATE.md
git add .
git commit -qm change
body=$'## Summary\nA change.\n\n## Tests\nResult: passed\n\n## Durable handoff\n- HANDOFF.md, TODO.md, and docs/CURRENT_STATE.md updated\n\n## Risks / limitations\nNone known\n\n## Remaining work\nNone\n\n## Recommended next step\nReview\n\n## Deployment\n- [x] No deployment performed'
PR_BODY="$body" BASE_SHA="$(git rev-parse HEAD~1)" HEAD_SHA="$(git rev-parse HEAD)" bash "$tmp/check.sh"
bad_body="$(printf '%s\n' "$body" | sed '/^## Durable handoff$/d')"
if PR_BODY="$bad_body" BASE_SHA="$(git rev-parse HEAD~1)" HEAD_SHA="$(git rev-parse HEAD)" bash "$tmp/check.sh"; then
  echo "Expected missing-section fixture to fail" >&2
  exit 1
fi
printf '\nchange\n' >> src/change.js
git add src/change.js
git commit -qm missing-handoff-state
if PR_BODY="$body" BASE_SHA="$(git rev-parse HEAD~1)" HEAD_SHA="$(git rev-parse HEAD)" bash "$tmp/check.sh"; then
  echo "Expected missing durable-state fixture to fail" >&2
  exit 1
fi
echo "Agent handoff check fixtures passed."
