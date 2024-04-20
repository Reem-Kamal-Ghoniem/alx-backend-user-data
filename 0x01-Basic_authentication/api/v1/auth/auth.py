#!/usr/bin/env python3
""" Auth class
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """ Auth class.
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ def require_auth
        """
        if not path or not excluded_paths:
            return True
        path = path + '/' if path[-1] != '/' else path
        wildcard = any(x.endswith("*") for x in excluded_paths)
        if not wildcard:
            return path not in excluded_paths
        for e in excluded_paths:
            if e.endswith("*"):
                if path.startswith(e[:-1]):
                    return False
            if path == e:
                return False
        return True


def authorization_header(self, request=None) -> str:
    """ auth header
    """
    if request:
        return request.headers.get("Authorization")
    return None


def current_user(self, request=None) -> TypeVar('User'):
    """current user function
    """
    return None
