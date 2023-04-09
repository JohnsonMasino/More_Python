#!/usr/bin/python3

"""
This program stores an information of a person in a dictionary
"""

def diction():
    dic = {"name": "Johnson Masino", "complexion": "Fair", "Remark": "Very Good"}
    try:
        print("# Name: " + dic["name"] + "\n# Complexion: " + dic["complexion"] + "\n# Remark: " + dic["Remark"])
    except NameError:
        print("Not identified")
    except Exception as e:
        print(e)
    else:
        print("Success!")
    finally:
        print("End Of code")
diction()    
print("\nCode developed by Masino")
