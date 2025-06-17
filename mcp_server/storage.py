"""JSON persistence for MCP Server graph."""
import json

from mcp_server.engine import Graph, Node, Edge


def save_graph(graph, file_path):
    """Serialize the graph to a JSON file."""
    data = {
        "nodes": [
            {"id": n.id, "type": n.type, "attributes": n.attributes}
            for n in graph.nodes.values()
        ],
        "edges": [
            {"source": e.source, "target": e.target, "type": e.type}
            for e in graph.edges
        ],
    }
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)


def load_graph(file_path):
    """Load the graph from a JSON file."""
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    graph = Graph()
    for n in data.get("nodes", []):
        node = Node(n["id"], n["type"], n.get("attributes"))
        graph.add_node(node)
    for e in data.get("edges", []):
        edge = Edge(e["source"], e["target"], e["type"])
        graph.add_edge(edge)
    return graph