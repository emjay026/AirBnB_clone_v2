#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.city import City
from models import storage

from base_model import Base, Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state")

    @property
    def cities(self):
        """getter for list of city instances related to the state"""
        city_list = []
        all_cities = storage.all(City)
        for city in all_cities.values():
            if city.state_id == self.id:
                city_list.append(city)
        return city_list

# class State(BaseModel):
#     """ State class """
#     name = ""
