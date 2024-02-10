#!/usr/bin/python3
import json
import cmd
import sys


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
