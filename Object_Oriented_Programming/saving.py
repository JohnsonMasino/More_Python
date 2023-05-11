#!/usr/bin/python3

"""
This class saves a data to
a list fir re-use
"""
class Schooling:

    def __init__(self, name, id_num):
        self.name = name
        self.id_num = id_num

    def say_name(self):
        print("Hi!\nMy new name is:", self.name)

    def say_id(self):
        print("My new id_number is",  self.id_num)

student = []
#student = reload()
print(student.append(Schooling("Marcell", "903-620-6457")))
#save(student)

Schooling("Johnson Masino", "903-620-6457").say_name()
Schooling("Johnson Masino", "903-620-6457").say_id()

print("\nCode developed by Masino")
