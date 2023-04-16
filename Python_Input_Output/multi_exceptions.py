#!/usr/bin/python3

"""
This program handles multiple exceptions
"""

def File():
    excs = [OSError("error 1"), SystemError('error 2')]
    raise ExceptionGroup('problems discovered', excs)
File()
print("\nCode developed by Masino")
