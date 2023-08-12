#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
import datetime
from models.engine.file_storage import FileStorage


class TestFile(unittest.TestCase):
    """class to test base model"""

    def test_file(self):
        file1 = FileStorage()
        self.assertEqual(type(file1.all()), dict)
