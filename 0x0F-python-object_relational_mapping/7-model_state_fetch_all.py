#!/usr/bin/python3

from model_state import Base, State
from sqlalchemy import Column, Integer, String, create_engine, select
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_4_usa')
Base.metadata.create_all(engine)

with engine.connect() as conn:
    result = conn.execute(select(State))
    for row in result:
        print(row)
