import sqlite3


def dbaConnection():
    dbaConnect = sqlite3.connect("db/G-Numbers.db")
    return dbaConnect


def dbaShowLatest():
    dbcon = dbaConnection()
    dbcur = dbcon.cursor()
    dbdatas = dbcur.execute("SELECT * FROM 'games' WHERE gType = 'S'\
                            AND gWeek = 'W1'").fetchone()
    dbdatal = dbcur.execute("SELECT * FROM 'games' WHERE gType = 'L'\
                            AND gWeek = 'W1'").fetchall()
    return dbdatas, dbdatal


def dbaUpdateGame(dbtype):
    dblist = ["W6", "W5", "W4", "W3", "W2", "W1"]

    if dbtype == "short":
        dbtype = "S"
    else:
        dbtype = "L"

    dbcon = dbaConnection()
    dbcur = dbcon.cursor()

    row1 = "DELETE FROM games WHERE gWeek ='W6'"
    row2 = f"AND gType = '{dbtype}';"
    command = row1 + row2
    dbcur.execute(command)

    for dbindex in range(1, 6):
        row1 = f"UPDATE games SET gWeek = '{dblist[dbindex-1]}'"
        row2 = f"WHERE gWeek = '{dblist[dbindex]}' AND gType = '{dbtype}';"
        command = row1 + row2
        dbcur.execute(command)

    dbcon.commit()
    dbcon.close()
