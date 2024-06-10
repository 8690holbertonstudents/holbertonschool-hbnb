#!/usr/bin/python3
"""
"""
from models import BaseModel


class Amenity(BaseModel):
    """
    Defines class Amenity with various attributes
    """

    def __init__(self, name, amenity_id=None, created_at=None, updated_at=None):
        """
        The constructor of the class Amenity
        """

        super().__init__(id=amenity_id, created_at=created_at, updated_at=updated_at)
        self.name = name
