#!/usr/bin/python3
"""
"""
from models import BaseModel


class Amenity(BaseModel):
    """
    Defines class Amenity with various attributes
    """

    def __init__(self, name):
        """
        The constructor of the class Amenity
        """

        super().__init__()
        self.name = name
