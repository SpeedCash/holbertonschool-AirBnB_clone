# models/engine/file_storage.py

import json
from models.base_model import BaseModel
# Import other classes


class FileStorage:
    """Serializes instances to a JSON file & deserializes\
        JSON file to instances."""

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary '__objects'"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in '__objects' the obj with key <obj class name>.id"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Serializes '__objects' to the JSON file (path: '__file_path')"""
        with open(self.__file_path, 'w') as f:
            json.dump({k: v.to_dict() for k, v in self.__objects.items()}, f)

    def reload(self):
        """Deserializes the JSON file to '__objects'"""
        try:
            with open(self.__file_path, 'r') as f:
                objects = json.load(f)
            for obj_id, obj_dict in objects.items():
                cls_name = obj_dict['__class__']
                cls = eval(cls_name)
                self.__objects[obj_id] = cls(**obj_dict)
        except FileNotFoundError:
            pass
