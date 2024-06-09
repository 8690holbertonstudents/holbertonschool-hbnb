#!/usr/bin/python3
"""
"""
from flask_restx import Resource, Namespace

user_ns = Namespace('users', description='user operations')


@user_ns.route('/')
class UserResource(Resource):
    def get(self):
        """
        Retrieve users list
        """
        return ({'message': 'users !'})
