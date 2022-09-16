#!/usr/bin/python3
"""filter_states module"""

import sys
import MySQLdb

if __name__ == "__main__":
    args = sys.argv
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=args[1], passwd=args[2], db=args[3])
    cur = conn.cursor()
    cur.execute(
        "SELECT * FROM `states` WHERE name=%s \
                ORDER BY states.id ASC", (args[4],))
    rows = cur.fetchall()

    for row in rows:
        if row[1] == args[4]:
            print(row)
    cur.close()
    conn.close()
