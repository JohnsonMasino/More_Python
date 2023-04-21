#!/usr/bin/python3

def Lists0():
    i = 0
    numbers = [1, 2, 3, 4, 5]
    for number in numbers:
        i += 1
        new = number ** 2
        print(f"{i}: {number}^2 = {new}")

def Lists1():
    print()
    count = 0
    fruits = ["Mango", "Apple", "Cashew", "Guava", "Udara"]
    for fruit in fruits:
        count += 1
        print(f"{count}: I love {fruit}s")

def Lists3():
    print()
    m = 0
    persons = {"Name": "Johnson Masino", "Occupation": "Software Engineering/Medical Lab Sci", "Weight": "68kgs", "Complexion": "Fairly Fair", "Hobby": "Fishing"}
    for value, answer in persons.items():
        m += 1
        print(f"{m}: {value}: {answer}")
        
Lists0()
Lists1()
Lists3()
print("\nCode developed by Masino")
