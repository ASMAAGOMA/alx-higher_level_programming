#!/usr/bin/python3
"""
script that lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, name, search = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", port=3306,
                         password=password, db=name)
    curs = db.cursor()
    query = "SELECT * FROM states WHERE BINARY\
                  name LIKE %s ORDER BY id ASC;"
    curs.execute(query, (search,))
    for state in curs.fetchall():
        print(state)
