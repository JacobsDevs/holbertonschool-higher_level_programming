#!/usr/bin/python3
"""Module containing the State Class and information for database entries"""
from sqlalchemy.orm import relationship, declarative_base, mapped_column, Mapped
from sqlalchemy import Nullable, create_engine, Column, Integer, String, Null
from model_city import Base


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
    cities: Mapped[list["City"]] = relationship()
