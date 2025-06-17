"""Smoke tests for the CLI commands."""

import subprocess
import sys
import json


def test_help_command():
    result = subprocess.run(
        [sys.executable, "-m", "mcp_server.cli", "--help"],
        capture_output=True,
        text=True,
    )
    assert "usage" in result.stdout.lower()

def test_init_creates_file(tmp_path):
    file_path = tmp_path / "graph.json"
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "mcp_server.cli",
            "--file",
            str(file_path),
            "init",
        ],
        capture_output=True,
        text=True,
    )
    assert result.returncode == 0
    assert file_path.exists()
    import json

    data = json.loads(file_path.read_text(encoding="utf-8"))
    assert data == {"nodes": [], "edges": []}

def test_node_add_and_query(tmp_path):
    file_path = tmp_path / "graph.json"
    # initialize
    subprocess.run(
        [sys.executable, "-m", "mcp_server.cli", "--file", str(file_path), "init"],
        check=True,
        capture_output=True,
    )
    # add a node
    subprocess.run(
        [
            sys.executable,
            "-m",
            "mcp_server.cli",
            "--file",
            str(file_path),
            "node",
            "add",
            "Account",
            "--id",
            "1",
            "-a",
            "name=Test",
        ],
        check=True,
        capture_output=True,
    )
    # query nodes
    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "mcp_server.cli",
            "--file",
            str(file_path),
            "query",
            "nodes",
        ],
        capture_output=True,
        text=True,
    )
    lines = [l for l in result.stdout.splitlines() if l.strip()]
    assert len(lines) == 1
    node = json.loads(lines[0])
    assert node["id"] == "1"
    assert node["type"] == "Account"
    assert node["attributes"]["name"] == "Test"