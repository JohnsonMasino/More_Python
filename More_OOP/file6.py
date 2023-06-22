#!/usr/bin/python3

def FizzBuzz():
    """defines the function of the FizzBuzz"""
    num = int(input("Enter a number limit greater than 15 for printing: "))
    for i in range(1, (num + 1)):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)

if __name__ == "__main__":
    FizzBuzz()
print("\nCode developed by Masino")
