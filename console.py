#!/usr/bin/python3
"""The main console program
"""

import cmd
import re
import sys
import importlib
from models import *


class HBNBCommand(cmd.Cmd):
    intro = "Welcome to the AirBnB. Type 'help' to list available commands."
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command and exit the program
        """
        return True

    def do_EOF(self, args):
        """Handle the End-of-File condition"""
        return True

    def emptyline(self):
        """Override emptyline to display only the prompt"""
        pass

    def do_create(self, args):
        """Create a new instance of BaseModel, save it, and print the id"""
        if not args:
            print("** class name missing **")
            return

        class_name = args.split()[0]
        classes = storage.modules.keys()
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        module_name = storage.modules[class_name]
        module = importlib.import_module('.' + module_name, package='models')
        class_ = getattr(module, class_name)

        obj = class_()
        obj.save()
        print(obj.id)

    def do_show(self, args):
        """Print the string representation of an instance"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        classes = storage.modules.keys()
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_id = args_list[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        print(objects[key])

    def do_destroy(self, args):
        """Delete an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        classes = storage.modules.keys()
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_id = args_list[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        del objects[key]
        storage.save()

    def do_all(self, args):
        """Print all string representations of instances"""
        objects = storage.all()

        if not args:
            print([str(obj) for obj in objects.values()])
            return

        args_list = args.split('.')
        class_name = args_list[0]
        classes = storage.modules.keys()
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        class_objects = [
            str(obj) for obj in objects.values()
            if type(obj).__name__ == class_name
        ]
        print(class_objects)

    def do_update(self, args):
        """Update an instance based on the class name and id"""
        if not args:
            print("** class name missing **")
            return

        args_list = args.split()
        class_name = args_list[0]
        classes = storage.modules.keys()
        if class_name not in classes:
            print("** class doesn't exist **")
            return

        if len(args_list) < 2:
            print("** instance id missing **")
            return

        obj_id = args_list[1]
        key = "{}.{}".format(class_name, obj_id)
        objects = storage.all()
        if key not in objects:
            print("** no instance found **")
            return

        if len(args_list) < 3:
            print("** attribute name missing **")
            return

        if len(args_list) < 4:
            print("** value missing **")
            return

        attribute_name = args_list[2]
        attribute_value = args_list[3]
        obj = objects[key]
        setattr(obj, attribute_name, attribute_value)
        obj.save()

    def do_count(self, class_name):
        """Print the number of instances of the specified class"""
        objects = storage.all()

        if class_name not in storage.modules.keys():
            print("** class doesn't exist **")
            return

        class_count = sum(
            1 for obj in objects.values()
            if type(obj).__name__ == class_name
        )
        print(class_count)

    def default(self, line):
        """Handle arbitrary commands"""
        token = line.split(".")
        if line.endswith('.all()'):
            class_name = line[:-6]
            self.do_all(class_name)
        elif line.endswith('.count()'):
            class_name = line[:-8]
            self.do_count(class_name)
        elif token[1].startswith('show(') and token[1].endswith(')'):
            cmd_args = token[1][:-1]
            args_list = re.split(r'[()]', cmd_args)
            if len(args_list) != 2:
                print("Invalid arguments. Usage: <class name>.show(<id>)")
            else:
                class_name = token[0].strip()
                obj_id = args_list[1].strip()
                self.do_show(f"{class_name} {obj_id}")
        else:
            print("Command not recognized.")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
