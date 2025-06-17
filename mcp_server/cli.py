"""CLI entry point for MCP Server Memory Graph."""
import argparse
import json
from uuid import uuid4

from mcp_server.engine import Graph, Node, Edge
from mcp_server.storage import save_graph, load_graph
from mcp_server.shell import start_shell

def main():
    parser = argparse.ArgumentParser(
        prog="mcp_server",
        description="MCP Server Memory Graph CLI"
    )
    parser.add_argument(
        "-f", "--file",
        default="memory_graph.json",
        help="Path to graph JSON file"
    )

    subparsers = parser.add_subparsers(dest="cmd")

    # init command
    subparsers.add_parser("init", help="Initialize a new empty graph")

    # node commands
    node_parser = subparsers.add_parser("node", help="Node operations")
    node_sub = node_parser.add_subparsers(dest="node_cmd")
    node_add = node_sub.add_parser("add", help="Add a node")
    node_add.add_argument("type", help="Node type")
    node_add.add_argument("--id", help="Explicit node ID (UUID if omitted)")
    node_add.add_argument(
        "-a", "--attr",
        action="append",
        help="Attribute as key=value"
    )

    node_rm = node_sub.add_parser("rm", help="Remove a node")
    node_rm.add_argument("id", help="Node ID to remove")

    # edge commands
    edge_parser = subparsers.add_parser("edge", help="Edge operations")
    edge_sub = edge_parser.add_subparsers(dest="edge_cmd")
    edge_add = edge_sub.add_parser("add", help="Add an edge")
    edge_add.add_argument("source", help="Source node ID")
    edge_add.add_argument("target", help="Target node ID")
    edge_add.add_argument("type", help="Relationship type")

    edge_rm = edge_sub.add_parser(
        "rm", help="Remove edges by source/target/type"
    )
    edge_rm.add_argument("source", help="Source node ID")
    edge_rm.add_argument("target", help="Target node ID")
    edge_rm.add_argument("type", help="Relationship type")

    # query commands
    query_parser = subparsers.add_parser("query", help="Query operations")
    query_sub = query_parser.add_subparsers(dest="query_cmd")
    query_sub.add_parser("nodes", help="List nodes")
    query_sub.add_parser("edges", help="List edges")

    # interactive shell
    subparsers.add_parser("shell", help="Interactive conversational shell")

    args = parser.parse_args()

    # INIT
    if args.cmd == "init":
        graph = Graph()
        save_graph(graph, args.file)
        print(f"Initialized empty graph at {args.file}")
        return

    # NODE
    if args.cmd == "node":
        graph = load_graph(args.file)
        if args.node_cmd == "add":
            node_id = args.id or str(uuid4())
            attrs = {}
            for item in args.attr or []:
                if "=" in item:
                    key, val = item.split("=", 1)
                    attrs[key] = val
            node = Node(node_id, args.type, attrs)
            graph.add_node(node)
            save_graph(graph, args.file)
            print(f"Added node {node_id} ({args.type})")
        elif args.node_cmd == "rm":
            graph.remove_node(args.id)
            save_graph(graph, args.file)
            print(f"Removed node {args.id}")
        else:
            node_parser.print_help()
        return

    # EDGE
    if args.cmd == "edge":
        graph = load_graph(args.file)
        if args.edge_cmd == "add":
            edge = Edge(args.source, args.target, args.type)
            graph.add_edge(edge)
            save_graph(graph, args.file)
            print(f"Added edge {args.source} -[{args.type}]-> {args.target}")
        elif args.edge_cmd == "rm":
            original = list(graph.edges)
            graph.edges = [
                e for e in graph.edges
                if not (
                    e.source == args.source and
                    e.target == args.target and
                    e.type == args.type
                )
            ]
            save_graph(graph, args.file)
            removed = len(original) - len(graph.edges)
            print(f"Removed {removed} edge(s)")
        else:
            edge_parser.print_help()
        return

    # QUERY
    if args.cmd == "query":
        graph = load_graph(args.file)
        if args.query_cmd == "nodes":
            for node in graph.nodes.values():
                print(json.dumps({
                    "id": node.id,
                    "type": node.type,
                    "attributes": node.attributes
                }))
        elif args.query_cmd == "edges":
            for e in graph.edges:
                print(json.dumps({
                    "source": e.source,
                    "target": e.target,
                    "type": e.type
                }))
        else:
            query_parser.print_help()
        return

    # SHELL
    if args.cmd == "shell":
        graph = load_graph(args.file)
        start_shell(graph)
        return

    parser.print_help()


if __name__ == "__main__":
    main()