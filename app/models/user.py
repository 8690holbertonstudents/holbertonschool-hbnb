#!/usr/bin/python3
"""
Defines module user.py
"""
from app.models.base_model import BaseModel
from flask import jsonify
import re


class User(BaseModel):
    """
    Defines class User inherits from the class BaseModel
    """

    def __init__(self, email, first_name, last_name):
        """
        Constructor of class User
        """

        super().__init__()
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.places = []
        self.reviews = []

    @staticmethod
    def str_email_check(email):
        """
        Check email string content (not a real validation).
        """
        email_regex = re.compile(
            r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)"
        )
        return re.match(email_regex, email) is not None

    @staticmethod
    def data_check(user_data):
        """
        Common check for POST and PUT
        """
        if not user_data:
            return jsonify({'Error': 'Bad request, no data'}), 400

        if not isinstance(user_data, dict):
            return jsonify({'Error': 'user is not JSON object'}), 400

        if 'email' not in user_data or len(user_data['email']) == 0:
            return jsonify({'Error': 'user must have an email'}), 400

        if not User.str_email_check(user_data['email']):
            return jsonify({'Error': 'email string is not valid'}), 400

        if 'first_name' not in user_data or len(user_data['first_name']) == 0:
            return jsonify({'Error': 'user must have a first_name'}), 400

        if 'last_name' not in user_data or len(user_data['last_name']) == 0:
            return jsonify({'Error': 'user must have a last_name'}), 400

        if len(user_data) != 3:
            return jsonify({'Error': 'user must contain 3 elements'}), 400

        if not isinstance(user_data['email'], str) \
                or not isinstance(user_data['first_name'], str) \
                or not isinstance(user_data['last_name'], str):
            return jsonify({'Error': 'request data must be string'}), 400

        return None

    def add_place(self, place):
        """
        Method that adds a place to the user's list of places

        Args:
            place: An instance of the Place class

        Returns:
            The place added to the user's list of places
        """
        if isinstance(place, Place):
            place.host_id = self.id  # Assurez-vous que l'ID de l'hôte est défini
            self.places.append(place)
            return place
        else:
            raise TypeError("Expected a Place instance")

    def add_review(self, place_id, text):
        """
        Method that add review to a list of reviews of a specific user

        Args:
            place_id: the identifier to a place 
            text: the description of a new place
        Returns:
            a new place of a specific user
        """

        review = Review(place_id=place_id, user_id=self.id, text=text)
        self.reviews.append(review)
        return review
