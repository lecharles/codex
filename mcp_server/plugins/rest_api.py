"""REST API plugin for MCP Server using Flask."""
import threading

from mcp_server.plugins.base import PluginBase


class Plugin(PluginBase):
    """Plugin to expose the graph via a RESTful API."""

    @property
    def name(self):
        return "rest_api"

    def initialize(self, graph):
        try:
            from flask import Flask, jsonify
        except ImportError:
            import sys
            print(
                "Flask is required for REST API plugin. Skipping plugin.",
                file=sys.stderr,
            )
            return

        app = Flask(self.name)

        @app.route("/nodes")
        def list_nodes():
            return jsonify([
                {"id": n.id, "type": n.type, "attributes": n.attributes}
                for n in graph.nodes.values()
            ])

        @app.route("/edges")
        def list_edges():
            return jsonify([
                {"source": e.source, "target": e.target, "type": e.type}
                for e in graph.edges
            ])

        def run_server():
            app.run(port=5000, debug=False)

        thread = threading.Thread(target=run_server, daemon=True)
        thread.start()
        print("REST API server started at http://localhost:5000")