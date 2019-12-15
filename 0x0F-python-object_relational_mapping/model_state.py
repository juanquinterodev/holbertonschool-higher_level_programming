#!/usr/bin/python3
""" State model
"""
from SQLAlchemy import Column, Integer, String
from SQLAlchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    """
    __table__ = 'states'

    id = Column(Integer, primary_key=True, autoincrement=True, unique=True,
                nullable=False)
    name = Column(String(128), nullable=False)
