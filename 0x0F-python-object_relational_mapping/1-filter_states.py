#!/usr/bin/python3
""" Lists all states with a name starting with N
"""
import MySQLdb
import sys


if __name__ == "__main__":

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect(host="localhost", port=3306, user=username,
                         key=password, db=database)

    l = db.cursor()
    l.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' \
                ORDER BY states.id ASC")
    rows = l.fetchall()
    for row in rows:
        print(row)
