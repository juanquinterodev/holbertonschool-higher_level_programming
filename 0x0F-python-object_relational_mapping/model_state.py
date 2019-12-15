#!/usr/bin/python3
""" State model
"""
from SQLAlchemy import column, integer, string
from SQLAlchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class
    """
    __table__ = 'states'

    id = column(integer, primary_key=True, autoincrement=True, unique=True,
                nullable=False)
    name = column(string(128), nullable=False)
