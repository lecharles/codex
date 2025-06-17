#!/usr/bin/env bash
# Demonstration script: initialize graph, add nodes/edges, and query
set -euo pipefail

GRAPH=demo.json
rm -f "$GRAPH"

echo "== Initializing graph =="
mcp-server --file "$GRAPH" init

echo "== Adding nodes =="
mcp-server --file "$GRAPH" node add Account --id acct1 -a name=AcmeCorp
mcp-server --file "$GRAPH" node add Contact --id c1 -a name="John Doe"

echo "== Adding edge =="
mcp-server --file "$GRAPH" edge add acct1 c1 parent_of

echo "== Nodes =="
mcp-server --file "$GRAPH" query nodes

echo "== Edges =="
mcp-server --file "$GRAPH" query edges