#!/usr/bin/python3
"""
"""
from flask import jsonify
from flask_restx import Resource, Namespace
from app.persistence.data_manager import DataManager


amenity_ns = Namespace('amenities', description='Amenity operations')
data_manager = DataManager()


@amenity_ns.route('/')
class AmenityList(Resource):
    """
    Define AmenityList class inherit from Resource.
    """

    def get(self):
        """
        Retrieve amenities list
        """
        amenities = data_manager.get_all('amenity')
        return jsonify(amenities)

    def post(self, name):
        """
        Add a new amenity to amenities list
        """
        amenity = data_manager.save(name, 'amenity')
        return jsonify(amenity)


@amenity_ns.route('/<string:amenity_id>')
class AmenityResource(Resource):
    """
    Define AmenityResource class inherit from Resource.
    """

    def get(self, amenity_id):
        """
        Retrieve amenity from id
        """
        amenity = data_manager.get(amenity_id, 'amenity')
        if amenity is None:
            return {"message": "Amenity not found"}, 404
        return jsonify(amenity)

    def put(self, amenity_id):
        """
        Update amenity from id
        """
        pass

    def delete(self, amenity_id):
        """
        Delete amenity from id
        """
        pass
