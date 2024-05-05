#!/usr/bin/python3
"DB storage"

from os import getenv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker

from models.amenity import Amenity
from models.base_model import Base, BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class DBStorage():
    """
    DB
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        init
        """
        mysql_user = getenv("HBNB_MYSQL_USER")
        mysql_passwd = getenv("HBNB_MYSQL_PWD")
        mysql_host = getenv("HBNB_MYSQL_HOST")
        mysql_database = getenv("HBNB_MYSQL_DB")
        self.__engine = create_engine("mysql+mysqldb://{}:{}@{}:3306/{}"
                                      .format(mysql_user, mysql_passwd,
                                              mysql_host, mysql_database), pool_pre_ping=True)
        if (getenv("HBNB_ENV") == "test"):
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        getting Target Class query or default all
        """
        filter = []
        classes = [City, Place, Review, State, User]

        if (cls == None):
            filter = self.__session.query(cls).all()
        else:
            for clss in classes:
                filter.extend(self.__session.query(clss).all())

        dic_db = {}
        for query in filter:
            dic_db[(type(query).__name__ + '.' + query.id)] = query

        return dic_db

    def new(self, obj):
        """addes a new to the current database session."""
        self.__session.add(obj)

    def save(self):
        """saves a object to the current database session."""
        self.__session.commit()

    def delete(self, obj=None):
        """Delete obj from the current database session."""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """reload the sesssion"""
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine , expire_on_commit=False))
        self.__session = Session()

    def close(self):
        """Close the working SQLAlchemy session."""
        self.__session.close()