#!/usr/bin/python3
"""This module defines a class User"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel


class User(BaseModel, Base):
    """This class defines a user by various attributes"""
    __tablename__ = "users"
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128))
    last_name = Column(String(128))

    places = relationship("Place", backref="user", cascade="delete")
    # reviews = relationship("Review", backref="user", cascade="delete")

# 953b9aed-df48-4298-9118-be87ffd598fe STATE
# 7ccd2bcb-b447-4b42-b290-678111c80207 CITY 
# dbfc557e-0454-4988-b2ff-d117488083f2 CITY
# 30c2a559-48fe-4940-a166-026f36713e61 USER
#  create Place city_id="7ccd2bcb-b447-4b42-b290-678111c80207" user_id="30c2a559-48fe-4940-a166-026f36713e61" name="Lovely_place" number_rooms=3 number_bathrooms=1 max_guest=6 price_by_night=120 latitude=37.773972 longitude=-122.431297