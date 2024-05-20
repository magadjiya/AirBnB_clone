#!/usr/bin/python3
"""Test file for User Class"""
from models.review import Review
import unittest


class TestReview(unittest.TestCase):
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
        Test with default values
        """
        my_review = Review()
        my_review.text = "very good"
        self.assertEqual(my_review.text, "very bad")

if __name__ == '__main__':
    unittest.main()
