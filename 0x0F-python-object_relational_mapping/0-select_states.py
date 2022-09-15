#!/usr/bin/python3
"""0-select_states module"""
import sys
import MySQLdb
args = sys.argv
conn = MySQLdb.connect(host="localhost", port=3306,
                       user=args[1], passwd=args[2], db=args[3])
cur = conn.cursor()
cur.execute("SELECT * FROM `states` ORDER BY states.id ASC ")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
