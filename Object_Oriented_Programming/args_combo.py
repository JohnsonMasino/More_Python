#!/usr/bin/python3

"""
This program accepts arguments and key value combinations
"""

class AllFunctions:
    def Combo(self, *args, **kwargs):
        count = 0
        countt = 0
        print("From normal argument:", self)
        for arg in args:
            count += 1
            print(f"From Argument Combination {count}:", arg)
        for key, value in kwargs.items():
            countt += 1
            print(f"From Key and Value {countt}: ", key + ":", value)
AllFunctions.Combo("Self", "Orange", "Lemon", "Paw-Paw", Name="Masino", Eye_Color="Dark-Brown", Complexion="Fairly-Fair")
print("\nCode developed by Masino")
