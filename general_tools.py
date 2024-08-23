from pathlib import Path
import db_functions as dba


def verify_data():
    dbFolder = "db"
    dbFile = "G-Numbers.db"

    if not Path(dbFolder).is_dir():
        Path.mkdir("db")

    if not Path(dbFile).is_file():
        dba.dbaCreateDatabase()
