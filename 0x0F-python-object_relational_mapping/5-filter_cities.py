#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""

if (__name__ == "__main__"):
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
    JOIN states ON cities.state_id = states.id WHERE states.name LIKE %s \
    ORDER BY cities.id", (argv[4],))
    rows = cursor.fetchall()
    print(", ".join(row[0] for row in rows))
    cursor.close()
    db.close()
