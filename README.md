# codex
Codex repo - design and runtime

## Installation

Install from the local directory or via PyPI when published:

```bash
pip install .
# or, when released:
pip install mcp-server
```

## Examples

See [EXAMPLES.md](EXAMPLES.md) for usage examples and workflows.

## Plugins

The MCP Server supports a plugin system under the `mcp_server/plugins/` directory. Plugins are automatically discovered and initialized for all commands and in the interactive shell.

Currently provided plugins (see [PLUGIN_GALLERY.md](PLUGIN_GALLERY.md)):

- **example_connector**: Sample stub connector plugin.
- **rest_api**: Exposes the graph over HTTP using Flask (requires `flask`).

To enable the REST API plugin, install its dependency:
```bash
pip install flask
```

## Releasing

See [RELEASE.md](RELEASE.md) for details on publishing new versions to PyPI.
