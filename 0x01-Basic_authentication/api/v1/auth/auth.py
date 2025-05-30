#!/usr/bin/env python3
"""
Auth class
"""
from typing import List, TypeVar

from flask import request


class Auth:
    """
    authentication class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        :return: False
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        request headers
        :return: requests
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """

        :param request:
        :return:
        """
        return None
