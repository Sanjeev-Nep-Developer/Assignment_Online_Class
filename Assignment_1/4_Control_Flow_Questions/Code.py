# Control Flow with Nested Loops and Complex Logic
# Write a Python program that simulates a number guessing game:
# The program should generate a random number between 1 and 100 and give the user 7 attempts to guess it.
# After each wrong guess, the program should provide a hint whether the guess was too high or too low.
# If the user fails to guess the number within the attempts, the program should reveal the number and ask if they would like to play again.

# Note - I have not done error handling just in hurry..😂

import random

print("Welcome To the Number Guessing Game ")
print("You have to Guess the number which is in between 1 to 100 ")
print("You can Try maximum 7 times .. ")


def game():
    randomValue = random.randint(1, 100)
    count = 1
    while (count <= 7):
        input_value = int(input("Enter the number "))
        if (input_value == randomValue):
            print(
                f"Horaayaa.. You won The Game ..  and The correct answere is  {input_value} ")
            break
        else:
            if (input_value > randomValue):
                print("To High...  ")
            else:
                print("To Low..  ")
    if (count == 7):
        print("You have Exceed the 7 attempts ")


while (True):
    game()
    value = input(
        "User , Do you want to play again the Game Yes for Y and NO for N ")
    if (value == "N"):
        print("Thank You for Playin the Game , Bye Bye see You Next Time.. ")
        break
