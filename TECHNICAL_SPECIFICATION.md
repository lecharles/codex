# Technical Specification: MCP Server Memory Graph

## 1. Overview

This document describes the technical design and implementation plan for the MCP Server Memory Graph. It covers the overall architecture, data structures, command-line interface, persistence layer, and testing strategy.

## 2. Architecture

The MCP Server is a standalone CLI application comprising:

- **Core Graph Engine**: Manages nodes and edges in memory using Python data structures.
- **Persistence Layer**: Serializes and deserializes the graph to/from JSON files on disk.
- **CLI Interface**: Parses user commands (CRUD operations, queries, interactive shell).
- **Interactive Shell**: Provides conversational prompts and context-aware suggestions.

```
+------------+     +--------------+     +------------+
|  CLI Front | <-> | Core Engine | <-> | JSON Store |
+------------+     +--------------+     +------------+
```

## 3. Data Structures

### 3.1 Node Schema
```json
{
  "id": "<uuid>",
  "type": "Account",
  "attributes": {
    "name": "Acme Corporation",
    "industry": "Manufacturing"
  }
}
```

### 3.2 Edge Schema
```json
{
  "source": "<node-id>",
  "target": "<node-id>",
  "type": "parent_of"
}
```

### 3.3 Graph Container
```json
{
  "nodes": [ /* Node records */ ],
  "edges": [ /* Edge records */ ]
}
```

## 4. Storage & Persistence

- Use the built-in `json` module to read/write the graph container structure.
- Default file path: `memory_graph.json` in the working directory.
- Support custom file paths via CLI flags.

## 5. Command-Line Interface

All CLI commands follow the structure:
```
mcp graph <command> [options]
```

### 5.1 Commands

| Command                   | Description                                      |
| ------------------------- | ------------------------------------------------ |
| `init [--file <path>]`    | Create or overwrite an empty graph JSON file.    |
| `node add <type> [attrs]` | Add a node of given type with optional key/values.|
| `node rm <node-id>`       | Remove a node (and its incident edges).          |
| `edge add <src> <tgt> <type>` | Create a typed relationship.                |
| `edge rm <edge-id>`       | Remove an existing relationship edge.             |
| `query nodes [filters]`   | List nodes matching filter criteria.             |
| `query edges [filters]`   | List edges matching filter criteria.             |
| `shell`                   | Enter interactive conversational mode.            |

## 6. Modules & File Layout

```
mcp_server/
├── cli.py            # Entry point and argument parser
├── engine.py         # Core graph classes (Graph, Node, Edge)
├── storage.py        # JSON persistence logic
├── shell.py          # Interactive conversational shell
├── __main__.py       # Console script runner
└── tests/
    ├── test_engine.py
    ├── test_storage.py
    └── test_cli.py
```

## 7. Dependencies

- Python 3.8+
- `click` or `argparse` for CLI parsing
- `pytest` for testing

## 8. Testing Strategy

- Unit tests for core graph operations (add/remove nodes/edges).
- Integration tests for persistence (read/write JSON).
- End-to-end tests of CLI commands using subprocess fixtures.

## 9. Security & Reliability

- Validate JSON input and CLI parameters (sanity checks).
- Gracefully handle I/O errors and malformed graph files.

## 10. Future Enhancements

- Plugin system for custom graph exporters.
- Support alternative storage backends (e.g., SQLite, Neo4j).
- Enhance shell with autocompletion and history.