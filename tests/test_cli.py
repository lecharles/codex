"""Smoke tests for the CLI commands."""

import subprocess
import sys


def test_help_command():
    result = subprocess.run(
        [sys.executable, "-m", "mcp_server.cli", "--help"],
        capture_output=True,
        text=True,
    )
    assert "usage" in result.stdout.lower()