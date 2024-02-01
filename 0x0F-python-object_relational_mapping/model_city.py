#!/usr/bin/python3

"""
State Model
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

class State(Base):
    """
    Represents a state entity in the database.

    Attributes:
        id (int): The primary key of the state.
        name (str): The name of the state.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
