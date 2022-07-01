import json
from pathlib import Path
from .application import ETCJupyterServerExtensionApp
from ._version import __version__

HERE = Path(__file__).parent.resolve()


with (HERE / "labextension" / "package.json").open() as fid:
    data = json.load(fid)


def _jupyter_labextension_paths():
    return [{
        "src": "labextension",
        "dest": data["name"]
    }]



def _jupyter_server_extension_points():
    """
    Returns a list of dictionaries with metadata describing
    where to find the `_load_jupyter_server_extension` function.
    """
    return [
        {
            "module": "etc_jupyter_server_extension",
            "app": ETCJupyterServerExtensionApp
        }
    ]

load_jupyter_server_extension = ETCJupyterServerExtensionApp.load_classic_server_extension
