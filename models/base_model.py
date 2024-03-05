#!/usr/bin/python3
"""Module containing the BaseModel class"""

from datetime import datetime
import uuid


class BaseModel:
    """Base class for all models"""

    def __init__(self):
        """Initialize a new BaseModel object"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def save(self):
        """Update the update date (updated_at)"""
        return self.updated_at

    def to_dict(self):
        """Convert the object into a dictionary"""
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        """Return a string representation of the object"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)