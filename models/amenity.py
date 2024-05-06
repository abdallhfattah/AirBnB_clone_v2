#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, String

from models.base_model import Base, BaseModel


class Amenity(BaseModel, Base):
    __tablename__ = 'Amenity'
    name = ""
