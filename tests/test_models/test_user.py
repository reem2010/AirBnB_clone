#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.user import User


class TestFile(unittest.TestCase):
    """class to test base model"""

    def test_attributes_type(self):
        self.assertEqual(type(User().email), str)
        self.assertEqual(type(User().password), str)
        self.assertEqual(type(User().first_name), str)
        self.assertEqual(type(User().last_name), str)
        self.assertEqual(type(User().id), str)
        self.assertEqual(type(User().created_at), datetime)
        self.assertEqual(type(User().updated_at), datetime)

    def test_class_type(self):
        self.assertEqual(type(User()), User)
