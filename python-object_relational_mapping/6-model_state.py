#!/home/jacob/.local/share/mise/installs/python/3.13.1/bin/python3
"""Start link class to table in database 
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://jacob:jacob@172.17.0.2/hbtn_0d_usa')
    Base.metadata.create_all(engine)

