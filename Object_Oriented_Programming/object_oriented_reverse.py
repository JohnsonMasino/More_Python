#!/usr/bin/python3

"""
This class function uses iteration functions to prints variable elements backwards
"""

class Reverse:
    """Initialising iterator for looping a string backwards"""
    def __init__(self, name):
        self.name = name
        self.indexing = len(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.indexing == 0:
            raise StopIteration
        self.indexing = self.indexing - 1
        return self.name[self.indexing]
print("Iterating a sentence backwards as:")
rev = Reverse("ma I sa derob sa uoy erA")
iter(rev)
for letter in rev:
    print(letter, end="")

#Reverse("")
print("\n\nCode developed by Masino")
