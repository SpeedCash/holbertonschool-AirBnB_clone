

User
#!/usr/bin/python3
"""Module containing the BaseModel class"""

from datetime import datetime
import uuid


class BaseModel:
    """
    Base class for all models
    """

    def __init__(self):
        """Initialize a new BaseModel object"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now().isoformat()
        self.updated_at = datetime.now().isoformat()

    def save(self):
        """Update the update datetime (updated_at)"""
        return self.updated_at

    def to_dict(self):
<<<<<<< Updated upstream
        """Convert the object into a dictionary"""
        obj_class = self.__dict__
        obj_class["__class__"] = str(self.__class__.__name__)

        return obj_class

    def __str__(self):
        """Return a string representation of the object"""
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__)
=======
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = self.__class__.__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy


if __name__ == "__main__":
    from models.base_model import BaseModel

    my_model = BaseModel()
    my_model.name = "My_First_Model"
    my_model.my_number = 89
    print(my_model.id)
    print(my_model)
    print(type(my_model.created_at))
    print("--")
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(
            key, type(my_model_json[key]), my_model_json[key]
        ))

    print("--")
    my_new_model = BaseModel(**my_model_json)
    print(my_new_model.id)
    print(my_new_model)
    print(type(my_new_model.created_at))

    print("--")
    print(my_model is my_new_model)
    
>>>>>>> Stashed changes
