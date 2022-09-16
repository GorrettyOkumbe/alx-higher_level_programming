#!/usr/bin/python3
"""4-cities_by_states module
list all cities in the cities table
"""
from sys import argv
import MySQLdb

if __name__ == "__main__":
    conn = MySQLdb.connect(host="localhost", port=3306,
                           user=argv[1], passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
            FROM cities LEFT JOIN states\
            ON states.id = cities.state_id\
            WHERE states.name=%s\
            ORDER BY cities.id ASC", (argv[4], ))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    conn.close()
