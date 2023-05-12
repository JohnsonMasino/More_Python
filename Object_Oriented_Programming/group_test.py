#!/usr/bin/python3

"""
This is an example of the turtle console using the cmd module
"""
import cmd
import sys
import turtle

class Turtle_cmd(cmd.Cmd):
    """defining the the class of the console"""
    intro = "Welcome to the three buddies console. Please enter help or ? to view available subpackages"
    prompt = '(turtle) '
    file = None
    def do_left(self, arg):
        'This subpackage turns the console anticlockwise to the specified amount'
        #(*parse(arg))

    def do_say_name(self, arg):
        'This subpackage prints the entered input. example is say_name Masino'
        if arg:
            print(f"Hi! {arg}, How is it going with you?")

        else:
            print("Hi")


    def do_EOF(self, arg):
        'This subpackage terminates the turtle console. Example is EOF'
        return True

if __name__ == "__main__":
    Turtle_cmd().cmdloop()

print("\nCode developed by The Three buddies")
