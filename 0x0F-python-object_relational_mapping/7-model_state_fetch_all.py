#!/usr/bin/python3

"""
Lists all State objects from the database hbtn_0e_6_usa.
Usage: ./7-model_state_fetch_all.py <mysql username> /
                                    <mysql password> /
                                    <database name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

def list_states(username, password, database_name):
    # Define the engine to connect to the MySQL server
     engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}"
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all State objects and order by id
    states = session.query(State).order_by(State.id).all()

    # Display the results
    for state in states:
        print(f"{state.id}: {state.name}")

if __name__ == "__main__":
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: python list_states.py <username> <password> <database_name>")
        sys.exit(1)

    # Extract arguments
    username, password, database_name = sys.argv[1:]

    # Call the function to list states
    list_states(username, password, database_name)

