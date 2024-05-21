#!/usr/bin/python3
"""Test file for User Class"""
import unittest
from models.engine.file_storage import FileStorage


class TestCity(unittest.TestCase):
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
        storage = FileStorage()
        self.assertEqual(storage.reload(), '11111')


if __name__ == '__main__':
    unittest.main()
