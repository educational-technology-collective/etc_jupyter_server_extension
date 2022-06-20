import json
# from jupyter_server.base.handlers import APIHandler
# from jupyter_server.utils import url_path_join
from jupyter_server.base.handlers import JupyterHandler
from jupyter_server.extension.handler import ExtensionHandlerMixin
import tornado

class RouteHandler(ExtensionHandlerMixin, JupyterHandler):
    # The following decorator should be present on all verb methods (head, get, post,
    # patch, put, delete, options) to ensure only authorized user can request the
    # Jupyter server
    @tornado.web.authenticated
    def get(self):
        self.finish(json.dumps(self.config))

        # self.finish(json.dumps({
        #     "data": "This is /etc-jupyter-server-extension/test endpoint!"
        # }))

