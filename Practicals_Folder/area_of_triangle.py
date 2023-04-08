#!/usr/bin/python3

"""
This function returns the area of a triangle
"""

def area_of_triangle():
    base = int(input("Please enter the base of the triangle: "))
    height = int(input("Enter the height here: "))
    area = (1/2) * base * height
    return area
print("The area of the triangle with these info is: ", area_of_triangle())
print("\nCode developed by Masino")
