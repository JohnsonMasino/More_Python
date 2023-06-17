#!/usr/bin/python3

class People:
    """defines the class of the module"""
    def __init__(self, name, age):
        """initialises the parameters of the class"""
        self.name = name
        self.age = age

    def __str__(self):
        """defines the string representation of the class Peoples' parameters"""
        return f"The name of this person is {self.name} and the age is {self.age}"

    """def __repr__(self):
        'defines the representation function of the class People'
        return f'People({self.name}, {self.age})'"""
one = People("Masino", 23)
two = People("Favour", 21)

if __name__ == "__main__":
    print()
    print(str(one))
    print(repr(one))
    print()
    print(str(two))
    print(repr(two))
print("\nCode developed by Masino")
