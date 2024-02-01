#!/usr/bin/python3

"""
Script to add a new state to the 'states' table in
the database and print its ID.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import City, Base, State


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State).join(City).order_by(City.id)
    for state in query:
        for city in state.cities:
            print("{}: {} {}".format(state.name, city.id, city.name))
