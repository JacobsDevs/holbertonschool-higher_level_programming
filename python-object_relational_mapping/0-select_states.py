#!/usr/bin/python3
"""Prints all rows in a database"""
import sys
import MySQLdb



def print_all_rows():
    """This is the function that does it"""
    db = MySQLdb.connect(host='localhost:3306', user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])

    cur = db.cursor()
    results = cur.execute("SELECT * FROM states ORDER BY id")
    rows = results.fetchall()
    for r in rows:
        print(r)


if __name__ == "__main__":
    print_all_rows()
