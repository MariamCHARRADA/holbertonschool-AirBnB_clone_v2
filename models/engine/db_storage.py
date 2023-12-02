#!/usr/bin/python3
"""
Contains the class DBStorage
"""

from models.base_model import BaseModel
from models.base_model import Base
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from os import getenv
from sqlalchemy import Column
from sqlalchemy import create_engine
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage:
    """class for handling MySQL database using SQLAlchemy"""

    __engine = None
    __session = None
    __classes = {
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review,
    }

    def __init__(self):
        """Instantiate a DBStorage object"""
        self.__engine = create_engine(
            "mysql+mysqldb://HBNB_MYSQL_USER:HBNB_MYSQL_PWD@localhost/HBNB_MYSQL_DB",
            pool_pre_ping=True,
        )
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns the list of objects of one type of class"""
        new_dict = {}
        if cls is None:
            for object_class in self.__classes.values():
                for obj in self.__session.query(object_class).all():
                    key = obj.__class__.__name__ + "." + obj.id
                    new_dict[key] = obj
        else:
            for obj in self.__session.query(cls).all():
                key = obj.__class__.__name__ + "." + obj.id
                new_dict[key] = obj
        return new_dict

    def new(self, obj):
        """Adds the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Reloads data from the database"""
        Base.metadata.create_all(
            self.__engine
        )  # uses SQLAlchemy to create all the tables defined in your models
        self.__session = scoped_session(
            sessionmaker(bind=self.__engine, expire_on_commit=False)
        )
