#!/usr/bin/python3

"""
Script to add a new state to the 'states' table in
the database and print its ID.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State, City

if __name__ == "__main__":
    host, password, name = sys.argv[1:]
    uri = f"mysql+mysqldb://{host}:{password}@localhost/{name}"
    engine = create_engine(uri, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).join(City).order_by(City.id)
    for state in query:
        for city in state.cities:
            print(f"{state.name}: ({city.id}) {city.name}")
