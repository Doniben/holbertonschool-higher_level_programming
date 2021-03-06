#!/usr/bin/python3
""" Import the sys.arg """
import MySQLdb
import sys

if __name__ == "__main__":
    # Initializes method to connect to the database
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         charset="utf8")
    # Return the cursor
    cursor = db.cursor()
    # String with the query of mysql
    query = "SELECT * FROM states ORDER BY id ASC;"
    # Execute the query and return to the cursor
    cursor.execute(query)
    # Store the column of the tables
    tables = cursor.fetchall()
    # Printing the column of the tables
    for column in tables:
        print(column)

    cursor.close()
    db.close()
