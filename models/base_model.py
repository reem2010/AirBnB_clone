#!/usr/bin/python3
"""This module for BaseModel"""
import uuid
import datetime
import models


class BaseModel:
    """class BaseModel"""

    def __init__(self, *args, **kwargs):
        """Initiation of new instance"""

        if (kwargs is not None) and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            models.storage.new(self)

    def __str__(self):
        """return string representation"""

        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """update the time"""

        self.updated_at = datetime.datetime.now()
        models.storage.save()

    def to_dict(self):
        """Create dictionary of object"""

        update_dict = (self.__dict__).copy()
        update_dict['__class__'] = self.__class__.__name__
        update_dict['created_at'] = self.created_at.isoformat()
        update_dict['updated_at'] = self.updated_at.isoformat()
        return update_dict
