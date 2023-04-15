#!/usr/bin/python3
"""
This program imports the "os" module to work with
"""
import os
def Import():
    with open("file.py", "r+", encoding="utf-8")as m:
        print(m.read())
        os.rename("file.py", "newfile.py")
        m.write("First Line\nSecond Line\nThird Line")
        with open("newfile.py", encoding="utf-8") as m:
            print(m.read())
            m.close()
            print("File Closed: ", m.closed)
Import()
print("\nCode developed by Masino")
