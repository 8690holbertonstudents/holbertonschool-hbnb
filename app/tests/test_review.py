#!/usr/bin/python3
"""
Defines module test_review.py
"""
import unittest
from app.models.user import User
from app.models.place import Place
from app.models.city import City
from app.models.review import Review


class TestReview(unittest.TestCase):
    def setUp(self):
        self.user = User(email="reviewer@example.com")
        self.city = City(name="Paris", country="France")
        self.place = Place(name="Beautiful Apartment",
                           description="Lovely place", city=self.city, host=self.user)
        self.review = Review(user=self.user, place=self.place,
                             text="Great place!", rating=5)

    def test_review_creation(self):
        self.assertEqual(self.review, self.user)
        self.assertEqual(self.review, self.place)
        self.assertEqual(self.review.comment, "Great place!")
        self.assertEqual(self.review.rating, 5)

    def test_review_timestamps(self):
        self.assertIsNotNone(self.review.created_at)
        self.assertIsNotNone(self.review.updated_at)


if __name__ == '__main__':
    unittest.main()
