# Q1) Write a Python program that takes two integers as input and performs division (num1 / num2). Handle the ZeroDivisionError and display a custom error message when the second number is zero.

num1 = int(input("Enter a number : "))
num2 = int(input("Enter another number : "))


class ZeroDivisionError(Exception):
    pass


try:
    if (num2 == 0):
        raise ZeroDivisionError(
            "Second number should not be given Zero number")
    result = num1/num2
    print(result)
except Exception as e:
    print(e)


# Q2) Implement a program that takes user input for a filename, opens the file in read mode, and displays its contents. Handle the FileNotFoundError and display an error message if the file is not found.


def func(file_name):
    try:
        with open(file_name, "r") as f:
            print(f.read())
    except FileNotFoundError as E:
        print("FileNotFound Give the Name Correctly  Error ", E)


file_name_user = input("Enter the file Name : ")
func(file_name_user)


# Q3  Write a Python program that takes a user input and converts it to an integer. Handle the ValueError and display a custom error message when the input cannot be converted to an integer.


num = input("Enter a Number : ")

try:
    result = int(num)
    print("Succesfully Done The Converstion From String to Integer ", result)
    print(type(result))
except ValueError as e:
    print("Wrong Data Type input for Converting into Integer ", e)
else:
    print("No Error Ocured")


# Q4 Write a Python program that takes two integers as input and performs division (num1 / num2). Handle both ValueError (if non-integer input) and ZeroDivisionError and display appropriate error messages.

num1 = input("Enter first number : ")
num2 = input("Enter second number: ")

try:
    num1_value = int(num1)
    num2_value = int(num2)
    result = num2_value/num1_value
    print(result)
except ValueError as e:
    print("Wrong Data Type input for this Program.. ")

except ZeroDivisionError as e:
    print("num1 value is zero , and division can't be done .. ")


# Q5) Write a Python program that takes user input for age. Create a custom exception InvalidAgeError to handle cases where the age is below 0 or above 120.

class InvalidAgeError(Exception):
    pass


value = int(input("Enter the age : "))
if (value < 0 or value > 120):
    raise InvalidAgeError()
print("Program is Working Fine.. ")


# Q6) Implement a program that reads user input for a password. Create a custom exception WeakPasswordError to handle cases where the password should be
# at least 8 characters
# at least 1 uppercase letter, 1 lowercase letter, and 1 number
# contain special characters
# Hint: WeakPasswordError that inherits Exception class

import re


class WeakPasswordError(Exception):
    pass


def validate_password(psw):
    if (len(psw) < 8):
        raise WeakPasswordError("Password should be at least 8 characters..")

    pattern = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$"

    if not re.match(pattern, psw):
        raise WeakPasswordError("Password doesn't meet the requirements ")

    return True


password = input("Enter a password.. : ")
try:
    validate_password(password)
    print("password is valid.. ")
except WeakPasswordError as e:
    print("Invalid Password : ", e)
