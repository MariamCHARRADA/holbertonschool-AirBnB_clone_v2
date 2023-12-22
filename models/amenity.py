#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey, Table
from sqlalchemy.orm import relationship


class Amenity(BaseModel, Base):
    """Amenity class

    Attributes:
        name (str): The name of the amenity.

    Relationships:
        place_amenities (relationship):
            Many-to-Many relationship with the Place class.
    """

    __tablename__ = "amenities"
    place_amenities = relationship("Place", secondary="place_amenity", viewonly=False)
