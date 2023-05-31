#!/usr/bin/python3

"""
This file indicates the first name of a name input
"""
class Name:
    """creates the class of the function"""
    def __init__(self, name):
        """initialises the name variable"""
        self.name = name

    def say_name():
        """prints the first name of the input"""
        name = input("Hi! tell us your name please...")
        print(f"The first letter of your name is: {name[0]}")

Name.say_name()
print("\nCode developed by Masino")
