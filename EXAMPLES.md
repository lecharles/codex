# Usage Examples for MCP Server

Below are typical workflows demonstrating the MCP Server memory graph CLI.

## 1. Initialize a New Graph

```bash
mcp-server --file demo.json init
```

## 2. Add Nodes

```bash
mcp-server --file demo.json node add Account --id 1 -a name=Acme
mcp-server --file demo.json node add Contact --id 2 -a name="John Doe"
```

## 3. Add Relationships

```bash
mcp-server --file demo.json edge add 1 2 parent_of
```

## 4. Query the Graph

```bash
mcp-server --file demo.json query nodes
mcp-server --file demo.json query edges
```

## 5. Interactive Shell Mode

```bash
mcp-server --file demo.json shell
```