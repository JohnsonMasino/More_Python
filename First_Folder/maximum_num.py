#!/usr/bin/python3

numbers = input("Enter numbers here separating them with a space: ")
split_numbers = numbers.split(" ")
count = 0
for num in split_numbers:
    count += 1
print("The lenght of this list is: ", count)
for num in range(count):
    split_numbers[num] = int(split_numbers[num])
print("Numbers are: ", split_numbers)

maximum = split_numbers[0]

for num in split_numbers:
    maximum = split_numbers[0]
    while num > maximum:
        maximum = num
        break
print("The maximum number is: ", maximum)    
print("\nCode developed by Masino")
