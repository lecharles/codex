"""Integration tests for JSON storage."""

import os
import tempfile

from mcp_server.engine import Graph, Node, Edge
from mcp_server.storage import save_graph, load_graph


def test_save_and_load(tmp_path):
    graph = Graph()
    node = Node("1", "Account", {"name": "Test"})
    graph.add_node(node)
    edge = Edge("1", "1", "self")
    graph.add_edge(edge)

    file_path = tmp_path / "graph.json"
    save_graph(graph, str(file_path))
    loaded = load_graph(str(file_path))
    assert "1" in loaded.nodes
    assert len(loaded.edges) == 1