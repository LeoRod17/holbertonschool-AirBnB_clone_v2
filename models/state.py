#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db_storage':
        cities = relationship('City', backref='states', cascade="all, delete-orphan")
    else:
        @property
        def cities(self):
            from models import storage
            lista = []
            for x, y in storage.__objects.items():
                split = x.split(".")
                if split[0] == "City":
                    lista.append(y)
                    filt = list(
                        filter(lambda a: a.state_id == self.id), lista)
                    return filt
                