#!/usr/bin/python3

"""
This Module Opens and Closes the file 'file.py'
It also does some manipulations to the file
"""
def Open1():
    with open("file.py", encoding="utf-8") as a:
        read = a.read()
        read1 = a.read()
        print(read)
        print("You will see a blank line because it is the end of the line")
        print(read1)
        a.close()
        print(a.closed)
Open1()        
