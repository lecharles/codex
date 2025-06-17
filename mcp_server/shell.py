"""Interactive conversational shell for MCP Server."""


def start_shell(graph, file_path):
    """Start an interactive conversational REPL for graph operations."""
    import shlex
    import sys

    print("Welcome to the MCP Server interactive shell.")
    print("Type 'help' for a list of commands, or 'exit' to quit.")
    while True:
        try:
            line = input("mcp> ").strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not line:
            continue
        if line in ("exit", "quit"):
            print("Exiting shell.")
            break
        if line in ("help", "?"):
            print(
                "Commands: init | node add <type> [--id ID] [-a key=val] |"
                " node rm <id> | edge add <src> <tgt> <type> |"
                " edge rm <src> <tgt> <type> | query nodes | query edges | exit"
            )
            continue
        parts = shlex.split(line)
        sys.argv = [sys.argv[0], "--file", file_path] + parts
        try:
            from mcp_server.cli import main as cli_main

            cli_main()
        except SystemExit:
            # argparse may call sys.exit()
            pass
        except Exception as e:
            print(f"Error: {e}")