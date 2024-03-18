#!/usr/bin/python3
"""
this module for printing the frist row in
the databases from table state
"""

from model_state import Base, State
import sqlalchemy as sql
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sys
from re import search as se

if __name__ == "__main__":
    u = sys.argv[1]
    p = sys.argv[2]
    d = sys.argv[3]

    engine = sql.create_engine('mysql://{}:{}@localhost:\
                               3306/{}'.format(u, p, d))
    with engine.connect() as conn:
        conn.execute(sql.delete(State)
                     .where(State.name.like('%a%')))
        conn.commit()
