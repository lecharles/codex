#!/usr/bin/env bash
# Script to initialize GitHub Project board for MCP Server Roadmap
set -euo pipefail

# Create or reuse project
PROJECT_JSON=$(gh project create --owner lecharles --title "MCP Server Roadmap" --format json)
PROJECT_NUMBER=$(echo "$PROJECT_JSON" | jq -r .number)
echo "Created Project #$PROJECT_NUMBER: MCP Server Roadmap"

# Create 'Status' single-select field
gh project field-create "$PROJECT_NUMBER" --owner lecharles --name Status --type single_select --config '{"options":[{"name":"To do"},{"name":"In progress"},{"name":"Done"}]}'
echo "Added Status field to project"

# Add issues 6 & 7 to the project in 'To do'
for issue in 6 7; do
  gh project item-add "$PROJECT_NUMBER" --owner lecharles --url https://github.com/lecharles/codex/issues/$issue
  gh project item-edit "$PROJECT_NUMBER" --owner lecharles --url https://github.com/lecharles/codex/issues/$issue --field Status="To do"
done
echo "Added issues #6 and #7 to 'To do'"