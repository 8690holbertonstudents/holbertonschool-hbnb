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


@country_ns.route('/<string:country_code>')
class CountryResource1(Resource):
    """
    Define CountryResource1 class inherit from Resource.
    """

    def get(self, country_code):
        """
        Retrieve country from country_code
        """
        pass


@country_ns.route('/<string:country_code>/cities')
class CountryResource2(Resource):
    """
    Define CountryResource2 class inherit from Resource.
    """

    def get(self, country_code):
        """
        Retrieve cities from a country_code
        """
        pass
