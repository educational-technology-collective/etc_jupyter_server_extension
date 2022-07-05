import json
from ._version import _fetchVersion
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import ExtensionHandlerMixin
import tornado

class RouteHandler(ExtensionHandlerMixin, JupyterHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self, resource):

        self.add_header('Content-Type', 'application/json')
        
        if resource == 'version':
            self.finish(json.dumps(_fetchVersion()))
        elif resource == 'config':
            self.finish(json.dumps(self.config))

