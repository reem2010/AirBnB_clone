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
        self.created_at =
        self.updated_at =
    
    def save(self):

    def to_dict(self):
        """Create dictionary of object"""

        update_dict = self.__dict__
        update_dict['__class__'] = cls.__name__
        return update_dict
    
    def __str__(self):
        return f"[{cls.__name__}] ({self.id}) {self.__dict__}"
