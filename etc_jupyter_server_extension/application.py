from .handlers import RouteHandler
from jupyter_server.extension.application import ExtensionApp
from jupyter_server.utils import url_path_join
from traitlets import Bool


class ETCJupyterServerExtensionApp(ExtensionApp):

    name = "etc_jupyter_server_extension"

    test = Bool(False, config=True)

    def initialize_settings(self):
        self.log.info(f"Config {self.config}")

    def initialize_handlers(self):
        handlers = [(r'/etc-jupyter-server-extension/(.*)', RouteHandler)]
        self.handlers.extend(handlers)
