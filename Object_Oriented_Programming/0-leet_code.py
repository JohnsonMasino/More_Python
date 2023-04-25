#!/usr/bin/python3

#This class is a leet_code test

class Solution:
    def fizzBuzz():
        """
        :type n: int
        :rtype: List[str]
        """
        n = int(input("Please enter a number here: "))
        num = []
        for i in range(1, n + 1):
#            cnt = cnt + 1
            if i % 3 == 0 and i % 5 == 0:
                print("FizzBuzz")
            elif i % 5 == 0:
                print("Buzz")
            elif i % 3 == 0:
                print("Fizz")
            else:
                print(i)
#        print(num.append("Me"))

Solution.fizzBuzz()
print("\nCode developed by Masino")
