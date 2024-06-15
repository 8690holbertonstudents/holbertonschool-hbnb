#!/usr/bin/python3
"""
Defines module country.py
"""


class Country:
    """
    Defines class Country with various attributes
    """

    def __init__(self, name, country_code):
        """
        Initializes the Country class
        """

        self.name = name
        self.code = country_code
        self.cities = []

    def add_city(self, city):
        """
        Adds a City to the country's list of cities.
        """
        self.cities.append(city)
