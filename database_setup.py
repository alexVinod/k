import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

from flask_login import UserMixin

Base = declarative_base()

class Owner(Base, UserMixin):
    __tablename__ = 'ownerDetails'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)    
    email = Column(String(250), unique=True)
    password = Column(String(250), nullable=False)
    image = Column(String(250), nullable=False)
    ownerType = Column(String(250), nullable=False)


class Restaurant(Base):
    __tablename__ = 'restaurant'

    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    image = Column(String(3050), nullable=False )
    
    owner_id = Column(Integer, ForeignKey('ownerDetails.id'))
    owner = relationship(Owner)

    @property
    def serialize(self):
        return {
            'name':self.name,
            'id':self.id
        }

class MenuItem(Base):
    __tablename__ = 'menu_item'

    name = Column(String(80), nullable=False)
    id = Column(Integer, primary_key=True)
    description = Column(String(250))
    price = Column(String(8))
    course = Column(String(250))
    restaurant_id = Column(Integer, ForeignKey('restaurant.id'))
    restaurant = relationship(Restaurant)

    owner_id = Column(Integer, ForeignKey('ownerDetails.id'))
    owner = relationship(Owner)

    @property
    def serialize(self):
        #Returns object data in easily serializeable format
        return {            
            'name':self.name,
            'id':self.id,
            'description':self.description,
            'price':self.price,
            'course':self.course,
            'restaurant_id':self.restaurant_id,
            'restaurant':str(self.restaurant)
        }
    

engine = create_engine('sqlite:///restaurantmenu.db')


Base.metadata.create_all(engine)