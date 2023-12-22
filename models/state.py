#!/usr/bin/python3
""" State Module for HBNB project """
import models
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
from os import getenv


class State(BaseModel, Base):
    """State class for representing geographical states.

    Attributes:
        __tablename__ (str): The name of the table in the database.
        name (Column): A column representing the name of the state.
        cities (relationship): A one-to-many relationship with the City model.
    """

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":

        @property
        def cities(self):
            """get list of all related city obj"""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
