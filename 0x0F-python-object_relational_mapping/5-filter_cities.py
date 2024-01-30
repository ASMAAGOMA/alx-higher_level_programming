#!/usr/bin/python3
"""
Script that lists all cities from the database hbtn_0e_4_usa,
along with their corresponding state names.
"""
import MySQLdb
import sys

if __name__ == "__main__":
    username, password, name, search = sys.argv[1:]
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=username, passwd=password, db=name)
    curs = db.cursor()
    count = curs.execute(("SELECT cities.id, cities.name, states.name "
                          "FROM cities "
                          "INNER JOIN states ON cities.state_id = states.id "
                          "WHERE states.name = %s "
                          "ORDER BY cities.id ASC;"), (search,))
    for state in curs.fetchall():
        count -= 1
        if (count == 0):
            print(state[1], end='')
        else:
            print(state[1], end=', ')
    print()
