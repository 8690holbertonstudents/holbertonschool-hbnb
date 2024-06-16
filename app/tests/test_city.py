#!/usr/bin/python3
"""
Defines module test_city.py
"""
import unittest
from app.models.city import City
from app.models.country import Country


class TestCity(unittest.TestCase):
    def setUp(self):
        self.country = Country(name="France")
        self.city = City(name="Paris", country=self.country)

    def test_city_creation(self):
        self.assertEqual(self.city.name, "Paris")
        self.assertEqual(self.city.country, self.country)

    def test_city_id_unique(self):
        city1 = City(name="Lyon", country=self.country)
        city2 = City(name="Marseille", country=self.country)
        self.assertNotEqual(city1.id, city2.id)

    def test_city_timestamps(self):
        self.assertIsNotNone(self.city.created_at)
        self.assertIsNotNone(self.city.updated_at)
