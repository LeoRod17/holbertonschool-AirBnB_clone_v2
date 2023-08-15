#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        cities = relationship('City', backref='states',
                              cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            from models import storage
            from models import city
            lista = []
            for x, in storage.all(city).values():
                if x.state_id == self.id:
                    list.append(x)
                return lista
