#!/usr/bin/python3
"""New engine DBStorage"""
from os import getenv
from sqlalchemy import create_engine
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """this is the class DBStorage"""

    __engine = None
    __session = None

    def __init__(self):
        """constructor"""
        from models.base_model import Base

        user = getenv("HBNB_MYSQL_USER")
        pwd = getenv("HBNB_MYSQL_PWD")
        host = getenv("HBNB_MYSQL_HOST")
        db = getenv("HBNB_MYSQL_DB")
        if user and pwd and host and db:
            link = "mysql+mysqldb://{}:{}@{}/{}".format(user, pwd, host, db)
            self.__engine = create_engine(link, pool_pre_ping=True)
        if getenv("HBNB_ENV") == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """query all objects"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        dict = {}
        classes = [User, State, City, Amenity, Place, Review]
        if cls is None:
            for i in classes:
                res = self.__session.query(i).all()
                for v in res:
                    k = "{}.{}".format(i.__name__, v.id)
                    dict[k] = v
        else:
            res = self.__session.query(cls).all()
            for v in res:
                k = "{}.{}".format(cls.__name__, v.id)
                dict[k] = v
        return dict

    def new(self, obj):
        """add the object to the current database session"""
        self.__session.add(obj)

    def save(self):
        """commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """create all tables in the database"""
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from sqlalchemy.engine.base import Engine

        if isinstance(self.__engine, Engine):
            make_s = sessionmaker(bind=self.__engine, expire_on_commit=False)
            self.__session = scoped_session(make_s)
            Base.metadata.create_all(self.__engine)

    def close(self):
        """call remove() method on the private
        session attribute (self.__session) orclose() on the class Session"""
        self.__session.close()
