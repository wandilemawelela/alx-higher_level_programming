#!/usr/bin/python3

"""
Displays all values in the states table of the database hbtn_0e_0_usa
whose name matches that supplied as argument.
Usage: ./2-my_filter_states.py <mysql username> \
                                <mysql password> \
                                <database name> \
                                <state name searched>
"""

import MySQLdb
import sys


def search_states(username, password, database, state_name):
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

    # Use format to create the SQL query with the user input
    query = "SELECT * FROM states WHERE name = \
    '{}' ORDER BY states.id ASC".format(state_name)

    # Execute the SQL query
    cursor.execute(query)

    # Fetch all rows from the result set
    matching_states = cursor.fetchall()

    # Display the results
    for state in matching_states:
        print(state)

    # Close the cursor and connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> \
                <database> <state_name>")
        sys.exit(1)

    # Extract username, password, database name, and state
    # name from command-line arguments
    username, password, database, state_name = (
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
            )

    # Call the function to search for states with the provided name
    search_states(username, password, database, state_name)
