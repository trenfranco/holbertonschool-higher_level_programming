#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa"""

if (__name__ == "__main__"):
    import MySQLdb
    from sys import argv

    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities \
    JOIN states ON cities.state_id = states.id ORDER BY cities.id")
    rows = cursor.fetchall()
    for i in rows:
        print(i)
    cursor.close()
    db.close()
