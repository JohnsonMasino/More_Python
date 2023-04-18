#!/usr/bin/python3

"""
This function prints the range of some values
"""

def Range():
    print(list(range(0, 51, 5)))

    persons = ["Johnson", "Kingsley", "Malachy", "Anibuego", "Dikeoma", "Ukeagu"]
    for name in range(len(persons)):
        print(f"{name}: {persons[name]}")
    
    print()
    print("Next List coming up...")
    print()
    count = 0
    names = ["Man", "John", "Mark", "Chow", "Ping", "Jackie", "Ox"]
    for name in names:
        count += 1
        print(count, name)
Range()
print("\nCode developed by Masino")
