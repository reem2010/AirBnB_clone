#!/usr/bin/python3
"""test module for FileStorage"""
import unittest
import datetime
import time
from models.engine.file_storage import FileStorage
import uuid
from models.base_model import BaseModel
from models import storage


class TestFile(unittest.TestCase):
    """class to test base model"""

    def test_file(self):
        """initialize module"""
        file1 = FileStorage()
        self.assertEqual(type(file1.all()), dict)

    def test_Base(self):
        """test storage in dictionary"""
        my_model = BaseModel()
        self.assertIn(my_model, storage.all().values())
        key = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertIn(key, storage.all().keys())
        my_model2 = BaseModel()
        self.assertIn(my_model, storage.all().values())


if __name__ == '__main__':
    unittest.main()
