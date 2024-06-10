#!/usr/bin/python3
"""
"""
from flask_restx import Resource, Namespace

review_ns = Namespace('reviews', description='review operations')


@review_ns.route('/<string:review_id>')
class ReviewResource(Resource):
    """
    Define ReviewResource class inherit from Resource.
    """

    def get(self, review_id):
        """
        Retrieve review from id
        """
        pass

    def put(self, review_id):
        """
        Update review from id
        """
        pass

    def delete(self, review_id):
        """
        Delete review from id
        """
        pass
