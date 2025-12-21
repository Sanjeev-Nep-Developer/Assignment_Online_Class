# Q1 [map] Write a Python function square_numbers that takes a list of integers as input and uses the map function to return a new list containing the square of each element.

from functools import reduce


def square(val):
    return val**2


num_list = [10, 20, 30, 40, 50]
result = list(map(square, num_list))
print(result)

# Q2 [map] Create a function convert_to_uppercase that takes a list of strings as input and uses the map function to return a new list with all the strings converted to uppercase.


def convert_to_uppercase(val):
    return val.upper()


list_strings = ["sanjeev", "sulav", "samir", "deepa"]
result = list(map(convert_to_uppercase, list_strings))
print(result)


# Q3 filter] Implement a function called filter_prime_numbers that takes a list of integers as input and uses the filter function to return a new list containing only the prime numbers.

def filter_prime_numbers(number):
    result = True
    if (number == 1):
        result = None
        return result
    for i in range(2, number):
        if (number % i == 0):
            result = False
            break

    return result


list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

result = list(filter(filter_prime_numbers, list_numbers))
print(result)


# Q4 [filter] Write a Python function filter_long_strings that takes a list of strings as input and uses the filter function to return a new list containing strings with more than 5 characters.


def filter_long_strings(value):
    result = False
    if (len(value) > 7):
        result = True
    return result


list_strings = ["sanjeev_khadka", "sulav khadka ", "samir kc ",
                "deepa kc ", "man bhadur khadka tero baau thote ", "sanjeev", "apple", "ball", "cat", "dog"]
output = list(filter(filter_long_strings, list_strings))
print(output)


# Q5 [reduce] Write a Python function calculate_factorial that takes an integer as input and uses the reduce function to return the factorial of that number.


def calculate_factorial(number):
    return reduce(lambda a, b: a*b, range(1, number+1))


result = calculate_factorial(5)
print(result)

# Q6 [reduce] Implement a function called concatenate_strings that takes a list of strings as input and uses the reduce function to return a single string containing the concatenation of all the elements.


def concatenate_strings(list_of_strings):
    return reduce(lambda x, y: x+y, list_of_strings)


list_str = ["apple", "ball", "cat", "dog", "elephant"]
result = concatenate_strings(list_str)
print(result)
