#!/usr/bin/env python3
"""
define a hash pass function
"""
import bcrypt
from sqlalchemy.orm.exc import NoResultFound

from db import DB
from user import User


class Auth:
    """Auth class to interact with the authentication database.
    """

    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """
        register a new user
        :param email: user email
        :param password: user password
        :return: user
        """
        try:
            self._db.find_user_by(email=email)
            raise ValueError(f"User {email} already exists")
        except NoResultFound:
            hashed_pass = _hash_password(password)
            return self._db.add_user(email, hashed_pass)


def _hash_password(password: str) -> bytes:
    """
    Hash user passwords
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password_bytes, salt)
