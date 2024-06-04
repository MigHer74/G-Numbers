import sqlite3


def dbaConnection():
    dbaConnect = sqlite3.connect("dba/G-Numbers.db")
    return dbaConnect
