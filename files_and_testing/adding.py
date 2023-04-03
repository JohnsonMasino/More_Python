#!/usr/bin/python3

#This function sums two numbers.
#Code by Masino.
print("This function sums two numbers")
nums = input("Enter two numbers separate with comma: ")
list_nums = nums.split(",")
a = int(list_nums[0])
b = int(list_nums[1])
def add(a, b):
    if a == b:
        print("You enetered same number\nI can call this function but Masino asked me not to.\nTry different numbers")
    return a + b
print("The sum of both numbers is: ", add(a, b))
print("\nCode developed by Masino")
