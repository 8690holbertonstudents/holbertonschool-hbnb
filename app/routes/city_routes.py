#!/usr/bin/python3
"""
"""
from flask_restx import Resource, Namespace

city_ns = Namespace('cities', description='city operations')


@city_ns.route('/')
class CityList(Resource):
    """
    Define CityList class inherit from Resource.
    """

    def get(self):
        """
        Retrieve cities list
        """
        pass

    def post(self):
        """
        Add a new city to cities list
        """
        pass


@city_ns.route('/<string:id>')
class CityResource(Resource):
    """
    Define CityResource class inherit from Resource.
    """

    def get(self, id):
        """
        Retrieve city from id
        """
        pass

    def put(self, id):
        """
        Update city from id
        """
        pass

    def delete(self, id):
        """
        Delete city from id
        """
        pass
