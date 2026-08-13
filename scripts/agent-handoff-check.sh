#!/usr/bin/env bash
set -euo pipefail

body="${PR_BODY:-}"
for section in "## Summary" "## Tests" "## Durable handoff" "## Risks / limitations" "## Remaining work" "## Recommended next step" "## Deployment"; do
  grep -Fq "$section" <<<"$body" || { echo "Missing required PR section: $section" >&2; exit 1; }
done

grep -Eiq 'Result:[[:space:]]*[^[:space:]]|[[:space:]](pass|passed|success|successful)[[:space:].,:]' <<<"$body" || {
  echo "PR tests section must contain non-blank evidence." >&2
  exit 1
}

changed="$(git diff --name-only "$BASE_SHA" "$HEAD_SHA")"
substantive='(^|/)(src|api|app|lib|test|tests)/|(^|/)(package\.json|package-lock\.json|vercel\.json|supabase/|\.github/workflows/)'
if grep -Eq "$substantive" <<<"$changed"; then
  for file in HANDOFF.md TODO.md docs/CURRENT_STATE.md; do
    grep -qx "$file" <<<"$changed" || { echo "Substantive PR must include $file" >&2; exit 1; }
  done
fi

echo "Agent handoff evidence passed."
