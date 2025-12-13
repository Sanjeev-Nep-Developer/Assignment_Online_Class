# Write a Python program that iterates through integers from 1 to 50. For each multiple of three, print "Fizz" instead of the number; for each multiple of five, print "Buzz". For numbers that are multiples of both three and five, print "FizzBuzz".
# The FizzBuzz problem is a common coding challenge that is often used in programming interviews to test basic programming skills. The problem typically requires writing a function that prints numbers from 1 to a given limit, but with a twist:

# For multiples of 3, print "Fizz" instead of the number.
# For multiples of 5, print "Buzz" instead of the number.
# For numbers which are multiples of both 3 and 5, print "FizzBuzz".


for i in range(1, 51):
    if (i % 3 == 0 and i % 5 == 0):
        print("FizzBuzz")
    elif (i % 3 == 0):
        print("Fizz")
    elif (i % 5 == 0):
        print("Buzz")
    else:
        print(i)    
