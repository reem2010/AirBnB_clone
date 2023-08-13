#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
from datetime import datetime
from models.engine.file_storage import FileStorage
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class TestFile(unittest.TestCase):
    """class to test base model"""

    def test_file(self):
        file1 = FileStorage()
        self.assertEqual(type(file1.all()), dict)

    def test_attributes_type(self):
        self.assertEqual(type(State().name), str)
        self.assertEqual(type(State().id), str)
        self.assertEqual(type(State().updated_at), datetime)
        self.assertEqual(type(State().created_at), datetime)
        self.assertEqual(type(City().state_id), str)
        self.assertEqual(type(City().name), str)
        self.assertEqual(type(City().id), str)
        self.assertEqual(type(City().created_at), datetime)
        self.assertEqual(type(City().updated_at), datetime)
        self.assertEqual(type(Amenity().name), str)
        self.assertEqual(type(Amenity().id), str)
        self.assertEqual(type(Amenity().created_at), datetime)
        self.assertEqual(type(Amenity().updated_at), datetime)
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
        self.assertEqual(type(Place().id), list)
        self.assertEqual(type(Place().created_at), datetime)
        self.assertEqual(type(Place().updated_at), datetime)
        self.assertEqual(type(Review().place_id), str)
        self.assertEqual(type(Review().user_id), str)
        self.assertEqual(type(Review().text), str)
        self.assertEqual(type(Review().id), str)
        self.assertEqual(type(Review().created_at), datetime)
        self.assertEqual(type(Review().updated_at), str)

    def test_class_type(self):
        self.assertEqual(type(State()), State)
        self.assertEqual(type(City()), City)
        self.assertEqual(type(Amenity()), Amenity)
        self.assertEqual(type(Place()), Place)
        self.assertEqual(type(Review()), Review)

    def 
