#!/usr/bin/python3
"""
"""
from models import BaseModel


class Place(BaseModel):
    """
    """

    def __init__(self, email, user_pwd, first_name, last_name):
        """
        """
        self.email = email
        self.user_pwd = user_pwd
        self.first_name = first_name
        self.last_name = last_name
