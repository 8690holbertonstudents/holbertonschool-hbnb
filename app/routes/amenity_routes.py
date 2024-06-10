#!/usr/bin/python3
"""
"""
from flask_restx import Resource, Namespace

amenity_ns = Namespace('amenities', description='Amenity operations')


@amenity_ns.route('/')
class AmenityList(Resource):
    """
    Define AmenityList class inherit from Resource.
    """

    def get(self):
        """
        Retrieve amenities list
        """
        pass

    def post(self):
        """
        Add a new amenity to amenities list
        """
        pass


@amenity_ns.route('/<string:amenity_id>')
class AmenityResource(Resource):
    """
    Define AmenityResource class inherit from Resource.
    """

    def get(self, amenity_id):
        """
        Retrieve amenity from id
        """
        pass

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
