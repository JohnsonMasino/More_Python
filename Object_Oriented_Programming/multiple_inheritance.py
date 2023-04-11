#!/usr/bin/python3

"""
This class function explains multiple
inheritance in O - O - Programming
"""

class Parent1(object):
    def __init__(self):
        self.name1 = "Masino"
        print("In Parent1")

class Parent2(object):
    def __init__(self):
        self.name2 = "Obinna"
        print("\nIn Parent2")

class Child(Parent1, Parent2):
    def __init__(self):
        Parent1.__init__(self)
        Parent2.__init__(self)
        print("\nBoth called successfully")
        print("In the child class")
        print("In the next intance, Calling...!")

    def display(self):
        print(self.name1, self.name2)

Child().display()
print("\nCode developed by Masino")    
