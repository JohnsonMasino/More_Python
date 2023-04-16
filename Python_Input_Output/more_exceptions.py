#!/usr/bin/python3

"""
This Program Reports multiple exceptions
"""

def Exceptions():
    raise ExceptionGroup("group1", [OSError(1), SystemError(2), ExceptionGroup("group2", [OSError(3), RecursionError(4)])])
try:
    Exceptions()
except* OSError as e:
    print("OSError detected")
except* SystemError as e:
    print("SystemErrors detected")
Exceptions()
print("\nCode developed by Masino")
