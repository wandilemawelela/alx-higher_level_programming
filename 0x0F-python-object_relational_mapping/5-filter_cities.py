#!/usr/bin/python3

"""
Lists all cities of a given state from the database hbtn_0e_4_usa.
Usage: ./5-filter_cities.py <mysql username> \
                            <mysql password> \
                            <database name> \
                            <state name>
"""

import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py <username> <password> \
                <database> <state_name>")
        sys.exit(1)

    # Extract MySQL credentials and state name from command-line arguments
    username, password, database, state_name = (
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
            )

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            user=username,
            passwd=password,
            db=database,
            port=3306
            )
    cursor = db.cursor()

    # Use parameterized query to avoid SQL injection
    query = ("SELECT `cities`.`id`, `cities`.`name` "
             "FROM `cities` "
             "INNER JOIN `states` "
             "ON `cities`.`state_id` = `states`.`id` "
             "WHERE `states`.`name` = %s "
             "ORDER BY `cities`.`id`")

    # Execute the SQL query with the parameter
    cursor.execute(query, (state_name,))

    # Fetch all rows from the result set
    cities = cursor.fetchall()

    # Display the results
    for city in cities:
        print(city)

    # Close the cursor and connection
    cursor.close()
    db.close()
