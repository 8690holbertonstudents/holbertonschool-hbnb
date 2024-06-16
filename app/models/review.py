#!/usr/bin/python3
"""
Defines module review.py
"""
from app.models.base_model import BaseModel
from flask import jsonify


class Review(BaseModel):
    """
    Defines a class Review inherits BaseModel class
    """

    def __init__(self, user_id, place_id, rating, comment):
        """
        The constructor of the class Review
        """
        super().__init__()
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment

    @staticmethod
    def data_check(review_data):
        """
        Common check for POST and PUT
        """
        if 'comment' not in review_data:
            return jsonify({'Error': 'review must have a comment'}), 400

        if 'rating' not in review_data:
            return jsonify({'Error': 'review must have a rating'}), 400

        if not isinstance(review_data['comment'], str):
            return jsonify({'Error': 'review comment is not a string'}), 400

        if not isinstance(review_data['rating'], int) or review_data['rating'] not in range(1, 6):
            return jsonify({'Error': 'rating must be an integer between 1 and 5'}), 400

        if len(review_data['comment']) == 0:
            return jsonify({'Error': 'review comment cannot be empty'}), 400

        return None
