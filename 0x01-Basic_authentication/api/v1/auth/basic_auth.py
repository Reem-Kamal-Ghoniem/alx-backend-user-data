#!/usr/bin/env python3
""" Basic auth
"""

from api.v1.auth.auth import Auth


class BasicAuth(Auth):
    """ BasicAuth class.
    """

    def extract_base64_authorization_header(self, ah: str) -> str:
        """ def extract_base64_header.
        """
        if not ah or type(ah) is not str or not ah.startswith("Basic "):
            return
        return "".join(ah.split(" ")[1:])
