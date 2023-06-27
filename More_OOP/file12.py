#!/usr/bin/python3

#This program arranges books in a library in the order of ID number

def Storage():
    'defines the function of the module'

    print("Hi!\nWelcome to the big 'Medico Library'.\nWe are happy you took a session in our prestigiuos library...")
    print("""Our Book numbers always start with the Initials of the subject topic(example: BCH_291 for Biochemistry) as folows:\nPhysiology 'PHS'\nAnatomy 'ANA'\nMedicine 'MED'\nSurgery 'SURG'\nBiochemistry 'BCH'""")
    book_num = input("Enter the bold book number on the front page of the book you want to return to the book shelve: ")
    if book_num[0] == 'P':
        sorted_id = input("Enter the id number just below the bold book number(example: ID002): ")
        if sorted_id == "ID001":
            print("You have an 'Introduction to Physiology' textbook and the shelve is at:\nRow 1(floor row) at Rack/Stand 1 labelled 'Physiology rack'")
        elif sorted_id == "ID002":
            print("You have the 'Basic Principles of Physiology' textbook and the shelve is at:\nRow 2(second row) at Rack/Stand 1 labelled 'Physiology Rack'")
        elif sorted_id == "ID003":
            print("You have the 'Degree In Physiology' textbook and the shelve is at:\nRow 3(third row) at Rack/Stand 1 labelled 'Physiology Rack'")
        elif sorted_id == "ID004":
            print("You have the 'Advanced Physiology' textbook and the shelve is at:\nRow 4(fourth row) at Rack/Stand 1 labelled 'Physiology Rack'")
        elif sorted_id == "ID005":
            print("You have the 'Master of Pysiology' textbook and the shelve is at:\nRow 5(top row) at Rack/Stand 1 labelled 'Physiology Rack'")
        else:
            print("Unrecognised input.\nCheck and try again...")
    elif book_num[0] == 'A':
        sorted_id = input("Enter the id number just below the bold book number(example: ID002): ")
        if sorted_id == "ID001":
            print("You have the 'Introduction To Anatomy' textbook and the shelve is at:\nRow 1(floor row) at Rack/Stand 2 labelled 'Anatomy Rack'")
        elif sorted_id == "ID002":
            print("You have the 'Basic Principles Of Anatomy' textbook and the shelve is at:\nRow 2(second row) at Rack/Stand 2 labelled 'Anatomy Rack'")
        elif sorted_id == "ID003":
            print("You have the 'Degree in Anatomy' textbook and the shelve is at:\nRow 3(third row) at Rack/Stand 2 labelled 'Anatomy Rack'")
        elif sorted_id == "ID004":
            print("You have the 'Advanced Anatomy' textbook and the shelve is at:\nRow 4(fourth row) at Rack/Stand 2 labelled 'Anatomy Rack'")
        elif sorted_id == "ID005":
            print("You have the 'Master of Physiology' textbook and the shelve is at:\nRow 5(top row) at Rack/Stand 2 labelled 'Anatomy Rack'")
        else:
            print("Unrecognised input.\nCheck and try again...")

    elif book_num[0] == 'M':
        sorted_id = input("Enter the id number just below the bold book number(example: ID002): ")
        #sorted_id = id_num.split()
        if sorted_id == "ID001":
            print("You have an 'Introduction to Medicine' textbook and the shelve is at:\nRow 1(floor row) at Rack/Stand 3 labelled 'Medicine Rack'")
        elif sorted_id == "ID002":
            print("You have the 'Basic Principles of Medicine' textbook and the shelve is at:\nRow 2(second row) at Rack/Stand 3 labelled 'Medicine Rack'")
        elif sorted_id == "ID003":
            print("You have the 'Degree in Medicine' textbook and the shelve is at:\nRow 3(third row) at Rack/Stand 3 labelled 'Medicine Rack'")
        elif sorted_id == "ID004":
            print("You have the 'Advanced Medicine' textbook and the shelve is at:\nRow 4(fourth row) at Rack/Stand 3 labelled 'Medicine Rack'")
        elif sorted_id == "ID005":
            print("You have the 'Master of Physiology' textbook and the shelve is at:\nRow 5(top row) at Rack/Stand 3 labelled 'Medicine Rack'")
        else:
            print("Unrecognised input.\nCheck and try again...")

    elif book_num[0] == 'S':
        sorted_id = input("Enter the id number just below the bold book number(example: ID002): ")
        #sorted_id = id_num.split()
        if sorted_id == "ID001":
            print("You have an 'Introduction to Surgery' textbook and the shelve is at:\nRow 1(floor row) at Rack/Stand 4 labelled 'Surgery Rack'")
        elif sorted_id == "ID002":
            print("You have the 'Basic Principles of Surgery' textbook and the shelve is at:\nRow 2(second row) at Rack/Stand 4 labelled 'Surgery Rack'")
        elif sorted_id == "ID003":
            print("You have the 'Degree in Surgery' textbook and the shelve is at:\nRow 3(third row) at Rack/Stand 4 labelled 'Surgery Rack'")
        elif sorted_id == "ID004":
            print("You have the 'Advanced Surgery' textbook and the shelve is at:\nRow 4(fourth row) at Rack/Stand 4 labelled 'Surgery Rack'")
        elif sorted_id == "ID005":
            print("You have the 'Master of Surgery' textbook and the shelve is at:\nRow 5(top row) at Rack/Stand 4 labelled 'Surgery Rack'")
        else:
            print("Unrecognised input.\nCheck and try again...")

    elif book_num[0] == 'B':
        sorted_id = input("Enter the id number just below the bold book number(example: ID002): ")
        #sorted_id = id_num.split()
        if sorted_id == "ID001":
            print("You have an 'Introduction to Biochemistry' textbook and the shelve is at:\nRow 1(floor row) at Rack/Stand 5 labelled 'BCH Rack'")
        elif sorted_id == "ID002":
            print("You have the 'BAsic Principles of Biochemistry' textbook and the shelve is at:\nRow 2(second row) at Rack/Stand 5 labelled 'BCH Rack'")
        elif sorted_id == "ID003":
            print("You have the 'Degree In Biochemistry' textbook and the shelve is at:\nRow 3(third row) at Rack/Stand 5 labelled 'BCH Rack'")
        elif sorted_id == "ID004":
            print("You have the 'Advanced Biochemistry' textbook and the shelve is at:\nRow 4(fourth row) at Rack/Stand 5 labelled 'BCH Rack'")
        elif sorted_id == "ID005":
            print("You have the 'Master Of Biochemistry' textbook and the shelve is at:\nRow 5(top row) at Rack/Stand 5 labelled 'BCH Rack'")
        else:
            print("Unrecognised input.\nCheck and try again...")

    else:
        print("Please check and confirm the book number again...\nThe one you just entered is unrecognised")

if __name__ == "__main__":
    Storage()
print("\nCode developed by Masino")
