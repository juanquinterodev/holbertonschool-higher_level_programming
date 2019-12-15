#!/usr/bin/python3
""" Write one that is safe from MySQL injections
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
    l.execute("SELECT * FROM states WHERE name=%s \
                ORDER BY states.id ASC", (state,))
    rows = l.fetchall()
    for row in rows:
        print(row)
