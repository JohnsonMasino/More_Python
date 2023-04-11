#!/usr/bin/python3

"""
This Object Oriented Programming explians
Multiple Level Programming
"""

class Father(object):
    def __init__(self, name):
        self.name = name

class Son(Father):
    def __init__(self, name, age):
        Father.__init__(self, name)
        self.age = age

class GrandSon(Son):
    def __init__(self, name, age, salary):
        Son.__init__(self, name, age)
        self.salary = salary

    def display(self):
        print(f"Name:   {self.name}\nAge:    {self.age}\nSalary: {self.salary}")
        print("Calling from the last instance of the last class")

GrandSon("Masino", 23, 15000).display()
print("\nCode developed by Masino")
