#!/usr/bin/python3
"""file storage module"""
import json

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
        """sets in __objects the obj"""
        key = f"{obj.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        out = json.dumps(self.__objects)
        with open(self.__file_path, "w") as file:
            file.write(out)

    def reload(self):
        """deserializes the JSON file to __objects"""
        with open(self.__file_path, "r") as file:
            self.__objects = json.loads(file.read())

