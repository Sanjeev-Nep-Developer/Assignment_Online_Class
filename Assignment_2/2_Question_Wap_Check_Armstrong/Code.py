# Write a Python program to check whether a given number is an Armstrong number or not.

# Definition: An Armstrong number (also known as a narcissistic number) is a number that is equal to the sum of its own digits each raised to the power of the number of digits. For example:

# 153 is an Armstrong number because ( 1^3 + 5^3 + 3^3 = 153 ).
# 9474 is an Armstrong number because ( 9^4 + 4^4 + 7^4 + 4^4 = 9474 ).

def checkArmstrong(num):
    lengthDigit = int(len(str(num)))
    originalValue = num
    value = num
    totalValue = 0
    while (value != 0):
        lastValue = value % 10
        totalValue = totalValue + (lastValue ** lengthDigit)
        value = int(value / 10)
    print(totalValue)
    print(originalValue)
    result = True if originalValue == totalValue else False
    return result


output = checkArmstrong(153)
print(output)

output = checkArmstrong(9474)
print(output)