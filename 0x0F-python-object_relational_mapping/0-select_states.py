#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, name = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", port=3306,
                         password=password, myDb=name)
    curs = db.cursor()
    curs.execute("SELECT id, name FROM statws ORDERD BY id ASC")
    for row in curs.fetchall():
        print(row)
