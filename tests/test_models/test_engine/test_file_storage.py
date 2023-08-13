#!/usr/bin/python3
"""test module for FileStorage"""
import unittest
import datetime
import time
import uuid
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage
from models.engine.file_storage import FileStorage


class TestFile(unittest.TestCase):
    """class to test base model"""

    def test_class_type(self):
        """method check type"""
        self.assertEqual(type(storage), FileStorage)

    def test_Base(self):
        """test storage in dictionary"""
        my_model = BaseModel()
        self.assertIn(my_model, storage.all().values())
        my_model2 = BaseModel()
        self.assertIn(my_model2, storage.all().values())
        self.assertEqual(type(storage.all()), dict)

    def test_className(self):
        """test class name and id"""
        my_model = [BaseModel(), User(), State(), City(), Amenity(), Place()]
        my_model.append(Review())
        for i in my_model:
            key = f"{i.__class__.__name__}.{i.id}"
            self.assertIn(key, storage.all().keys())
