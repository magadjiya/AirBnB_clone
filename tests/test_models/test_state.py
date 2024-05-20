#!/usr/bin/python3
"""Test file for User Class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
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
        Test defaults for State Class
        """
        my_state = State()
        my_state.name = "Florida"
        self.assertEqual(my_state.name, "Florida")


if __name__ == '__main__':
    unittest.main()
