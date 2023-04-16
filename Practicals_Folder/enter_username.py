#!/usr/bin/python3
"""
This program forces a user to enter a username
"""
#container = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '.']

def UserName():
    container = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '@', '.']

    name = input('Enter your username here: ')
    for letter in container:
        try:
            print(f"{name} is noted Thanks!")
        except TypeError:
            print("Typeerror exists here")
        except Exception as masino:
            print(masino)
        else:
            print("Success...!")
        finally:
            print("End of program")
        break
#print(f"{name} is noted")        
UserName()
print("\nCode developed by Masino")
