#!/usr/bin/python3
"""
Defines module user.py
"""
from models import BaseModel


class User(BaseModel):
    """
    Defines class User inherits from the class BaseModel
    """

    def __init__(self, email, user_pwd, first_name='', last_name='', id=None, created_at=None, updated_at=None):
        """
        Constructor of class User
        """

        super().__init__(id=id, created_at=created_at, updated_at=updated_at)
        self.email = email
        self.user_pwd = user_pwd
        self.first_name = first_name
        self.last_name = last_name
        self.places = []
        self.reviews = []


    def add_place(self, name, description):
        """
        Method that add place to a list of places of a specific user

        Args:
            name: the name of new place
            description: the description of a new place
        Returns:
            a new place of a specific user
        """

        place = Place(name=name, description=description, user_id=self.id)
        self.places.append(place)
        return place

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

