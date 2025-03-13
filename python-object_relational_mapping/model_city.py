#!/usr/bin/python3
"""Module containing the State Class and information for database entries"""
from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import Nullable, create_engine, Column, Integer, String, Null
from sqlalchemy import ForeignKey

Base = declarative_base()


class City(Base):
    """State Class

    Inherits: DeclarativeBase from sqlalchemy.

    Args:
    @id: The id in the databasse, NOT NULL, AUTOINCREMENTING UNIQUE PK.
    @name: The name of the state.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id: Mapped[int] = mapped_column(ForeignKey("states.id"))
    state: Mapped["State"] = relationship(back_populates="cities")
