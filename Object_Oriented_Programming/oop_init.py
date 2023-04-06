#!/usr/bin/python3

"""
This program defines the __init__ object of a class
"""

class Masino:
    def __init__(self, name):
        self.name = name

    def greetings(self):
        print("Hello everyone, I am ", self.name)

Masino("Obinna").greetings()
print("\nCode developed by Masino")
