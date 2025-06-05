#!/usr/bin/env python3
from sqlalchemy import Integer, Column, String
from sqlalchemy.ext.declarative import declarative_base
"""
class User for data mode
"""
Base = declarative_base()


class User(Base):
    """
    Define table users
    """
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    session_id = Column(String, nullable=True)
    reset_token = Column(String, nullable=True)
