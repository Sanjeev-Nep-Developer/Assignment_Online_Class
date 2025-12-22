# Question Exception Handling Scenario: Online Age-Restricted Service
# Scenario: You’re building a sign-up system for an online movie rental platform. Some movies are age-restricted (18+). You need to ensure proper validation and error handling during user registration.
# Task:
# Create a custom exception class called UnderageError that inherits from Exception.
# Write a function register_user() that:
# Takes a user’s name and age as input.
# Raises UnderageError if the user is under 18.
# Otherwise, prints a welcome message.
# Wrap the function call in a try block and handle the exception.
# Use else to confirm successful registration and finally to always print “Thank you for using MovieTime!” regardless of outcome.
# Also try to validate if the age input is numeric. Raise a ValueError if not, and handle it separately.

class UnderAgeError(Exception):
    pass




class online_movie:
    def __init__(self):
        print("Welcome to The Online Movie System..   ")

    def register_user(self, name, age):
        self.name = name
        self.age = age

        try:

            if (age < 18):
                raise UnderAgeError(
                    "You Have not Reached the Age to Go to The Flim Now....  ")
            else:
                print("SuccessFully Registered for the Flim  ", name)

        except ValueError as e:
            print("Wrong Input Type for the Age : ", e)

        finally:
            print("Thank you for using Movie Time ! ")


mangoHall = online_movie()
mangoHall.register_user("sanjeev khadka ", 10)
