#!/usr/bin/python3
""" Review module for the HBNB project """
from base_model import BaseModel, Base, Column, String
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


class Review(BaseModel):
    """ Review class to store review information """
    __tablename__ = 'reviews'
    place_id = Column(String(60), ForeignKey('places.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    text = Column(String(1024), nullable=False)
