#!/usr/bin/python3
"""Test file for User Class"""
import unittest
from models.user import User


class TestUser(unittest.TestCase):
    """
    Tests the User data model
    """

    def setUp(self):
        """
        Test for all classes
        """
        pass

    def test_attributes(self):
        """
        Tests attributes assignment with expected values
        """
        pass

    def test_defaults(self):
        """
        Tests default values for User class
        """
        my_user = User()
        my_user.name = "Maverick"
        self.assertEqual(my_user.name, "Maverick")


if __name__ == '__main__':
    unittest.main()
