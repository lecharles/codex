"""Core graph engine: Graph, Node, and Edge classes."""


class Node:
    """Represents a node in the memory graph."""
    def __init__(self, node_id, node_type, attributes=None):
        self.id = node_id
        self.type = node_type
        self.attributes = attributes or {}


class Edge:
    """Represents a typed relationship between two nodes."""
    def __init__(self, source, target, edge_type):
        self.source = source
        self.target = target
        self.type = edge_type


class Graph:
    """In-memory graph containing nodes and edges."""
    def __init__(self):
        self.nodes = {}
        self.edges = []

    def add_node(self, node):
        self.nodes[node.id] = node

    def remove_node(self, node_id):
        self.nodes.pop(node_id, None)
        self.edges = [e for e in self.edges if e.source != node_id and e.target != node_id]

    def add_edge(self, edge):
        self.edges.append(edge)

    def remove_edge(self, edge):
        self.edges = [e for e in self.edges if e is not edge]