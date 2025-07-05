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


def center_window(window, window_width, window_height):
    display_width = window.winfo_screenwidth()
    display_height = window.winfo_screenheight()

    x = int((display_width / 2) - (window_width / 2))
    y = int((display_height / 2) - (window_height / 2))

    return window.geometry(f"{window_width}x{window_height}+{x}+{y}")
