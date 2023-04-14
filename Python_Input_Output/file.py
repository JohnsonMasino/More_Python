#!/usr/bin/python3

"""
This module is a file which i will
access from the input/output file
"""

class Man():
    def __init__(self, name):
        self.name = name

    def disp(self):
        print(self.name)
Man("Johnson").disp()
print("\nCode developed by Masino")
