#!/usr/bin/python3
""" It’s time to change your storage engine and use SQLAlchemy """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session

Base = declarative_base()
class DBStorage:
    """This class will be the New engine"""
    __engine = None
    __session = None
    def __init__(self):
        """The first function when creating the class"""
        self.__engine = create_engine(f'mysql+mysqldb://{os.getenv["HBNB_MYSQL_USER"]}:{os.getenv["HBNB_MYSQL_PWD"]}@{os.getenv["HBNB_MYSQL_HOST"]}:3306/{os.getenv["HBNB_MYSQL_DB"]}', pool_pre_ping=True)
        if os.getenv['HBNB_ENV'] == 'test':
            Meta = Base.MetaData(self.__engine)
            Meta.drop_all()
    def save(self):
        """"""
#    def all(self, cls=None):

"""    def reload(self):
        self.__engine = create_engine(f'mysql+mysqldb://{os.getenv["HBNB_MYSQL_USER"]}:{os.getenv["HBNB_MYSQL_PWD"]}@{os.getenv["HBNB_MYSQL_HOST"]}:3306/{os.getenv["HBNB_MYSQL_DB"]}', pool_pre_ping=True)
        Meta = Base.MetaData(self.__engine)
        self.__session = sessionmaker(expire_on_commit=False, bind=self.__engine)
        scoped_session(self.__session)
        Meta.create_all() """
    
        