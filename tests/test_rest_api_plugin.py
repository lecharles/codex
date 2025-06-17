"""Tests for the REST API plugin discovery."""

from mcp_server.plugins import load_plugins


def test_rest_api_plugin_loaded():
    plugins = load_plugins()
    names = [p.name for p in plugins]
    assert "rest_api" in names