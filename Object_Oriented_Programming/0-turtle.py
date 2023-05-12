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
        if arg:
            print(f"Hi there {arg}!\nHow is it going with you?")
        else:
            print("Heloo")

    def do_EOF(self, arg):
            return True

if __name__ == "__main__":
    TurtleConsole().cmdloop()
print("\nConsol developed by Masino")
