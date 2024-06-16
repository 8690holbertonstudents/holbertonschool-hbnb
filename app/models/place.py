#!/usr/bin/python3
"""
Defines module place.py
"""
from app.models.base_model import BaseModel


class Place(BaseModel):
    """
    Defines class Place inherits of BaseModel class
    """

    def __init__(self, name, description, address, city_id, latitude, longitude, host_id,
                 num_rooms, num_bathrooms, price_per_night, max_guest):
        """
        The constructor that initialise attributes of the class Place
        """
        super().__init__()
        self.name = name
        self.description = description
        self.address = address
        self.city_id = city_id
        self.latitude = latitude
        self.longitude = longitude
        self.host_id = host_id
        self.num_rooms = num_rooms
        self.num_bathrooms = num_bathrooms
        self.price_per_night = price_per_night
        self.max_guest = max_guest
        self.amenities = []
        self.reviews = []

    def add_amenity(self, amenity):
        """
        Adds an amenity to the place
        """
        if amenity not in self.amenities:
            self.amenities.append(amenity)

    def remove_amenity(self, amenity):
        """
        Removes an amenity from the place
        """
        if amenity in self.amenities:
            self.amenities.remove(amenity)

    def add_review(self, review):
        """
        Adds a review to the place
        """
        self.reviews.append(review)

    def remove_review(self, review_id):
        """
        Removes a review from the place by review_id
        """
        for review in self.reviews:
            if review['review_id'] != review_id:
                self.reviews = review
