#!/usr/bin/python3
"""
Defines module test_amenity.py
"""
import unittest
from app.models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity(name="WiFi")

    def test_amenity_creation(self):
        self.assertEqual(self.amenity.name, "WiFi")

    def test_amenity_id_unique(self):
        amenity1 = Amenity(name="Pool")
        amenity2 = Amenity(name="Parking")
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_amenity_timestamps(self):
        self.assertIsNotNone(self.amenity.created_at)
        self.assertIsNotNone(self.amenity.updated_at)


if __name__ == '__main__':
    unittest.main()
