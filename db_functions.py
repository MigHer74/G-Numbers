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
