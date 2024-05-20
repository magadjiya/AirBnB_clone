#!/usr/bin/python3
"""The test module for the base model"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """
    Test cases for `BaseModel` class
    """

    def setUp(self):
        """
        Class needed for testing
        """
        pass

    def test_inputs(self):
        """
        Tests normal inputs for the BaseModel
        """
        my_model = BaseModel()
        my_model.name = "Ebuka"
        my_model.number = 89
        self.assertEqual([my_model.name, my_model.number], ["Ebuka", 89])

    def test_datetime(self):
        """
        Test for datetime attribute
        """
        pass


if __name__ == '__main__':
    unittest.main()
