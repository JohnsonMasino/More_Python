#!/usr/bin/python3

height = input("Hi there!\nEnter heights here(separate with comma): ")
split_ht = height.split(",")
#print("The entered data in list is: ", split_ht)
count = 0
for i in (split_ht):
    count += 1
#print("The length of this list is: ", count)    
for i in range(count):
    split_ht[i] = int(split_ht[i])
print("The entered data is: ", split_ht)
print("The length of this list is: ", count)
num = 0
for i in split_ht:
    
    num = num + i
average = num/count
print("The average of these heights is: ", average)
print("\nCode developed by Masino")
