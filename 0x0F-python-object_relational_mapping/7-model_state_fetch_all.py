#!/usr/bin/python3
"""
this module for printing all data in
the databases from table state
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_4_usa')
Base.metadata.create_all(engine)
if __name__ == "__main__":
    with engine.connect() as conn:
        result = conn.execute(select(State))
        for row in result:
            print(row)
