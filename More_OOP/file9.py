#!/usr/bin/python3

import cmd

class Turtle_Console(cmd.Cmd):
    """defines the class of the module"""
    #import turtle
    #import sys

    intro = 'Welcomr to Masino commnad line console\nEnter "help" or "?" to quick start'
    prompt = '(My_Console) '
    file = None

    def do_EOF(self, line):
        'Terminates the console'
        print("Bye!\nThanks for using our console...")
        return True

    def do_say_name(seld, name):
        'Prints a message if no name is entered and prints the name if there is'
        if (name):
            print(f"Hi...!\nWelcome here {name}")
        else:
            print("Hi...!\nWelsome here")

    def do_forward(self, line):
        'moves the toggle forward by the specified degrees'
        return True

    def do_backward(self, line):
        'moves teh toggle backward by the specified degrees'
        return True

    def do_age(self, age):
        'enter your birth year and this module prints your current age from the current year'
        from datetime import datetime as dt

        try:
            today = dt.now()
            ans = today.year
            new_ans = ans - int(age)
            print(f"Your current age is: {new_ans}.")
        except ValueError as e:
            print(e)

if __name__ == "__main__":
    Turtle_Console().cmdloop()
print("\nCode developed by Masino")
