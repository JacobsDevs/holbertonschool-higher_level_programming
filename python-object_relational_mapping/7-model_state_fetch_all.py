#!/usr/bin/python3
"""Lists the states in the database using sqlalchemy"""
import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from model_state import Base, State

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = Session(engine)

    stmt = select(State)

    for state in session.scalars(stmt):
        print("{}: {}".format(state.id, state.name))
