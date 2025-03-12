#!/usr/bin/python3
import sys
import MySQLdb


"""
Prints a list of the states in the database
"""
if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost:3306', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    results = cur.execute("SELECT * FROM states ORDER BY id")
    rows = results.fetchall()
    for r in rows:
        print(r)
