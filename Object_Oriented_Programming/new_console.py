#!/usr/bin/python3

"""
This is a console built with python using the cmd module
"""
import cmd
import sys

class Console(cmd.Cmd):
    """class of the console"""
    prompt = '(turtle) '
    intro = 'Welcome to this console.\nUse "help" or "?" to checkout our available commands'

    def do_say_name(self, name):
        'prints the name of the input'
        if name:
            print(f"Hi {name}")
        else:
            print("Hi!\nWelcome here.\nLet us know your name next time if you dont mind")

    def do_EOF(self, line):
        'terminates the console'
        return True

Console().cmdloop()
print("\nCode developed by Masino")
