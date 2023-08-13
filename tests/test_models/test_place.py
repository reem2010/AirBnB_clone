#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.place import Place


class TestFile(unittest.TestCase):
    """class to test base model"""

    def test_attributes_type(self):
        """test attributes type"""
        self.assertEqual(type(Place().city_id), str)
        self.assertEqual(type(Place().user_id), str)
        self.assertEqual(type(Place().name), str)
        self.assertEqual(type(Place().description), str)
        self.assertEqual(type(Place().number_rooms), int)
        self.assertEqual(type(Place().number_bathrooms), int)
        self.assertEqual(type(Place().max_guest), int)
        self.assertEqual(type(Place().price_by_night), int)
        self.assertEqual(type(Place().latitude), float)
        self.assertEqual(type(Place().longitude), float)
        self.assertEqual(type(Place().amenity_ids), list)
        self.assertEqual(type(Place().id), str)
        self.assertEqual(type(Place().created_at), datetime)
        self.assertEqual(type(Place().updated_at), datetime)

    def test_class_type(self):
        """test class type"""
        self.assertEqual(type(Place()), Place)
