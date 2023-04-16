#!/usr/bin/python3

#This code multiplies two numbers

print("""This Function multiplies two numbers""")

nums = input("Enter two numbers(separate with a space) here: ")

nums = nums.split(" ")
num1 = int(nums[0])
num2 = int(nums[1])
count = 0
for i in nums:
    count += 1
for i in range(count):
    nums[i] = int(nums[i])

print(nums)
def mul(a, b):
    return a * b

print("The product is: ", mul(num1, num2))
print("\nCode developed by Masino")
