#!/usr/bin/python3

#This code subtracts two numbers.

print("This function subtracts second number from first")
numbers = input("Please enter two numbers(separate them with a space) here: ")
sorted_num = numbers.split(" ")
num1 = int(sorted_num[0])
num2 = int(sorted_num[1])

def sub(a, b):
    return a - b

print("The difference is: ", sub(num1, num2))
print("\nCode developed by Masino")
