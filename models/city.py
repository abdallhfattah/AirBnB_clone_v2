#!/usr/bin/python3
""" City Module for HBNB project """
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from models.base_model import Base, BaseModel


class City(BaseModel,Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    name = Column(String(128) , nullable=False)
    # adding __tablename__.id as string form to avoid circular dependency
    state_id = Column(String(60) ,ForeignKey("states.id") ,nullable=False )
