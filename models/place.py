#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
from models.review import Review
from models.amenity import Amenity
import models


class Place(BaseModel, Base):
    """A place to stay"""

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)

    place_amenity = Table(
        "place_amenity",
        Base.metadata,
        Column("place_id", String(60), ForeignKey("places.id"), nullable=False),
        Column("amenity_id", String(60), ForeignKey("amenities.id"), nullable=False),
    )
    if getenv("HBNB_TYPE_STORAGE") == "db":
        reviews = relationship("Review", backref="place", cascade="delete")
        amenities = relationship("Amenity", secondary="place_amenity", viewonly=False)
    else:

        @property
        def reviews(self):
            """Return the list of Review instances with place_id"""
            list_of_reviews = []
            for key, value in models.storage.all(Review).items():
                if value.place_id == self.id:
                    list_of_reviews.append(value)
            return list_of_reviews

        @property
        def amenities(self):
            """Return the list of Amenity instances based on the list of
            amenity_ids"""
            list_of_amenities = []
            for key, value in models.storage.all(Amenity).items():
                if value.id in self.amenity_ids:
                    list_of_amenities.append(value)
            return list_of_amenities
