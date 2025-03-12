#!/usr/bin/python3
"""Lists cities in a database"""
import sys
import MySQLdb


def print_all_rows():
    """This is the function that does it"""
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT c.id, c.name, s.name
                FROM cities AS c
                LEFT JOIN states AS s
                ON s.id = c.state_id
                ORDER BY c.id""")
    rows = cur.fetchall()
    for r in rows:
        print(r)


if __name__ == "__main__":
    print_all_rows()
