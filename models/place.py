#!/usr/bin/python3
""" Place Module for HBNB project """
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from os import getenv


"""many to many relationship"""
association_table = Table(
    "place_amenity",
    Base.metadata,
    Column(
        "place_id",
        String(60),
        ForeignKey("places.id"),
        primary_key=True,
        nullable=False,
    ),
    Column(
        "amenity_id",
        String(60),
        ForeignKey("amenities.id"),
        primary_key=True,
        nullable=False,
    ),
)


class Place(BaseModel, Base):
    """Represents a Place for a MySQL database.
        Many-to-Many relationship with the Amenity class.
    """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship(
        "Amenity",
        secondary="place_amenity",
        viewonly=False,
        back_populates="place_amenities",
    )

    amenity_ids = []
    if getenv("HBNB_TYPE_STORAGE", None) != "db":

        @property
        def reviews(self):
            """Getter attribute for reviews in FileStorage"""
            from models import storage

            reviews_list = []
            for review in storage.all(Review).values():
                if review.place_id == self.id:
                    reviews_list.append(review)
            return reviews_list

        @property
        def amenities(self):
            """Getter attribute for amenities in FileStorage"""
            from models import storage

            return [storage.all(Amenity)[amenity_id] for amenity_id in self.amenity_ids]

        @amenities.setter
        def amenities(self, amenity):
            """Setter attribute for amenities in FileStorage"""
            if isinstance(amenity, Amenity):
                self.amenity_ids.append(amenity.id)
