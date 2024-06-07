#!/usr/bin/python3
"""
Defines module country.py
"""
import .models from BaseModel


class Country:
    """
    Defines class Country with various attributes
    """

    def __init__(self, name, code):
        """
        Initializes a Country instance

        Args:
            name (str): The name of the country.
            code (str): The code of the country
        """

        super().__init__()
        self.name = name
        self.code = code
        self.cities = []

    def add_city(self, city):
        """
        Adds a City to the country's list of cities.

        Args:
            city (City): The city to add to the country.

        Returns:
            None
        """
        self.cities.append(city)
