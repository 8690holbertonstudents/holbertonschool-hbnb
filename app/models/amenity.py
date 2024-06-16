#!/usr/bin/python3
"""
"""
from app.models.base_model import BaseModel
from flask import jsonify


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

    @staticmethod 
    def data_check(amenity_data):
        """
        Common check for POST and PUT
        """
        if 'name' not in amenity_data:
            return jsonify({'Error': 'amenity must have a name'}), 400

        if not isinstance(amenity_data['name'], str):
            return jsonify({'Error': 'amenity name is not a string'}), 400

        if len(amenity_data['name']) == 0:
            return jsonify({'Error': 'amenity name cannot be empty'}), 400

        return None
