#!/usr/bin/python3

"""
This uses fseek to manipulate an object's position in an opened file
"""

def Open():
    with open("file.py", "rb+") as s:
        s.write(b"ABCDEF123456")
        print(s.readlines())
        s.seek(3)
        print(s.read(1))
        print(s.readline())
        s.close()
        print("File Closed: ", s.closed)
Open()
print("\nCode developed by Masino")
