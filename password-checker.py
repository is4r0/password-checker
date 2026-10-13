import re

def validator(code):
    digit = r'[0-9]'
    upper = r'[A-Z]'
    lower = r'[a-z]'
    symbol = r'[~`!@#$%^&*()_+-={}|[]\\;,./<>?]'

    length = len(code)
    points = 5

    if length < 6:
        print("password length must be greater than 6")
        points = points - 1

    if not re.search(digit, code):
        print("password must contain a number 0-9")
        points = points - 1

    if not re.search(upper, code):
        print("password must contain a upper-case letter A-Z")
        points = points - 1

    if not re.search(lower, code):
        print("password must contain a lower-case letter a-z")
        points = points - 1

    if not re.search(symbol, code):
        print("password must contain a special symbol (~`!@#$%^&*()_+-={}|[]\\;,./<>?)")
        points = points - 1

    if points >= 5:
        print("Strong Password")


if __name__ == "__main__":
    password = input("Password : ")
    validator(password)