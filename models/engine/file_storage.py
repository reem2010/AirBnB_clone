#!/usr/bin/python3
"""file storage module"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary"""
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = FileStorage.__objects.copy()
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        out = json.dumps(new_dict)
        with open(FileStorage.__file_path, "w") as file:
            file.write(out)

    def reload(self):
        """deserializes the JSON file to __objects"""
        fun = {
                'BaseModel': BaseModel,
                'User': User,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
                }
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, 'r') as file:
                readFile = json.loads(file.read())
                for key, value in readFile.items():
                    self.new(fun[key.split('.')[0]](**value))
