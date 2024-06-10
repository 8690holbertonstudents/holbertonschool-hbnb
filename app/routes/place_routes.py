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


@place_ns.route('/<string:place_id>')
class PlaceResource(Resource):
    """
    Define PlaceResource class inherit from Resource.
    """

    def get(self, place_id):
        """
        Retrieve place from id
        """
        pass

    def put(self, place_id):
        """
        Update place from id
        """
        pass

    def delete(self, place_id):
        """
        Delete place from id
        """
        pass


@place_ns.route('/<string:place_id>/reviews')
class PlaceReview(Resource):
    """
    Define PlaceReview class inherit from Resource.
    """

    def get(self, place_id):
        """
        Retrieve review list from a specific place
        """
        pass

    def post(self, place_id):
        """
        Add a new review for a specific place
        """
        pass
