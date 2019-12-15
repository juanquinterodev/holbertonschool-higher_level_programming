#!/usr/bin/python3
"""Takes in an argument and displays all values in the states table of
    hbtn_0e_0_usa where name matches the argument
"""
import MySQLdb
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         passwd=password, db=database)

    l = db.cursor()
    l.execute("SELECT * FROM states WHERE name LIKE BINARY '{:s}' \
                ORDER BY states.id ASC".format(state))
    rows = l.fetchall()
    for row in rows:
        print(row)
