#!/usr/bin/python3

"""
This program opens a file and writes to it
"""

def Open():
    with open("file.py", "r+", encoding="utf-8") as m:
        new = m.write("\nThank you\n")
        print(new)
        m.close()
        print("File Closed: ", m.closed)
Open()
print("\nCode developed by Masino")
