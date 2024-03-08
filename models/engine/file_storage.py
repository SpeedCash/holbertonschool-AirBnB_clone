#!/usr/bin/python3

import json
from models.base_model import BaseModel
# Assurez-vous d'importer toutes les autres classes
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class FileStorage:
    __file_path = 'file.json'
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
        return FileStorage.__objects

    def new(self, obj):
        key = f'{obj.__class__.__name__}.{obj.id}'
        self.__objects[key] = obj

    def save(self):
        obj_dict = {obj_id: obj.to_dict()
                    for obj_id, obj in self.__objects.items()}

        """Sets in '__objects' the obj with key <obj class name>.id"""
        if obj:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file (path: '__file_path')"""
        obj_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w') as f:
            json.dump(obj_dict, f)

    def reload(self):
        try:
            with open(self.__file_path, 'r') as f:
                obj_dict = json.load(f)
            for obj_id, obj_data in obj_dict.items():
                cls_name = obj_data['__class__']
                cls = eval(cls_name)  # Assurez-vous que
                toutes les classes sont importées
                self.__objects[obj_id] = cls(**obj_data)

            for key, obj_data in obj_dict.items():
                class_name, obj_id = key.split('.')
                cls = None
                bases = (BaseModel,)
                namespace = obj_data
                cls = type(class_name, bases, namespace)
                self.__objects[key] = cls(**obj_data)
                
        except FileNotFoundError:
            pass
