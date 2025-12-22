# Math Tutor Using Random, Arithmetic Operators, and OOP
# Scenario: Create a MathTutor class that generates random math questions using random and math operators.

# Track correct and incorrect answers.
# Provide a score at the end.
# Handle invalid input using exception handling.
# Concepts: Random, Math, Exception Handling, Classes


import random


class MathTutor:
    def __init__(self):
        print("Math Tutor class is being Called.. ")

    def generate_random_questions(self, name_of_the_player):
        # Generate random operands
        name = name_of_the_player
        Score = 0
        correct_answers = 0
        incorrect_answers = 0
        number_times_played = 1

        cond = True
        while (cond):

            num1 = random.randint(1, 10)
            num2 = random.randint(1, 10)
            operators = ['+', '-', '*', '/']
            operator = random.choice(operators)

            # Perform arithmetic Operation
            if operator == '+':
                result = num1 + num2
            elif operator == '-':
                result = num1 - num2
            elif operator == '*':
                result = num1 * num2
            else:
                result = num1 / num2

            question = f"Question is What is the value of {num1} {operator} {num2} "
            print(question)
            try:
                answer = int(input("Enter the answere : "))

            except ValueError as e:
                print("Invalid input type of The Variable.. ", e)
                print("Try Again.. ")

            else:
                if (result == answer):
                    print("You Won The Game.. ")
                    correct_answers += 1
                    Score += 1
                    val = input(
                        "Enter Do you want to continue playing the Game , Yes for Y and No for N : ")
                    val = val.upper()
                    if (val == 'Y'):
                        number_times_played += 1
                        continue
                    else:
                        cond = False
                        break
                elif (result != answer):
                    print(" Wrong Answer : ")
                    incorrect_answers += 1
                    Score -= 1
                    val = input(
                        "Enter Do you want to continue playing the Game , Yes for Y and No for N : ")
                    val = val.upper()
                    if (val == 'Y'):
                        number_times_played += 1
                        continue
                    else:
                        cond = False
                        break
        print("\n")
        print("Your Overall Results of The Game you played are below -: ")
        print("Name of The Player is : ", name)
        print("Score of The game ", Score)
        print("Correct answers is ", correct_answers)
        print("Incorrect answers is ", incorrect_answers)

sanjeev1 = MathTutor()
sanjeev1.generate_random_questions("sanjeev khadka ")