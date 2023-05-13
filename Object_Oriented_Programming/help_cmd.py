#!/usr/bin/python3

"""
This class adds a help function to a 'do_greet' function
"""
import cmd
import turtle
#import sys

class Hello_Person(cmd.Cmd):
    """Simply states the class of our project"""

    intro = 'Welcome to the Masino console editor.\nEnter help or ? to list available subpackages'
    prompt = '(Masino_developed/turtle) '
    file = None

    def do_greet(self, person):
        'This subpackage prints a greeting message and adds the name of the added argument'
        if person:
            print(f"Hi {person}!\nHow is it going with you?")
        else:
            print("Hi, What's up?")

    def help_greet(self):
        'This subpackage prints the help to the greet function'
        print('\n'.join([ 'greet [person]',
                           'Greet the named person',
                           ]))

    def do_EOF(self, line):
        'This subpackage terminates the working terminal'
        return True

if __name__ == "__main__":
    Hello_Person().cmdloop()
