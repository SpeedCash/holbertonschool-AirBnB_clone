#!/usr/bin/python3
"""Module for HBNBCommand class."""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """A command interpreter class."""
    prompt = '(hbnb) '

    def __init__(self):
        super().__init__()
        self.classes = {
            "BaseModel": BaseModel,
            "User": User,
            "Place": Place,
            "State": State,
            "City": City,
            "Amenity": Amenity,
            "Review": Review
        }

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program."""
        print()
        return True

    def emptyline(self):
        """An empty line + ENTER shouldn’t execute anything."""
        pass

    def do_create(self, line):
        args = line.split()
        if not args:
            print("** class name missing **")
            return
        class_name = args[0]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        new_instance = self.classes[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **" if not args else "** \
                  instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all(self.classes[class_name])
        obj_key = "{}.{}".format(class_name, instance_id)
        if obj_key in all_objs:
            print(all_objs[obj_key])
        else:
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id."""
        args = arg.split()
        if len(args) < 2:
            print("** class name missing **" if not args else "** \
                  instance id missing **")
            return
        class_name, instance_id = args[0], args[1]
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all(self.classes[class_name])
        obj_key = "{}.{}".format(class_name, instance_id)
        if obj_key in all_objs:
            del all_objs[obj_key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of instances."""
        args = arg.split()
        if args and args[0] not in self.classes:
            print("** class doesn't exist **")
            return
        objs = storage.all(self.classes.get(args[0], None))
        print([str(obj) for obj in objs.values()])

    def do_update(self, arg):
        """Updates an instance based on the class name and\
            id by adding or updating attribute."""
        args = arg.split()
        if len(args) < 4:
            print("** class name missing **" if not args else
                  "** instance id missing **" if len(args) == 1 else
                  "** attribute name missing **" if len(args) == 2 else
                  "** value missing **")
            return
        class_name, instance_id, attribute_name, attribute_value = \
            args[0], args[1], args[2], args[3].strip('"')
        if class_name not in self.classes:
            print("** class doesn't exist **")
            return
        all_objs = storage.all(self.classes[class_name])
        obj_key = "{}.{}".format(class_name, instance_id)
        if obj_key in all_objs:
            setattr(all_objs[obj_key], attribute_name, attribute_value)
            all_objs[obj_key].save()
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
