#!/usr/bin/python3
"""
Defines module test_place.py
"""
import unittest
from app.models.user import User
from app.models.city import City
from app.models.place import Place


class TestPlace(unittest.TestCase):
    def setUp(self):
        self.user = User(email="host@example.com", password="password")
        self.city = City(name="Paris", country="France")
        self.place = Place(name="Beautiful Apartment",
                           description="Lovely place", city=self.city, host=self.user)

    def test_place_creation(self):
        self.assertEqual(self.place.name, "Beautiful Apartment")
        self.assertEqual(self.place.city, self.city)
        self.assertEqual(self.place.host, self.user)

    def test_place_attributes(self):
        self.place.rooms = 2
        self.place.bathrooms = 1
        self.place.price_per_night = 100
        self.place.max_guests = 4
        self.place.latitude = 48.8566
        self.place.longitude = 2.3522
        self.assertEqual(self.place.rooms, 2)
        self.assertEqual(self.place.bathrooms, 1)
        self.assertEqual(self.place.price_per_night, 100)
        self.assertEqual(self.place.max_guests, 4)
        self.assertEqual(self.place.latitude, 48.8566)
        self.assertEqual(self.place.longitude, 2.3522)

    def test_place_amenities(self):
        self.place.amenities = ["WiFi", "Pool"]
        self.assertIn("WiFi", self.place.amenities)
        self.assertIn("Pool", self.place.amenities)


if __name__ == '__main__':
    unittest.main()
