#!/usr/bin/python3
"""
This Program uses for loop to print the first six lines
of the file 'file.py'
"""

def Open():
    count = 0
    with open("file.py", encoding="utf-8") as m:
        for line in m:
            count += 1
            if count <= 6:
                print(line, end="")
        m.close()
        print("Checking if the file was closed successfully: ", m.closed)
Open()
print("\nCode developed by Masino")
