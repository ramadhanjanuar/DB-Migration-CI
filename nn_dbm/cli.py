# """
# @Author: Ramadhan Januar
# @Email: ramadhan@99.co
# @Date: 2022-04-21
# """

from ensurepip import version
import typer
import subprocess
from typing import Optional
from nn_dbm import __app_name__, __version__, init_app, DATA

app = typer.Typer()

def _version_callback(value: bool) -> None:
    if value:
        typer.echo(f"{__app_name__} v{__version__}")
        raise typer.Exit()

@app.callback()
def main(
    version: Optional[bool] = typer.Option(
        None,
        "--version",
        "-v",
        help="Show the application's version and exit.",
        callback=_version_callback,
        is_eager=True,
    )
) -> None:
    return

@app.command()
def init():
    init_app()
 
@app.command()
def create_migration(dbname: str, filename: str) -> None:
    dbObjct = DATA[dbname]
    migrationsPath = "databases/{}/migrations".format(dbObjct["DB_name"])
    cp = subprocess.run(["golang-migrate/./migrate","create", "-ext", "sql", "-dir", migrationsPath, "-seq", filename])
    cp.stdout
    return

@app.command()
def migrate(dbname: str) -> None:
    dbObjct = DATA[dbname]
    migrationsPath = "databases/{}/migrations".format(dbObjct["DB_name"])
    dbURL = "{}://{}:{}@{}:{}/{}".format(
        dbObjct["DB_driver"], dbObjct["DB_user"], dbObjct["DB_password"], \
        dbObjct["DB_host"], dbObjct["DB_port"], dbObjct["DB_name"]
    )
    cp = subprocess.run(["golang-migrate/./migrate","-path", migrationsPath, "-database", dbURL, "up"])
    cp.stdout
    return

@app.command()
def force(dbname: str, version: str) -> None:
    dbObjct = DATA[dbname]
    migrationsPath = "databases/{}/migrations".format(dbObjct["DB_name"])
    dbURL = "{}://{}:{}@{}:{}/{}".format(
        dbObjct["DB_driver"], dbObjct["DB_user"], dbObjct["DB_password"], \
        dbObjct["DB_host"], dbObjct["DB_port"], dbObjct["DB_name"]
    )
    cp = subprocess.run(["golang-migrate/./migrate","-path", migrationsPath, "-database", dbURL, "force", version])
    cp.stdout
    return

@app.command()
def rollback(dbname: str) -> None:
    dbObjct = DATA[dbname]
    migrationsPath = "databases/{}/migrations/".format(dbObjct["DB_name"])
    dbURL = "{}://{}:{}@{}:{}/{}".format(
        dbObjct["DB_driver"], dbObjct["DB_user"], dbObjct["DB_password"], \
        dbObjct["DB_host"], dbObjct["DB_port"], dbObjct["DB_name"]
    )
    cp = subprocess.run(["golang-migrate/./migrate","-path", migrationsPath, "-database", dbURL, "down"])
    cp.stdout
    return