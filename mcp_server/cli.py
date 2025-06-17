"""CLI entry point for MCP Server Memory Graph."""
import argparse


def main():
    parser = argparse.ArgumentParser(
        description="MCP Server Memory Graph CLI"
    )
    # TODO: add subcommands
    args = parser.parse_args()


if __name__ == "__main__":
    main()