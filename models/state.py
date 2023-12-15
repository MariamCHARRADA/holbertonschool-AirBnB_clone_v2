#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"

    if getenv("HBNB_TYPE_STORAGE") == "db":
        cities = relationship("City", cascade="delete", backref="state")
        name = Column(String(128), nullable=False)
    else:
        name = ""

        @property
        def cities(self):
            """cities getter: returns the list of City instances with state_id"""
            from models import storage
            from models.city import City

            city_list = []
            for city in list(storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
