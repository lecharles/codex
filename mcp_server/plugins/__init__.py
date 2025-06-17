"""Plugin system for MCP Server Memory Graph."""
import importlib
import pkgutil


def load_plugins():
    """Discover and load all plugins in the mcp_server.plugins package."""
    plugins = []
    for _finder, name, ispkg in pkgutil.iter_modules(__path__):
        module = importlib.import_module(f"{__name__}.{name}")
        # Look for Plugin class in module
        plugin_cls = getattr(module, "Plugin", None)
        if plugin_cls:
            plugins.append(plugin_cls())
    return plugins

__all__ = ["load_plugins"]