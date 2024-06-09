#!/usr/bin/python3
"""
"""
from flask_restx import Resource, Namespace

country_ns = Namespace('countries', description='country operations')


@country_ns.route('/')
class CountryList(Resource):
    """
    Define CountryList class inherit from Resource.
    """

    def get(self):
        """
        Retrieve countries list
        """
        pass


@country_ns.route('/<string:id>')
class CountryResource1(Resource):
    """
    Define CountryResource1 class inherit from Resource.
    """

    def get(self, id):
        """
        Retrieve country from id
        """
        pass


@country_ns.route('/<string:id>/cities')
class CountryResource2(Resource):
    """
    Define CountryResource2 class inherit from Resource.
    """

    def get(self, id):
        """
        Retrieve cities from a country id
        """
        pass
