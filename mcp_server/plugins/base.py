"""Plugin architecture base for MCP Server."""
from abc import ABC, abstractmethod


class PluginBase(ABC):
    """Abstract base class for MCP Server plugins."""

    @property
    @abstractmethod
    def name(self):
        """Name of the plugin."""
        pass

    @abstractmethod
    def initialize(self, graph):
        """Initialize plugin with the graph instance."""
        pass