
#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv

from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

import models
from models.base_model import Base, BaseModel
from models.city import City


class State(BaseModel ,Base):
    """ State class """
    __tablename__ = 'states'
    name = Column(String(128) , nullable=False)
    cities = relationship(City , backref="state" , cascade="all, delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related City objects."""
            city_list = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list