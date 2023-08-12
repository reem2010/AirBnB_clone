#!/usr/bin/python3
"""test module for BaseModel"""
import unittest
import datetime
import uuid
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """class to test base model"""

    def test_Base(self):
        """test base id"""
        my_model = BaseModel()
        self.assertEqual(type(my_model), BaseModel)
        self.assertEqual(type(my_model.id), str)
        my_model2 = BaseModel()
        self.assertNotEqual(my_model.id, my_model2.id)

    def test_uuid(self):
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
        my_model_1 = BaseModel()
        my_model_2 = BaseModel()
        self.assertLess(my_model_1.created_at, my_model_2.created_at)
        self.assertLess(my_model_1.updated_at, my_model_2.updated_at)

    def test_time(self):
        """test the time"""
        my_model = BaseModel()
        model_up = my_model.updated_at
        my_model.save()
        self.asserLess(model_up, my_model.updated_at)
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
        my_model_json = my_model.to_dict()
        self.assertTrue('__class__' in my_model_json)


if __name__ == '__main__':
    unittest.main()
