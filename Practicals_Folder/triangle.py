#!/usr/bin/python3

"""
This program returns the type os a triangle based on it's sizes
"""

def Triangle_Area():
    side_A = int(input("Enter the heigth of the triangle: "))
    side_B = int(input("Enter the lenght of the first side: "))
    side_C = int(input("Enter the lenght of the second side: "))
    if side_A == side_B and side_A == side_C and side_B == side_C:
        print("Thsi triangle is an equilateral triangle")
    elif side_A == side_B or side_B == side_C or side_A == side_C:
        print("This is an isoceles triangle")
    else:
        print("This is a scalen triangle")
Triangle_Area()        
print("\nCode developed by Masino")
