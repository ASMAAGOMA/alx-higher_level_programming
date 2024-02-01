#!/usr/bin/python3

"""
City Model: Defines the City model representing a city entity in the database.
"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from model_state import State, Base

Base = declarative_base()

class City(Base):
    """
    Represents a city entity in the database.

    Attributes:
        id (int): The primary key of the city.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the state the city belongs to.
        state (State): The relationship to the State model representing the state the city belongs to.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
    state = relationship(State, back_populates="cities")

State.cities = relationship(City, back_populates="state")
