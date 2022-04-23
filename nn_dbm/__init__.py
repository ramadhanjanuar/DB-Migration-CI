# """
# @Author: Ramadhan Januar
# @Email: ramadhan@99.co
# @Date: 2022-04-21
# """

import configparser
from pathlib import Path
import typer
import yaml
from pathlib import Path
from yaml.loader import SafeLoader

__app_name__ = "nn-dbm"
__version__ = "0.1.0"

(
    SUCCESS,
    DIR_ERROR,
    FILE_ERROR,
    JSON_ERROR,
) = range(4)

ERRORS = {
    DIR_ERROR: "config directory error",
    FILE_ERROR: "config file error",

}

DATABASES = "databases"
DATABASES_DIR = "databases"
DATA = {}

with open("config.yaml") as f:
    data = yaml.load(f, Loader=SafeLoader)
    for datum in data[DATABASES]:
        DATA[datum["DB_name"]] = datum

def init_app() -> int:
    """Initialize the application."""
    for datum in data[DATABASES]:
        create_dir(DATABASES_DIR+"/"+datum["DB_name"])

    return SUCCESS

def create_dir(pathname: str) -> None:
    p = Path(pathname)
    p.mkdir(exist_ok=True)