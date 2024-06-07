#!/usr/bin/python3
"""
Defines module review.py
"""
from models import BaseModel


class Review(BaseModel):
    """
    Defines a class Review inherits BaseModel class
    """

    def __init__(self, user_id, place_id, rating, comment):
        """
        The constructor of the class Review
        """
        super().__init__()  # Appel au constructeur de BaseModel
        self.user_id = user_id
        self.place_id = place_id
        self.rating = rating
        self.comment = comment
