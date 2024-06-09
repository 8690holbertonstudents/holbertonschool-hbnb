#!/usr/bin/python3
"""
"""
from flask_restx import Resource, Namespace

review_ns = Namespace('reviews', description='review operations')


@review_ns.route('/')
class ReviewResource(Resource):
    def get(self):
        """
        Retrieve reviews list
        """
        return ({'message': 'reviews !'})
