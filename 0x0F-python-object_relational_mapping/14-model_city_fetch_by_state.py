#!/usr/bin/python3

"""
Script to list all states in the database along with their cities.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, State, City

if __name__ == "__main__":
    # The script takes three arguments: host, password, and database name.
    host, password, name = sys.argv[1:]
    # Construct the URI for connecting to the MySQL database.
    uri = f"mysql+mysqldb://{host}:{password}@localhost/{name}"
    engine = create_engine(uri, pool_pre_ping=True)

    # Create a session to interact with the database.
    session = sessionmaker(bind=engine)()
    
    # Query all states from the database, joining with cities and ordering by city ID.
    query = session.query(State).join(City).order_by(City.id)

    # Iterate over the query results and print each state along with its cities.
    for state in query:
        for city in state.cities:
            print(f"{state.name}: ({city.id}) {city.name}")
