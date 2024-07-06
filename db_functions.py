import sqlite3


def dbaConnection():
    dbaConnect = sqlite3.connect("db/G-Numbers.db")
    return dbaConnect
