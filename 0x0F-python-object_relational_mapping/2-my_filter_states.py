#!/usr/bin/python3
"""Task 2 takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument."""
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
    query = """
    SELECT * FROM states
    WHERE name LIKE BINARY '{}'
    ORDER BY id ASC""".format(argv[4])
    all_states = cursor.execute(query)
    for row in cursor.fetchall():
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
