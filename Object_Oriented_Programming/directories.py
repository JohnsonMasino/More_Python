#!/usr/bin/python3

"""
This class shows the directories of
some modules that I will be using in my
alx airbnb clone projects
"""
class Dir:
    """The main class"""
    def directories():
        """Calls the directories of these
        modules individualy"""
        import sys, cmd, turtle
        #import cmd
        #import turtle
        
        print("The directories of the 'sys' module are:\n", dir(sys))
        print()
        print("The directories of the 'turtle' module are:\n", dir(turtle))
        print()
        print("The directories of the 'cmd' module are:\n",dir(cmd))

Dir.directories()
print("\nCode developed y Masino")
