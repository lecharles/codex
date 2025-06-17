#!/usr/bin/env bash
# Script to initialize GitHub Project board for MCP Server Roadmap
set -euo pipefail

# Create or reuse project
PROJECT_JSON=$(gh project create --owner lecharles --title "MCP Server Roadmap" --format json)
PROJECT_NUMBER=$(echo "$PROJECT_JSON" | jq -r .number)
echo "Created Project #$PROJECT_NUMBER: MCP Server Roadmap"

# Create or ensure 'Status' single-select field (ignore errors if already exists)
gh project field-create "$PROJECT_NUMBER" \
  --owner lecharles \
  --name Status \
  --data-type SINGLE_SELECT \
  --single-select-options "To do" \
  --single-select-options "In progress" \
  --single-select-options "Done" || true
echo "[OK] Status field created or already present"

# Add issues 6 & 7 to the project in 'To do'
for issue in 6 7; do
  gh project item-add "$PROJECT_NUMBER" --owner lecharles --url https://github.com/lecharles/codex/issues/$issue || true
  gh project item-edit "$PROJECT_NUMBER" --owner lecharles --url https://github.com/lecharles/codex/issues/$issue --field Status="To do" || true
  echo "[OK] Issue #$issue added to 'To do'"
done
echo "All specified issues assigned to 'To do'"