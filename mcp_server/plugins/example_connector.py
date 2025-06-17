"""Example connector plugin for external graph databases."""
from mcp_server.plugins.base import PluginBase


class Plugin(PluginBase):
    """Sample connector plugin stub."""

    @property
    def name(self):
        return "example_connector"

    def initialize(self, graph):
        """Initialize connector (stub: no-op)."""
        # TODO: connect to external graph DB and sync data
        pass