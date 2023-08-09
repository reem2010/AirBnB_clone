import unittest
import datetime
from models.base_model import BaseModel
"""test module for BaseModel"""

class TestBase(unittest.TestCase):
    """class to test base model"""

    def test_Base(self):
        my_model = BaseModel()
        self.assertEqual(type(my_model.id), str)
        my_model2 = BaseModel()
        self.assertNotEqual(my_model.id, my_model2.id)

    def test_str(self):
        my_model = BaseModel()
        out = f"[BaseModel] ({my_model.id}) {my_model.__dict__}"
        self.assertEqual(my_model.__str__(), out)

    def test_time(self):
        my_model = BaseModel()
        my_model.save()
        self.assertNotEqual(my_model.created_at, my_model.updated_at)
        self.assertEqual(type(my_model.created_at), datetime.datetime)
        self.assertEqual(type(my_model.updated_at), datetime.datetime)
        my_model_json = my_model.to_dict()

    def test_tidic(self):
        my_model = BaseModel()
        my_model_json = my_model.to_dict()
        self.assertTrue('__class__' in my_model_json)

if __name__ == '__main__':
    unittest.main()
