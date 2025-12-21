# Q1) Write a Python function called check_odd_even that takes an integer as input and uses a ternary operator to return "Even" if the number is even, and "Odd" if the number is odd.

import math


def check_odd_even(num):
    result = "Even Number" if num % 2 == 0 else "Odd Number"
    return result


output = check_odd_even(5)
print(output)

# Q2) Create a Python function check_leap_year that takes a year as input and uses a ternary operator to determine if it's a leap year. Return "Leap Year" if it is, otherwise "Not a Leap Year." (A leap year is divisible by 4, except for years divisible by 100 but not divisible by 400).


def check_leap_year(year):
    result = "Leap_year" if (year % 4 == 0 and (
        year % 100 != 0 or year % 400 == 0)) else "Not a Leap Year"
    return result


result = check_leap_year(2028)
print(result)


# Q3) Write a function find_bigger_number that takes three integers as input and uses a ternary operator to return the larger number. If all numbers are equal, return "Equal."

def find_bigger_number(a=int, b=int, c=int):
    # result = "a is greater " if(a > b and a > c) elif(b >a and b > c) "B is greater "  else "Cis greater "
    if (a == b == c):
        return "All Numbers are Equal "
    if (c > a and c > b):
        return "C is greater than A and B "
    else:
        result = "A is greater than B and C " if (
            a > b and a > c) else "B is greater than A and C "
        return result


output = find_bigger_number(a=20, b=30, c=40)
print(output)


# Q4 Implement a function called check_prime that takes a positive integer as input and uses a ternary operator to determine if it's a prime number. Return "Prime" if it is, otherwise "Not Prime."


def check_prime(num=int):
    cond = True
    for i in range(2, num):
        if (num % 2 == 0):
            cond = False
            break
    result = "Prime Number " if (cond) else "Not a Prime Number "
    return result


output = check_prime(6)
print(output)
