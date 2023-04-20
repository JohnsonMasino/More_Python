#!/usr/bin/python3

#This program imports the 'math' package

def Maths():
    import math as mt

    print("First FXN:")
    print(mt.log(10))
    print(mt.cos(3.147/4))
    print(mt.log(1024, 2))

def Random():
    import random as rd

    print("\nSecond FXN:")
    print(rd.randrange(9))
    print(rd.choice([6, 5, 3, 8]))
    print(rd.choice(["Masino", "Chineche", "Ebube", "Chisom", "Obumneme"]))

def Stat():
    import statistics as st

    print("\nThird FXN:")
    names = ["Masino", "Chineche", "Ebube", "Chisom", "Obumneme"]
    print(st.median(names))

    nums = [4, 6, 9, 0, 1, 5, 5, 3]
    print(st.mean(nums))
    print(st.median(nums))
    print(st.variance(nums))

Maths()
Random()
Stat()
print("\nCode developed by Masino")
