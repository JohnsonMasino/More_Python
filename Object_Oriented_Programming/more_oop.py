#!/usr/bin/python3

"""
This programe explains Inheritance as a
concept of Object Oriented Programming
"""

class First(object):
    def __init__(self, name, age):
        """initialising the variables"""
        self.name = name
        self.age = age

    def disp(self):
        print(self.name, self.age)

    def answer(self):
        print("True")

class Second(First):

    def answer_2(self):
        print("False")
#    print("Showing from second class")

print("Accessing this line from First class:")
First("Obinna", 23).disp()
First("", "").answer()
print("\nAccessing this line from class Second:")
Second("Chineche", 19).disp()
Second("", "").answer_2()
print("\nCode developed by Masino")
