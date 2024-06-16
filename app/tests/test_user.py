#!/usr/bin/python3
"""
Defines module test_user.py
"""
import unittest
from datetime import datetime
from app.models.user import User


class TestUser(unittest.TestCase):
    """
    Defines the class TestUser inherits from TestCase class
    """

    def test_created_at_set_on_creation(self):
        """
        Test if the attribute created_at is updated in the creation of an object
        """
        user = User(email='8688@example.com')
        self.assertIsInstance(user.created_at, datetime)

    def test_updated_at_set_on_update(self):
        """
        Test if the attribute updated_at that updated when we update it
        """
        user = User(email='test@example.com')
        original_updated_at = user.updated_at
        user.email = 'new_email@example.com'
        user.save()
        self.assertNotEqual(user.updated_at, original_updated_at)

    def setUp(self):
        self.user = User(email="test@example.com")

    def test_user_creation(self):
        self.assertEqual(self.user.email, "test@example.com")

    def test_user_id_unique(self):
        user1 = User(email="test1@example.com")
        user2 = User(email="test2@example.com")
        self.assertNotEqual(user1.id, user2.id)

    def test_user_timestamps(self):
        self.assertIsNotNone(self.user.created_at)
        self.assertIsNotNone(self.user.updated_at)

    def test_user_first_last_name(self):
        self.user.first_name = "John"
        self.user.last_name = "Doe"
        self.assertEqual(self.user.first_name, "John")
        self.assertEqual(self.user.last_name, "Doe")


if __name__ == '__main__':
    unittest.main()
