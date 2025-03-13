#!/home/jacob/.local/share/mise/installs/python/3.13.1/bin/python
#!/usr/bin/python3
"""Lists the first state in the database using sqlalchemy"""
import sys
from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]))
    session = Session(engine)

    query = select(City).order_by(City.id)

    for i in session.scalars(query):
        print("{}: ({}) {}".format(i.state.name, i.id, i.name))
