"""Unit tests for the core graph engine."""

from mcp_server.engine import Graph, Node, Edge


def test_node_edge_graph_basic():
    node = Node("1", "Account", {"name": "Test"})
    graph = Graph()
    graph.add_node(node)
    assert "1" in graph.nodes

    edge = Edge("1", "1", "self")
    graph.add_edge(edge)
    assert edge in graph.edges
    graph.remove_edge(edge)
    assert edge not in graph.edges
    graph.remove_node("1")
    assert "1" not in graph.nodes