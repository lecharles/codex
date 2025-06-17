# Plugin Gallery

This page lists the built-in plugins that extend the MCP Server core functionality. You can also author your own plugins by implementing `PluginBase` and placing the module under `mcp_server/plugins/`.

## Built-in Plugins

| Name             | Description                                              |
| ---------------- | -------------------------------------------------------- |
| `example_connector` | A starter stub connecting to an external graph system. |
| `rest_api`          | Exposes the graph over HTTP via Flask (requires `flask`).|

## Creating Your Own Plugin

1. Create a new Python file in `mcp_server/plugins/`, e.g. `my_plugin.py`.
2. Subclass `PluginBase` and implement `name` (property) and `initialize(graph)`.
3. Automatically, the CLI and shell will discover and invoke your plugin on each command.

```python
from mcp_server.plugins.base import PluginBase

class Plugin(PluginBase):
    @property
    def name(self):
        return "my_plugin"

    def initialize(self, graph):
        # e.g. sync/transform graph data
        pass
```