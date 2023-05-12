#!/usr/bin/python3

"""
This class is a simple example of the turtle console
"""
import cmd
import sys
import turtle

class Simple_Turtle_Console(cmd.Cmd):
    """States the class of the turtle module
    and defines some variables"""

    intro = 'Welcome to Masino turtle console.    Type in help or ? to display some built-in functions'
    prompt = '(turtle) '
    file = None


    #____________________________________These are some Basic Turtle Commands______________________________________
    def do_forward(self, arg):
        'This subpackge moves the turtle console forward to the specified number of times. Example is "FORWARD 60"'
        #forward(*parse(arg))

    def do_home(self, arg):
        'This subpackage takes the turtle console to the home page. Example is "HOME"'
        #home(*parse(arg))

    def do_right(self, arg):
        'This subpackage turns the turtle console clockwise to a specified time. Example is "RIGHT 55"'
        #right(*parse(arg))

    def do_goto(self, arg):
        'This subpackage takes the turtle console to the specified path'
        #goto(*parse(arg))

    def do_left(self, arg):
        'This subpackage turns the turtle console anti-clockwise to a specified time. Example is "LEFT 75"'
        #left(*parse(arg))


    #______________________________________These are some playback/recording_____________________________________
    def do_save(self, arg):
        'This subpackage saves data in a specified file name. Example is "RECORD my_note.cmd"'
        save(*parse(arg))

#Simple_Turtle_Console()
if __name__ == "__main__":
    Simple_Turtle_Console().cmdloop()

print("\nTurtle Console develoepd by Masino")
