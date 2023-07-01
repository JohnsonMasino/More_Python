#!/usr/bin/python3

def Nums(*num):
    """defines the class of the module"""
    nums = input("Enter number here to detect the maximum number: ")
    nums = nums.split()
    int_nums = []
    try:
        for i in nums:
            int_nums.append(int(i))
        print(f"The entered numbers are: {int_nums}")
        max_num = int_nums[0]
        for i in int_nums:
            if i > max_num:
                max_num = i
        print(f"The new max number is: {max_num}.")
    except Exception as e:
        print(e)
    finally:
        print("Program execution completed...")

if __name__ == "__main__":
    Nums(2, 3, 6, 9, 4, 6, 3)
print("\nCode developed by Masino")
