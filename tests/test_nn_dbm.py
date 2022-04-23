# """
# @Author: Ramadhan Januar
# @Email: ramadhan@99.co
# @Date: 2022-04-21
# """
# tests/test_nn_dbm.py

from typer.testing import CliRunner
from nn_dbm import __app_name__, __version__, cli

runner = CliRunner()

def test_version():
    result = runner.invoke(cli.app, ["--version"])
    assert result.exit_code == 0
    assert f"{__app_name__} v{__version__}\n" in result.stdout