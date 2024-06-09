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


@amenity_ns.route('/<string:id>')
class AmenityResource(Resource):
    """
    Define AmenityResource class inherit from Resource.
    """

    def get(self, id):
        """
        Retrieve amenity from id
        """
        pass

    def put(self, id):
        """
        Update amenity from id
        """
        pass

    def delete(self, id):
        """
        Delete amenity from id
        """
        pass
