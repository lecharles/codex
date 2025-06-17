#!/usr/bin/env bash
# Demonstration script: start REST API plugin and query via HTTP
set -euo pipefail

GRAPH=demo.json
rm -f "$GRAPH"

echo "== Initializing graph =="
mcp-server --file "$GRAPH" init

echo "== Starting REST API plugin (in background) =="
# Assumes 'flask' is installed and plugin is enabled automatically
mcp-server --file "$GRAPH" shell &
SERVER_PID=$!
sleep 1

echo "== Querying via HTTP =="
curl -s http://localhost:5000/nodes | jq .
curl -s http://localhost:5000/edges | jq .

echo "== Stopping shell/REST API server =="
kill "$SERVER_PID"