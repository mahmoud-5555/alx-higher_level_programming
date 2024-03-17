#!/usr/bin/python3
"""
this module for printing the frist row in
the databases from table state
"""

from model_state import Base, State
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
import sys
from re import search as se

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]
    s = sys.argv[4]

    engine = sql.create_engine('mysql://{}:{}@localhost:\
                               3306/{}'.format(u, p, d))
    Base.metadata.create_all(engine)
    id = State.id
    s_n = State.name
    with engine.connect() as conn:
        result = conn.execute(sql.select(State.id).
                              where(State.name == s))
    row = result.fetchone()
    print("{}".format(row[0]))
