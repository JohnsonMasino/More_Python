#!/usr/bin/python3

"""
This file builds another console for the air bnb project as
requested by the als Africa program
"""
import cmd
import sys
import turtle

class MoreConsole(cmd.Cmd):
    """Stipulates the class of the console"""

    intro = 'Welcome to Masinos console of the air bnb project'
    prompt = '(Masino Console) '
    file = None

    def do_say_name(self, arg):
        'prints the name of the entrered argument Example is: say_name Johnson'
        if arg:
            print(f"Hello {arg}, What is popping ?")
        else:
            print("Hi!\nYou can provide your name")

    def do_quit(self, line):
        'This subpackage exits the console'
        return True

    def do_right(self, time):
        'This subpackage moves the console clockwise to the specified amount. Example is right 499'

    def do_EOF(self):
        'This subpackage termiates the console totally'
        return True

if __name__ == "__main__":
    MoreConsole().cmdloop()
print("\nCode developed by Masino")
