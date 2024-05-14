#!/usr/bin/env python3
"""Defines the HBnB console."""
import cmd
import sys
import json
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.place import Place
from models.amenity import Amenity
from models.review import Review

def parse(arg):
    curly_braces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curly_braces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            retl = [i.strip(",") for i in lexer]
            retl.append(brackets.group())
            return retl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        retl = [i.strip(",") for i in lexer]
        retl.append(curly_braces.group())
        return retl


class HBNBCommand(cmd.Cmd):
    """Defines the HolbertonBnB command interpreter.

    Attributes:
        prompt (str): The command prompt
    """


    prompt = '(hbnb) '

    __classes = {
            "BaseModel",
            "User",
            "State",
            "City",
            "Place",
            "Amenity",
            "Review"
            }

    match = re.search(r"\.", arg)
    if match is not None:
        argl = [arg[:match.span()[0]], arg[match.span()[1]:]]
        match = re.search(r"\((.*?)\)", argl[1])
        if match is not None:
            command = [argl[1][:match.span()[0]], match.group()[1:-1]]
            if command[0] in argdict.keys():
                call = "{} {}".format(argl[0], command[1])
                return argdict[command[0]](call)
    print("*** Unknown syntax: {}".format(arg))
    return False


    def do_quit(self, arg):
        """Quit command to exit the program"""
        sys.exit(0)

    def do_EOF(self, arg):
        """Exit the program"""
        print()
        sys.exit(0)

    def emptyline(self):
        """Do nothing when an empty line is entered"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel or User"""
        if not arg:
            print("** class name missing **")
            return

        class_name = arg.split()[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        new_instance = globals()[class_name]()
        new_instance.save()
        print(new_instance.id)

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        print(storage.all()[key])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        del storage.all()[key]
        storage.save()

    def do_all(self, arg):
        """Prints all string representation of all instances"""
        objects = storage.all()
        if not arg:
            print([str(obj) for obj in objects.values()])
            return

        class_name = arg.split()[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        print([str(obj) for key, obj in objects.items() if key.startswith(class_name)])

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        class_name = args[0]
        if class_name not in globals():
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_id = args[1]
        key = f"{class_name}.{obj_id}"
        if key not in storage.all():
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        attr_name = args[2]
        if hasattr(storage.all()[key], attr_name):
            attr_type = type(getattr(storage.all()[key], attr_name))
            try:
                attr_value = attr_type(args[3])
            except ValueError:
                print("** value missing **")
                return
            setattr(storage.all()[key], attr_name, attr_value)
            storage.save()
        else:
            print("** attribute doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
