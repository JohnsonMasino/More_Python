#!/usr/bin/python3

"""
This program checks for the contents of two folders in my desktop
"""
import Unittest_Files
import Test_Files
import one
import two

def Checking(arg1, arg2):
    if arg1 == arg2:
        print("Same Content")
    else:
        print("Not same content")
Checking(Unittest_Files, Test_Files)
print("\nCode developed by Masino")
