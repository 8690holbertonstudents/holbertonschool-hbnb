#!/usr/bin/python3
"""
"""
from app.models.base_model import BaseModel


class City(BaseModel):
    """
    Defines class City with various attributes
    """

    def __init__(self, country_code, name):
        """
        The constructor of the class City
        """
        super().__init__()
        self.country_code = country_code
        self.name = name
        self.places = []

    def add_place(self, place):
        """
        Adds a Place to the city's list of places.

        Args:
            place (Place): The place to add to the city.

        Returns:
            None
        """

        self.places.append(place)
