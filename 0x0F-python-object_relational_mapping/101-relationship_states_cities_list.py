#!/usr/bin/python3

"""
A script that lists all states in the database.
"""

from relationship_city import Base, City
from relationship_state import State


if name == "main":
    from sqlalchemy.orm import sessionmaker
    from sqlalchemy import create_engine
    import sys

    host, password, name = sys.argv[1:]
    uri = f"mysql+mysqldb://{host}:{password}@localhost/{name}"
    engine = create_engine(uri, pool_pre_ping=True)

    session = sessionmaker(bind=engine)()
    query = (
        session.query(State).join(City)
        .order_by(State.id, City.id)
    )

    for state in query:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")