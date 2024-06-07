#!/usr/bin/python3
"""
"""
from models import BaseModel


class City(BaseModel):
    """
    Defines class City with various attributes
    """

    def __init__(self, country_id, name):
        """
        The constructor of the class City
        """
        super().__init__()
        self.country_id = country
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

