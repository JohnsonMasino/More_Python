#!/usr/bin/python3

class Student():
    """defines the class of the function"""

    def __init__(self, name):
        """initialises the parameters"""
        self.name = name

students = reload() #recreates the instances o fthe students file
s = Student("Johnson Masino")
students.append(s)
save(students) #saves the students objects to a file

if __name__ == "__main__":
    Student("Johnson Masino")
print("\nCode developed by Masino")
