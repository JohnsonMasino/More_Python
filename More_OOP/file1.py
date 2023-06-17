#!/usr/bin/python3

class Fruits:
    """defines the class Fruits"""
    def __init__(self, fruit_name, fruit_age):
        """initialises the class parameters"""
        self.name = fruit_name
        self.age = fruit_age

    def say_all(name, age):
        """prints the name of the fruit"""
        name1 = f"The name of the first fruit is: {name}"
        age1 = f"The age of the first fruit is: {age}"
        print(name1)
        print(age1)
        print()
        print(name1.__repr__())
        print(age1.__repr__())

if __name__ == "__main__":
    Fruits.say_all("Mango", 5)
print("\nCode developed by Masino")
