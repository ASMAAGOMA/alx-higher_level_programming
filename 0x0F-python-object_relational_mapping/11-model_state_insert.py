#!/usr/bin/python3

"""
Define a class that maps to the 'states' table in the database.
"""

import sys
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from model_state import Baze, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    session = sessionmaker(bind=engine)
    session = session()

    new = State(name="Louisiana")
    session.add(new)
    session.commit()
    print(new.id)