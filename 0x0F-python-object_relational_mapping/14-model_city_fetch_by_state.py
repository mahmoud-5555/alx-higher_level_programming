#!/usr/bin/python3
"""
this module for printing all data in
the databases from table City
"""

from model_city import Base, City
from model_state import State
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
        query = sql.select(State.name, City.id, City.name).join(City, State.id == City.state_id).order_by(City.id)
        result = conn.execute(query)
        result = result.fetchall()
        for row in result:
            print("{}: ({}) {}".format(row[0], row[1],row[2]))
