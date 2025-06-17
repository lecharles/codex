"""Unit tests for the plugin loader."""

from mcp_server.plugins import load_plugins


def test_load_plugins_empty(tmp_path, monkeypatch):
    # Temporarily override plugins path to an empty directory
    monkeypatch.setattr(
        load_plugins.__module__ + ".__path__", [],
        raising=False
    )
    plugins = load_plugins()
    assert isinstance(plugins, list)
    assert plugins == []