#!/usr/bin/python3

"""
This File imports the add function and calls it to add two numbers
"""
import add_path_one.add_fxn as af

class UserInput:
    """Defines the class of the file"""
    def User():
        """Defines the usage of the file"""
        inputs = input("Please enter two numbers to be added: ")
        inputs = inputs.split()
        input0 = int(inputs[0])
        input1 = int(inputs[1])
        #print(input0, input1)
        answer = af.Adding(input0, input1)
        print("The sum of these number is: ", answer)
UserInput.User()
print("\nCode develoepd by Masino")
