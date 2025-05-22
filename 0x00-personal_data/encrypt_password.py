#!/usr/bin/env python3
"""
function hash_password
"""
import bcrypt


def hash_password(password: str) -> bytes:
    """
    :param password: plain text
    :return: hashed password
    """
    encoded_pass = password.encode('UTF-8')
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(encoded_pass, salt)


def is_valid(hashed_password: bytes, password: str) -> bool:
    """
    :param hashed_password: hashed pass
    :param password: plain password
    :return: True or False
    """
    return bcrypt.checkpw(password.encode('UTF-8'), hashed_password)
