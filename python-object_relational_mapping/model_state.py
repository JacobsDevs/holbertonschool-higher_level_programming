#!/usr/bin/python3
from sqlalchemy.orm import declarative_base
from sqlalchemy import Nullable, create_engine, Column, Integer, String, Null


"""Module containing the State Class and information for database entries"""
Base = declarative_base()

class State(Base):
    """State Class

    Inherits: DeclarativeBase from sqlalchemy.

    Args:
    @id: The id in the databasse, NOT NULL, AUTOINCREMENTING UNIQUE PK.
    @name: The name of the state.
    """
    __tablename__ = 'states'

    id = Column(Integer,
                nullable=False,
                autoincrement=True,
                unique=True,
                primary_key=True)
    name = Column(String(128), nullable=False)

