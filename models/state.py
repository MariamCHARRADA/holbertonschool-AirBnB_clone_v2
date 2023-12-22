#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base


class State(BaseModel, Base):
    """State class"""

    __tablename__ = "states"
    from os import getenv
    from sqlalchemy import Column, String
    from sqlalchemy.orm import relationship

    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="state", cascade="all, delete")
    else:
        name = ""

        @property
        def cities(self):
            """returns the list of City instances
            with state_id equals to the current State.id"""
            from models import storage
            from models.city import City

            l = []
            res = storage.all(City)
            for v in res.values():
                if v.state_id == self.id:
                    l.append(v)
            return l
