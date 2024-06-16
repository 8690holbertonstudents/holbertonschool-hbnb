#!/usr/bin/python3
"""
"""
from app.models.base_model import BaseModel
from flask import jsonify


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

    @staticmethod
    def data_check(city_data):
        """
        Common check for POST and PUT
        """
        if 'name' not in city_data:
            return jsonify({'Error': 'city must have a name'}), 400

        if not isinstance(city_data['name'], str):
            return jsonify({'Error': 'city name is not a string'}), 400

        if len(city_data['name']) == 0:
            return jsonify({'Error': 'city name cannot be empty'}), 400

        return None

    def add_place(self, place):
        """
        Adds a Place to the city's list of places.

        Args:
            place (Place): The place to add to the city.

        Returns:
            None
        """

        self.places.append(place)
