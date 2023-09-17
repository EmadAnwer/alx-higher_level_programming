#!/usr/bin/python3
"""create state model
"""
from sqlalchemy import Column, Integer
from sqlalchemy.ext.declarative import declarative_base

if __name__ == "__main__":
    Base = declarative_base()


    class State(Base):
        __tablename__ = 'states'
        id = Column(Integer, primary_key=True, autoincrement='auto',
                    nullable=False, unique=True)
        name = Column(String(128), nullable=False)
