# Q1 Write a Python function that takes an arbitrary number of positional arguments and returns the sum of all the numbers. Test your function with various input cases.
def sum_parameters(*args):
    totalSum = 0
    for i in args:
        totalSum += i
    return totalSum


result = sum_parameters(10, 20, 30, 40, 50, 60)
print(result)

# Q2 Write a Python function concat_strings that takes any number of strings as arguments and returns a single concatenated string.


def concat_strings(*args):
    total_string = ""
    for i in args:
        total_string += i
    return (total_string)


result = concat_strings("sanjeev", "sulav", "samir")
print(result)

# Q3  Write a Python function calculate_total_cost that calculates the total cost of items purchased from a store. The function should accept multiple keyword arguments, where the key is the item name, and the value is the item's price. The function should return the total cost of all items.


def calculate_total_cost(**kwargs):
    total_cost = 0
    for [key, value] in kwargs.items():
        total_cost += value

    return total_cost


result = calculate_total_cost(chips=200, apple=300, layz=5000)
print(result)


# Q4  Create a function create_student_report that takes the student's name as the first argument, the student's age as the second argument, and an arbitrary number of keyword arguments for the subjects and their respective scores. The function should return a dictionary with the student's information and a list of subjects along with their scores.

def create_student_report(student_name, student_age, **subjects_with_scores):
    dict = {
        "name": student_name,
        "age": student_age,
        "subject_scores": subjects_with_scores
    }
    return dict


result = create_student_report(
    "Sanjeev Khadka ", 18, Maths=100, Science=90, English=80)
print(result)


