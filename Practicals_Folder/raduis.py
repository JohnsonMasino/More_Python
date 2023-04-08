#!/usr/bin/python3

"""
This function returns the volume of a sphere.
"""
import math

def vol_of_sphere(radius):
    volume = (4/3) * math.pi * (radius ** 3)
    return volume
print("The vlome of shpere of radius 4 is: ", round(vol_of_sphere(4), 2))
print("\nCode developed by Masino")
