#!/usr/bin/python3
"""Module containing the BaseModel class"""

from datetime import datetime
from uuid import uuid4
import models


class BaseModel:
    """Base class for all models"""

    def __init__(self, *args, **kwargs):
        """Initialize a new BaseModel object"""
        if kwargs:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at" or key == "updated_at":
                        value = datetime.strptime(
                            value, "%Y-%m-%dT%H:%M:%S.%f")
                    setattr(self, key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """Update the update date (updated_at)"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert the object into a dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        """Return a string representation of the object"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
