#!/usr/bin/python3
"""file storage module"""
import json
import os

class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary"""
        return (self.__objects)

    def new(self, obj):
        print(type(obj))
        """sets in __objects the obj"""
        key = f"BaseModel.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = self.__objects.copy()
        for value, key in new_dict.items():
            print(type(value))
            new_dict[key] = value.to_dict()
        out = json.dumps(self.__objects)
        with open(self.__file_path, "w") as file:
            file.write(out)

    def reload(self):
        """deserializes the JSON file to __objects"""
        if os.path.exists(self.__file_path): 
            with open(self.__file_path, "r") as file:
                self.__objects = json.loads(file.read())

