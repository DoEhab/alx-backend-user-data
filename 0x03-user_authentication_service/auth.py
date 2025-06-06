#!/usr/bin/env python3
"""
define a hash pass function
"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """
    hash user passwords
    """
    password_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()

    return bcrypt.hashpw(password_bytes, salt)
