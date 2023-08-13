#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.review import Review


class TestFile(unittest.TestCase):
    """class to test base model"""

    def test_attributes_type(self):
        self.assertEqual(type(Review().place_id), str)
        self.assertEqual(type(Review().user_id), str)
        self.assertEqual(type(Review().text), str)
        self.assertEqual(type(Review().id), str)
        self.assertEqual(type(Review().created_at), datetime)
        self.assertEqual(type(Review().updated_at), datetime)

    def test_class_type(self):
        self.assertEqual(type(Review()), Review)
