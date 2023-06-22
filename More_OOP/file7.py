#!/usr/bin/python3

#This file generates random password

def PassWord():
    """defines the function of the password generator file"""
    import random as rd

    LETTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '%', '&', '?', '=']

    name = input("Welcome here.\nTell us your name please...: ")
    print(f"Hi {name}!\nWelcome to Masino's Password generator.")
    LET_no = int(input("How many upper case letters would you want in your password ? "))
    let_no = int(input("How many lower case letters would you want in your password ? "))
    num_no = int(input("How many digits would you want in your password ? "))
    sym_no = int(input("How many symbols would you want in your password ? "))
    print(f"Got it {name}.\nWe are generating your password now...")
    password = []
    for i in range(0, (LET_no + 1)):
        char = rd.choice(LETTERS)
        password += char

    for i in range(0, (let_no + 1)):
        char = rd.choice(letters)
        password += char

    for i in range(0, (num_no + 1)):
        char = rd.choice(numbers)
        password += char

    for i in range(0, (sym_no + 1)):
        char = rd.choice(symbols)
        password += char
    rd.shuffle(password)
    pswd = ""
    for i in password:
        pswd += i
    print(f"Your password is: {pswd}\nThank you for using masino's password generator")

if __name__ == "__main__":
    PassWord()
print("\nCode developed by Masino")
