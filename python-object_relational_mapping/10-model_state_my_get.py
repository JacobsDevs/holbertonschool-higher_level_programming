#!/usr/bin/python3
"""Lists the first state in the database using sqlalchemy"""
import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from model_state import Base, State


if __name__ == "__main__":
    if ";" in sys.argv[4]:
        exit()
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = Session(engine)

    query = select(State).where(State.name == sys.argv[4])
    state = session.scalars(query).first()

    if state is None:
        print("Not found")
    else:
        print(state.id)
