#!/usr/bin/python3

"""
This class describes Inheritance as a core concept of
Object Oriented Programming
"""

class Inheritance:
    def __init__(self, name, age, salary):
        self.name = name
        self.age = age
        self.salary = salary

    def Display(self):
        print(f"#Name: {self.name}\n#Age: {self.age}\n#Salary: KWD{self.salary}")

Inheritance("Masino", 23, 15000).Display()
print("\nCode developed by Masino")
