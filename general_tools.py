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
    temp_game1 = []
    temp_game2 = []
    temp_game3 = []

    data = dba.dbaRetrieveOrderValues(loadtype, loadweek)

    temp_g1 = data[0][3:]
    temp_g2 = data[1][3:]
    temp_g3 = data[2][3:]

    for num in temp_g1:
        if len(str(num)) == 1:
            if num != ",":
                temp_game1.append(" " + str(num))
            else:
                temp_game1.append(str(num))
        else:
            temp_game1.append(str(num))

    for num in temp_g2:
        if len(str(num)) == 1:
            if num != ",":
                temp_game2.append(" " + str(num))
            else:
                temp_game2.append(str(num))
        else:
            temp_game2.append(str(num))

    for num in temp_g3:
        if len(str(num)) == 1:
            if num != ",":
                temp_game3.append(" " + str(num))
            else:
                temp_game3.append(str(num))
        else:
            temp_game3.append(str(num))

    tmp_game1 = ", ".join(temp_game1)
    tmp_game2 = ", ".join(temp_game2)
    tmp_game3 = ", ".join(temp_game3)

    return tmp_game1, tmp_game2, tmp_game3
