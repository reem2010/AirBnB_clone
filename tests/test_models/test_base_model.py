#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
import datetime
import time
from models import storage
import uuid
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """class to test base model"""

    def test_Base(self):
        """test base id"""
        my_model = BaseModel()
        self.assertTrue(isinstance(my_model, BaseModel))
        self.assertIn(my_model, storage.all().values())
        key = f"{my_model.__class__.__name__}.{my_model.id}"
        self.assertIn(key, storage.all().keys())
        my_model2 = BaseModel()
        self.assertIn(my_model, storage.all().values())

    def test_arguments(self):
        """test arguments"""
        my_model = BaseModel()
        my_model.my_number = 89
        self.assertEqual(my_model.my_number, 89)
        out = my_model.to_dict().copy()
        self.assertIn('my_number', out.keys())
        model = BaseModel(**out)
        self.assertFalse(my_model is model)
        self.assertEqual(my_model.id, model.id)
        self.assertEqual(my_model.created_at, model.created_at)
        self.assertEqual(my_model.updated_at, model.updated_at)
        model.save()

    def test_id(self):
        """test id"""
        my_model = BaseModel()
        self.assertEqual(type(my_model), BaseModel)
        self.assertEqual(type(my_model.id), str)
        my_model2 = BaseModel()
        self.assertNotEqual(my_model.id, my_model2.id)

    def test_uuid(self):
        """test uuid type"""
        my_model = BaseModel()
        try:
            uuid_4 = uuid.UUID(my_model.id).version
        except ValueError:
            uuid_4 = 0
        self.assertTrue(uuid_4 == 4)

    def test_str(self):
        """test function string"""
        my_model = BaseModel()
        out = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(my_model.__str__(), out)

    def test_creation_date(self):
        """test creation data"""
        my_model_1 = BaseModel()
        my_model_2 = BaseModel()
        self.assertLess(my_model_1.created_at, my_model_2.created_at)
        self.assertLess(my_model_1.updated_at, my_model_2.updated_at)

    def test_time(self):
        """test the time"""
        my_model = BaseModel()
        model_up = my_model.updated_at
        my_model.save()
        self.assertLess(model_up, my_model.updated_at)
        self.assertLess(my_model.created_at, my_model.updated_at)
        self.assertEqual(type(my_model.created_at), datetime.datetime)
        self.assertEqual(type(my_model.updated_at), datetime.datetime)
        my_model_json = my_model.to_dict()
        create = (my_model.created_at).isoformat()
        update = (my_model.updated_at).isoformat()
        self.assertEqual(my_model_json['created_at'], create)
        self.assertEqual(my_model_json['updated_at'], update)

    def test_todic(self):
        """test to dic function"""
        my_model = BaseModel()
        my_model.name = "MODEL"
        my_model.num = 19
        my_model_json = my_model.to_dict()
        self.assertIn('__class__', my_model_json)
        for key in my_model.__dict__:
            self.assertIn(key, my_model_json)
        self.assertEqual(type(my_model_json), dict)
