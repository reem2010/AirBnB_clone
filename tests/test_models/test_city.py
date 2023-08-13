#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.city import City


class TestFile(unittest.TestCase):
    """class to test base model"""

    def test_attributes_type(self):
        """test attributes type"""
        self.assertEqual(type(City().state_id), str)
        self.assertEqual(type(City().name), str)
        self.assertEqual(type(City().id), str)
        self.assertEqual(type(City().created_at), datetime)
        self.assertEqual(type(City().updated_at), datetime)

    def test_class_type(self):
        """test class type"""
        self.assertEqual(type(City()), City)
