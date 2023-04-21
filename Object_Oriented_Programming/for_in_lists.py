#!/usr/bin/python3

def Lists0():
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        new = number ** 2
        print(f"{number}^2 = {new}")

def Lists1():
    print()
    fruits = ["Mango", "Apple", "Cashew", "Guava", "Udara"]
    for fruit in fruits:
        print(f"I love {fruit}s")

def Lists3():
    print()
    persons = {"Name": "Johnson Masino", "Occupation": "Software Engineering/Medical Lab Sci", "Weight": "68kgs", "Complexion": "Fairly Fair", "Hobby": "Fishing"}
    for value, answer in persons.items():
        print(f"{value}: {answer}")
        
Lists0()
Lists1()
Lists3()
print("\nCode developed by Masino")
