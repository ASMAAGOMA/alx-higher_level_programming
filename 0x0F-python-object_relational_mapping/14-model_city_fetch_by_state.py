#!/usr/bin/python3

"""
Script to list all states in the database along with their cities.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, State, City

if __name__ == "__main__":
    host, password, name = sys.argv[1:]
    uri = f"mysql+mysqldb://{host}:{password}@localhost/{name}"
    engine = create_engine(uri, pool_pre_ping=True)

    session = sessionmaker(bind=engine)()
    query = session.query(State).join(City).order_by(City.id)

    for state in query:
        for city in state.cities:
            print(f"{state.name}: ({city.id}) {city.name}")
