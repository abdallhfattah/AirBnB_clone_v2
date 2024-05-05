#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from models.base_model import BaseModel


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
