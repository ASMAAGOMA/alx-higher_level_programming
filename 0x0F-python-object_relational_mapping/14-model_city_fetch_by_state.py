#!/usr/bin/python3

"""
Script to list all states in the database along with their cities.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_city import Base, State, City


if __name__ == "__main__":
    engine = create_engine(f'mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost/{sys.argv[3]}'
                           , pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    query = session.query(State).join(City).order_by(City.id)

    for state in query:
        print(f"{state.name}:")
        for city in state.cities:
            print(f"({city.id}) {city.name}")
