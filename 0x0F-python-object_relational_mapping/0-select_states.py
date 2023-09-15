#!/usr/bin/python3
"""Task 0 Get all states from  states from the database hbtn_0e_0_usa"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    mysql_username, mysql_password, mysql_db_name = argv[1], argv[2], argv[3]

    db = MySQLdb.connect(
        host='127.0.0.1',
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=mysql_db_name
    )
    # Close the cursor and database connection
    cursor.close()
    db.close()
    cursor = db.cursor()
    all_states = cursor.execute("SELECT * FROM states ORDER BY id")

    for i in cursor.fetchall():
        print(i)
