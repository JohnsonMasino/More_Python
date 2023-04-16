#!/usr/bin/python3

"""
This function divides a first number by the second number
"""
num1 = int(input("Enter first number here: "))
num2 = int(input("Enter second number here: "))

def Div(a, b):
    """num1 = int(input("Enter first number here: "))
    num2 = int(input("Enter second number here: "))"""
    got = num1/num2
    try:
        print("Devision is: ", round(a/b, 2))
        return a/b
    except ZeroDivisionError:
        print("Can not be divided by Zero")
    except Exception as e:
        print(e, "Not Understood")
Div(num1, num2)
print("\nCode developed by Masino")
