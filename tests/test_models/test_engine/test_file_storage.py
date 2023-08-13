#!/usr/bin/python3
"""test module for FileStorage"""
import unittest
import datetime
import time
import uuid
from models.base_model import BaseModel
from models import storage
from models.engine import FileStorage


class TestFile(unittest.TestCase):
    """class to test base model"""

    def test_class_type(self):
        self.assertEqual(type(storage), FileStorage)

    def test_Base(self):
        """test storage in dictionary"""
        my_model = BaseModel()
        self.assertIn(my_model, storage.all().values())
        self.assertEqual(type(storage.all), dict)
        key = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertIn(key, storage.all().keys())
        my_model2 = BaseModel()
        self.assertIn(my_model, storage.all().values())
