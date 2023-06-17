#!/usr/bin/python3
"""declares a mapping"""
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy import Column, Integer, String
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)

    def __repr__(self):
        """defines the representation function of the class -User"""
        return f"<User(name={self.name}, fullname={self.fullname}, nickname={self.nickname})>
