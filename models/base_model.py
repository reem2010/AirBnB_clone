#!/usr/bin/python3
"""This module for BaseModel"""
import uuid
import datetime


class BaseModel:
    """
     class BaseModel that defines all
     common attributes/methods for other classes
    """

    def __init__(self):
        """Initiation of new instance"""

        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def save(self):
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Create dictionary of object"""

        update_dict = self.__dict__
        update_dict['__class__'] = "BaseModel"
        update_dict['created_at'] = self.created_at.isoformat()
        update_dict['updated_at'] = self.updated_at.isoformat()
        return update_dict

    def __str__(self):
        return f"[BaseModel] ({self.id}) {self.__dict__}"
