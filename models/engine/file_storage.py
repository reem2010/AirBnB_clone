#!/usr/bin/python3
"""file storage module"""
import json
import os
import models

class FileStorage:
    """
    class FileStorage that serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}
    
    def all(self):
        """returns the dictionary"""
        print(f"{FileStorage.__objects}all")
        return (FileStorage.__objects)

    def new(self, obj):
        """sets in __objects the obj"""
        key = f"BaseModel.{obj.id}"
        FileStorage.__objects[key] = obj
        print(f"{FileStorage.__objects}new \n {obj}")

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = FileStorage.__objects
        for key, value in new_dict.items():
            new_dict[key] = value.to_dict()
        out = json.dumps(new_dict)
        print(f"{FileStorage.__objects}save")
        with open(FileStorage.__file_path, "w") as file:
            file.write(out)

    def reload(self):
        """deserializes the JSON file to __objects"""
        print(f"{FileStorage.__objects}reload")
        if os.path.exists(FileStorage.__file_path): 
            with open(FileStorage.__file_path, 'r') as file:
                readFile = json.loads(file.read())
            FileStorage.__objects = {key: (readFile[key['__class__']])(**readFile[key]) for key in readFile.keys()}
