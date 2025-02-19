#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import os

class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False,)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False,)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float)
    longitude = Column(Float)

    if os.getenv('HBNB_TYPE_STORAGE') == 'db':
        place = relationship('Review', backref='places', cascade="all, delete-orphan")
    else:
        def reviews(self):
            from models import storage
            lista = []
            for x, y in storage.__objects.items():
                split = x.split(".")
                if split[0] == "Review":
                    lista.append(y)
                    filt = list(
                        filter(lambda a: a.place_id == self.id), lista)
                    return filt


place_amenity = Table('place_amenity', Base.metadata,
Column('place_id', String(60), ForeignKey('places.id'), nullable=False, primary_key=True),
Column('amenity_id', String(60), ForeignKey('amenities.id'), nullable=False, primary_key=True))
