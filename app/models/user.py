#!/usr/bin/python3
"""
Defines module user.py
"""
from app.models.base_model import BaseModel


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
