#!/usr/bin/python3
"""
this module for printing all data in
the databases from table state
"""

from model_state import Base, State
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
import sys

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]

    engine = sql.create_engine('mysql://{}:{}@localhost:\
                               3306/{}'.format(u, p, d))
    Base.metadata.create_all(engine)

    with engine.connect() as conn:
        result = conn.execute(sql.select(State).order_by(State.id))
        for row in result:
            print("{}: {}".format(row.id, row.name))
