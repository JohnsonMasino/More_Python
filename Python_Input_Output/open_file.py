#!/usr/bin/python3

"""
This Module opens and close the 'File' class
It tells us if the file is successfully closed after opening
It finally prints the contents of the 'file.py' file
"""
def Openn():
    with open("file.py", "r", encoding="utf-8") as m:
        read = m.read()
    print(m.closed)
    print()
    print(read)
Openn()
print("\nCode developed by Masino")
