#!/usr/bin/python3
import json
import cmd
import sys
import importlib
from models.engine import storage


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
        classes = {type(value).__name__ for value in storage.all().values()}
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
        classes = {type(value).__name__ for value in storage.all().values()}
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
        classes = {type(value).__name__ for value in storage.all().values()}
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
        classes = {type(value).__name__ for value in storage.all().values()}
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
        classes = {type(value).__name__ for value in storage.all().values()}
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


def run_console():
    """
    Run the console: command line
    """
    console = HBNBCommand()

    if not sys.stdin.isatty():
        print(console.prompt + "\n", end='')
        line = sys.stdin.readline().rstrip('\n')
        console.onecmd(line)
        print(console.prompt + "\n", end='')
    else:
        console.cmdloop()


if __name__ == '__main__':
    run_console()
