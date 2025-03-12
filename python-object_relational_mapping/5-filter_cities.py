#!/usr/bin/python3
"""Lists cities belonging to a state in a database"""
import sys
import MySQLdb


def print_all_rows():
    if len(sys.argv) > 4 and ';' in sys.argv[4]:
        return
    """This is the function that does it"""
    db = MySQLdb.connect(host='localhost',
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    cur = db.cursor()
    cur.execute("""SELECT c.name
                FROM cities AS c
                LEFT JOIN states AS s
                ON s.id = c.state_id
                WHERE s.name = '{}'
                ORDER BY c.id""".format(sys.argv[4]))
    rows = cur.fetchall()
    cities = []
    for r in rows:
        cities.append(r[0])
    print(", ".join(cities))


if __name__ == "__main__":
    print_all_rows()
