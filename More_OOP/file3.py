#!/usr/bin/python3

import cmd
import turtle
from datetime import datetime as dt

class Turtle(cmd.Cmd):
    """Defines the class of the turtle console"""
    intro = 'Welcome to Masino turtle console...\nUse "?" or  "help" to explore available actions'
    prompt = '(Turtle) '
    file = None

    def do_EOF(self, line):
        'Quits the turtle console'
        print("Bye...\nThank you for using cmd console created by Masino")
        return True

    def do_say_name(self, name):
        'Prints the name entered or nothing if no name is entered'
        if name:
            print(f"Hi {name}\nWelcome here")
        else:
            print("Welcome here...")

    def do_say_date(self, line):
        'prints the date of today'
        print(f"Today is: {dt.now()}")

if __name__ == "__main__":
    Turtle().cmdloop()
print("\nCode developed by Masino")
