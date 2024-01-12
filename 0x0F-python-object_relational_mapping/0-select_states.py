#!/usr/bin/python3

import MySQLdb
import sys

def list_states(username, password, database):
    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        user=username,
        passwd=password,
        db=database,
        port=3306
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Execute the SQL query to fetch all states
    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    # Fetch all rows from the result set
    states = cursor.fetchall()

    # Display the results
    for state in states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python script.py <username> <password> <database>")
        sys.exit(1)

    # Extract username, password, and database name from command-line arguments
    username, password, database = sys.argv[1], sys.argv[2], sys.argv[3]

    # Call the function to list states
    list_states(username, password, database)

