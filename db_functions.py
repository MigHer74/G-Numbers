import sqlite3


def dbaConnection():
    dbaConnect = sqlite3.connect("db/G-Numbers.db")
    return dbaConnect


def dbaCreateDatabase():
    dbcon = dbaConnection()
    dbcur = dbcon.cursor()

    sqlrow = """CREATE TABLE IF NOT EXISTS 'games' (
    gType TEXT,
    gWeek TEXT,
    gGame INTEGER,
    gNumber1 INTEGER,
    gNumber2 INTEGER,
    gNumber3 INTEGER,
    gNumber4 INTEGER,
    gNumber5 INTEGER,
    gNumber6 INTEGER
);"""

    dbcur.execute(sqlrow)
    dbcon.commit()
    dbcon.close()


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


def dbaInsertValues(dbdata):
    dbcon = dbaConnection()
    dbcur = dbcon.cursor()
    dbcur.execute("INSERT INTO games VALUES(?,?,?,?,?,?,?,?,?)", (dbdata))
    dbcon.commit()
    dbcon.close()


def dbaRetriveValues(dbtype):
    if dbtype == "short":
        dbtype = "S"
    else:
        dbtype = "L"

    sqlrow = f"SELECT * FROM games WHERE gType = '{dbtype}'"

    dbcon = dbaConnection()
    dbcur = dbcon.cursor()
    dbdata = dbcur.execute(sqlrow).fetchall()
    dbcon.close()

    return dbdata


def dbaRetriveOrderValues(dbtype):
    if dbtype == "short":
        dbtype = "S"
        sqlrow = f"SELECT * FROM games WHERE gType = '{dbtype}' ORDER BY gweek"
    else:
        dbtype = "L"
        sqlrow = f"""SELECT * FROM games WHERE gType = '{dbtype}' ORDER BY
                     gweek, ggame"""

    dbcon = dbaConnection()
    dbcur = dbcon.cursor()
    dbdata = dbcur.execute(sqlrow).fetchall()
    dbcon.close()

    return dbdata


def dbaRetrieveOneWeek(dbtype, dbweek):
    if dbtype == "short":
        dbtype = "S"
    else:
        dbtype = "L"

    sqlrow1 = f"SELECT * FROM games WHERE gType = '{dbtype}' "
    sqlrow2 = f"AND gWeek = '{dbweek}'"

    sqlrow = sqlrow1 + sqlrow2
    print(sqlrow)
    dbcon = dbaConnection()
    dbcur = dbcon.cursor()
    dbdata = dbcur.execute(sqlrow).fetchall()
    dbcon.close()

    return dbdata
