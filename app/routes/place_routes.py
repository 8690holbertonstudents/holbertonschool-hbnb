#!/usr/bin/python3
"""
"""
from flask_restx import Resource, Namespace

place_ns = Namespace('places', description='place operations')


@place_ns.route('/')
class PlaceList(Resource):
    """
    Define PlaceList class inherit from Resource.
    """

    def get(self):
        """
        Retrieve places list
        """
        pass

    def post(self):
        """
        Add a new place to places list
        """
        pass


@place_ns.route('/<string:id>')
class PlaceResource(Resource):
    """
    Define PlaceResource class inherit from Resource.
    """

    def get(self, id):
        """
        Retrieve place from id
        """
        pass

    def put(self, id):
        """
        Update place from id
        """
        pass

    def delete(self, id):
        """
        Delete place from id
        """
        pass
