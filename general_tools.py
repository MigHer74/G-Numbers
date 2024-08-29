from pathlib import Path
import db_functions as dba


def verify_data():
    dbFolder = "db"
    dbFile = "G-Numbers.db"

    if not Path(dbFolder).is_dir():
        Path.mkdir("db")

    if not Path(dbFile).is_file():
        dba.dbaCreateDatabase()


def load_weeks(loadtype, loadweek):
    data = dba.dbaRetrieveOrderValues(loadtype, loadweek)

    temp_game1 = data[0][3:]
    temp_game2 = data[1][3:]
    temp_game3 = data[2][3:]

    temp_game1 = ", ".join(map(str, temp_game1))
    temp_game2 = ", ".join(map(str, temp_game2))
    temp_game3 = ", ".join(map(str, temp_game3))

    return temp_game1, temp_game2, temp_game3
