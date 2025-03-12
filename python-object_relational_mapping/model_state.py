#!/home/jacob/.local/share/mise/installs/python/3.13.1/bin/python3
from sqlalchemy.orm import declarative_base
from sqlalchemy import Nullable, create_engine, Column, Integer, String, Null


"""Module containing the State Class and information for database entries"""
Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer,
                nullable=False,
                autoincrement=True,
                unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)

