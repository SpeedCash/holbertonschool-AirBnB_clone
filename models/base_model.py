#!/usr/bin/python3
"""Module containing the BaseModel class"""

from datetime import datetime
from uuid import uuid4


class BaseModel:
    """Base class for all models"""

    def __init__(self):
        """Initialize a new BaseModel object"""
        self.id = str(uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Update the update date (updated_at)"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """Convert the object into a dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = datetime.now().isoformat()
        obj_dict["updated_at"] = datetime.now().isoformat()
        return obj_dict

    def __str__(self):
        """Return a string representation of the object"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
