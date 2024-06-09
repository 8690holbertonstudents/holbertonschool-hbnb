#!/usr/bin/python3
"""
Module __init__.py to import package routes
"""
from .amenity_routes import amenity_ns
from .city_routes import city_ns
from .country_routes import country_ns
from .place_routes import place_ns
from .review_routes import review_ns
from .user_routes import user_ns

__all__ = ['amenity_ns', 'city_ns', 'country_ns', 'place_ns', 'review_ns',
           'user_ns']
