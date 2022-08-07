#!/usr/bin/python3
"""lists all states with a name starting with N"""

if (__name__ == "__main__"):
    from sys import argv
    import MySQLdb

    db = MySQLdb.connect(
            host="localhost", port=3306,
            user=argv[1], passwd=argv[2],
            db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
