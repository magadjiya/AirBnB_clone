#!/usr/bin/python3
"""Test file for User Class"""
import unittest
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
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

    def test_default(self):
        """
        Tests default attributes
        """
        my_amenity = Amenity()
        my_amenity.name = "anything"
        self.assertEqual(my_amenity.name, "anything")


if __name__ == '__main__':
    unittest.main()
