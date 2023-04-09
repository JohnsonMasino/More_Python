#!/usr/bin/python3
"""
This function multiplies two numbers
"""
def function():
    num = input("Enter two numbers to be multiplied and separate with space: ")
    num = num.split(" ")
    num1 = int(num[0])
    num2 = int(num[1])
    try:
        print("Product is: ", (num1 * num2))
    except ValueError:
        return ("Not compatible")
   # except Exception as e:
    #    print(e)
    else:
        print("Successful...")
    finally:
        return ("The end")
print(function())
print("\nCode developed by Masino")
