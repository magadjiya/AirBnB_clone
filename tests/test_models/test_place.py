#!/usr/bin/python3
"""Test file for User Class"""
import unittest
from models.place import Place


class TestPlace(unittest.TestCase):
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
        Testing default values
        """
        my_place = Place()
        my_place.latitude = 5
        self.assertEqual(my_place.latitude, 10)


if __name__ == '__main__':
    unittest.main()
