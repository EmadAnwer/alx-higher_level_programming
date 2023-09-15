#!/usr/bin/python3
"""Task 0 Get all states from  states from the database hbtn_0e_0_usa"""
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
    SELECT cities.id, cities.name, states.name FROM cities
    INNER JOIN states
    ON cities.state_id = states.id
    ORDER BY cities.id ASC"""
    all_states = cursor.execute(query)

    for row in cursor.fetchall():
        print(row)
    # Close the cursor and database connection
    cursor.close()
    db.close()
