#!/usr/bin/python3
"""
this module for printing all data in
the databases from table state
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.ext.declarative import declarative_base
import sys

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]

    engine = create_engine('mysql://{}:{}@localhost:3306/{}'.fromat(u, p, d))
    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        result = conn.execute(select(State))
        for row in result:
            print(row)
