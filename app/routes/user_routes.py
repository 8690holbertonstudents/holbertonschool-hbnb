#!/usr/bin/python3
"""
"""
from flask_restx import Resource, Namespace

user_ns = Namespace('users', description='user operations')


@user_ns.route('/')
class UserList(Resource):
    """
    Define UserList class inherit from Resource.
    """

    def get(self):
        """
        Retrieve users list
        """
        pass

    def post(self):
        """
        Add a new user to users list
        """
        pass


@user_ns.route('/<string:id>')
class UserResource(Resource):
    """
    Define UserResource class inherit from Resource.
    """

    def get(self, id):
        """
        Retrieve user from id
        """
        pass

    def put(self, id):
        """
        Update user from id
        """
        pass

    def delete(self, id):
        """
        Delete user from id
        """
        pass


@user_ns.route('/<string:id>/reviews')
class UserReview(Resource):
    """
    Define UserReview class inherit from Resource.
    """

    def get(self, id):
        """
        Retrieve review list from a specific user
        """
        pass
