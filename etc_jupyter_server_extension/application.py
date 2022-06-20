from .handlers import RouteHandler
from jupyter_server.extension.application import ExtensionApp
from traitlets import Bool


class ETCJupyterServerExtensionApp(ExtensionApp):

    # -------------- Required traits --------------
    name = "etc_jupyter_server_extension"
    # default_url = "/myextension"
    # load_other_extensions = True
    # file_url_prefix = "/render"

    # --- ExtensionApp traits you can configure ---
    # static_paths = [...]
    # template_paths = [...]
    # settings = {...}
    # handlers = [...]

    # ----------- add custom traits below ---------
    # ...

    test = Bool(False, config=True)

    def initialize_settings(self):
        # ...
        # Update the self.settings trait to pass extra
        # settings to the underlying Tornado Web Application.
        # self.settings.update({'<trait>':...})
        self.log.info(f"Config {self.config}")

    def initialize_handlers(self):
        # ...
        # Extend the self.handlers trait
        # self.handlers.extend(...)
        self.handlers.extend([(r"/etc-jupyter-server-extension/test", RouteHandler)])

    # def initialize_templates(self):
    #     ...
        # Change the jinja templating environment

    # async def stop_extension(self):
    #     ...
        # Perform any required shut down steps

# def setup_handlers(web_app):
#     host_pattern = ".*$"

#     base_url = web_app.settings["base_url"]
#     route_pattern = url_path_join(base_url, "etc-jupyter-server-extension", "get_example")
#     handlers = [(route_pattern, RouteHandler)]
#     web_app.add_handlers(host_pattern, handlers)
