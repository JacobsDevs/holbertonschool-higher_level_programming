#!/usr/bin/python3
"""Filter states in a database"""
import sys
import MySQLdb


def print_all_rows():
    """This is the function that does it"""
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for r in rows:
        print(r)


if __name__ == "__main__":
    print_all_rows()
