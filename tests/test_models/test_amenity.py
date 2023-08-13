#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.amenity import Amenity


class TestFile(unittest.TestCase):
    """class to test base model"""

    def test_attributes_type(self):
        """test type of attributes"""
        self.assertEqual(type(Amenity().name), str)
        self.assertEqual(type(Amenity().id), str)
        self.assertEqual(type(Amenity().created_at), datetime)
        self.assertEqual(type(Amenity().updated_at), datetime)

    def test_class_type(self):
        """test class type"""
        self.assertEqual(type(Amenity()), Amenity)
