#!/usr/bin/python3
""" It's time to change your storage engine and use SQLAlchemy """
import models
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from sqlalchemy.ext.declarative import declarative_base


class DBStorage():
    """This class will be the New engine"""
    __engine = None
    __session = None

    def __init__(self):
        """The first function when creating the class"""
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.
                                      format(HBNB_MYSQL_USER,
                                             HBNB_MYSQL_PWD,
                                             HBNB_MYSQL_HOST,
                                             HBNB_MYSQL_DB), pool_pre_ping=True)
        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        diccionario = {}
        if cls is None:
            pass
        else:
            objetos = self.__session.query(cls).all()

        for objet in objetos:
            key = f"{objet.__class__.__name__}.{objet.id}"
            diccionario[key] = objet
        return (diccionario)

    def new(self, obj):
        self.__session.add(obj)

    def save(self):
        """ commit all changes of the current database session"""
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """ reload """
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        Base.metadata.create_all(self.__engine)
        session = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session)
        self.__session = Session()
