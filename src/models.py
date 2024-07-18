import os
import sys
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    user_id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False, unique=True)
    
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(10), nullable=False, unique=True)
    subscription_date = Column(DateTime, nullable=False)
    

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.user_id'))  
    user = relationship(User)
    planet_id = Column(Integer, ForeignKey('planet.planet_id'))  
    planet = relationship("Planet")
    vehicles_id = Column(Integer, ForeignKey('vehicles.vehicles_id'))  
    vehicles = relationship("Vehicles")
    characters_id = Column(Integer, ForeignKey('characters.characters_id'))  
    characters = relationship("Characters")


class Planet(Base):
    __tablename__ = 'planet' 
    planet_id = Column(Integer, primary_key=True)
    planet_name = Column(String(100), nullable=False)
    rotation_period = Column(Integer, nullable=False)
    diameter = Column(Integer, nullable=False)
    climate = Column(String(100), nullable=True)
    terrain = Column(String(100), nullable=False)


class Characters(Base):
    __tablename__ = 'characters'
    characters_id = Column(Integer, primary_key=True)
    character_name = Column(String(100), nullable=False)
    character_weight = Column(String(100), nullable=True)
    character_hair_color = Column(String(20), nullable=True)
    character_eye_color = Column(String(20), nullable=False)
    character_birth_year = Column(Integer, nullable=False)


class Vehicles(Base): 
    __tablename__ = 'vehicles'
    vehicles_id = Column(Integer, primary_key=True)
    vehicles_name = Column(String(100), nullable=False)
    vehicles_model = Column(String(100), nullable=True)
    vehicles_length = Column(Integer, nullable=True)
    vehicles_cargo_capacity = Column(Integer, nullable=False)
    vehicles_model = Column(String(250), nullable=False)
    vehicles_manufacturer = Column(String(250), nullable=False)
    vehicles_class = Column(String, nullable=False)
#     __tablename__ = 'address'
#     # Here we define columns for the table address.
#     # Notice that each column is also a normal Python instance attribute.
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     user_id = Column(Integer, ForeignKey('user.id'))
#     User = relationship(User)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
