#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.state import State


class TestFile(unittest.TestCase):
    """class to test base model"""

    def test_attributes_type(self):
        self.assertEqual(type(State().name), str)
        self.assertEqual(type(State().id), str)
        self.assertEqual(type(State().updated_at), datetime)
        self.assertEqual(type(State().created_at), datetime)

    def test_class_type(self):
        self.assertEqual(type(State()), State)
