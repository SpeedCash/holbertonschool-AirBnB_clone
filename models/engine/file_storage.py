#!/usr/bin/python3
"""Module for handling file storage"""

from models.base_model import BaseModel
import json


class FileStorage:
    """
    Class for serializing instances to a JSON file
    and deserializing JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file (path: '__file_path')"""
        odict = FileStorage.__objects
        objdict = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, 'w') as f:
            json.dump(objdict, f)

    def reload(self):
        """Deserializes the JSON file to '__objects'"""
        try:
            with open(FileStorage.__file_path, 'r') as f:
                objdict = json.load(f)
                for obj_data in objdict.values():
                    cls_name = obj_data['__class__']
                    del obj_data['__class__']
                    cls = globals()[
                        cls_name] if cls_name in globals() else None
                    if cls:
                        self.new(cls(**obj_data))
        except FileNotFoundError:
            pass
