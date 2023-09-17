#!/usr/bin/python3
"""create state model
"""


from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class State(Base):
    """create state model
    """
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement='auto',
                nullable=False, unique=True)
    name = Column(String(128), nullable=False)
