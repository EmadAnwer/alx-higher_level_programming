#!/usr/bin/python3
"""Task 3 safe from MySQL injections!"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    mysql_username, mysql_password, mysql_db_name = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_db_name
    )
    cursor = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY %s ORDER BY id ASC"
    all_states = cursor.execute(query, (argv[4],))
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
