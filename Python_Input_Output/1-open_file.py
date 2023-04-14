#!/usr/bin/python3

"""
This program The four two lines of the file 'file.py'
"""

def Open():
    with open("file.py", encoding="utf-8") as M:
        print("This prints the first four lines of the imported file:\n", M.readline(), M.readline(), M.readline(), M.readline())
        M.close()
        print("Checking if the file was closed: ", M.closed)
Open()
print("\nCode developed by Masino")
