#!/usr/bin/python3
"""
module for class that mange databases
"""
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """databases class  to manage the state of a device."""
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __init__(self, name):
        self.name = name


engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_4_usa')
