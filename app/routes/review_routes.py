#!/usr/bin/python3
"""
"""
from flask_restx import Resource, Namespace

review_ns = Namespace('reviews', description='review operations')






@review_ns.route('/<string:id>')
class ReviewResource(Resource):
    """
    Define ReviewResource class inherit from Resource.
    """

    def get(self, id):
        """
        Retrieve review from id
        """
        pass

    def put(self, id):
        """
        Update review from id
        """
        pass

    def delete(self, id):
        """
        Delete review from id
        """
        pass
