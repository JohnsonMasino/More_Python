#!/usr/bin/python3

"""
This class uses turtle to run some commands
"""
import cmd
import turtle
import sys

class TurtleConsole(cmd.Cmd):
    """defines the main class"""
    
    def do_greet(self, arg):
        #'This subpackage prints a greeting message'
        #greet(*parse(arg))
        print("Hi there!\nHow is it going with you?")

    def do_EOF(self, arg):
            return True

if __name__ == "__main__":
    TurtleConsole().cmdloop()
print("\nConsole developed by Masino")
