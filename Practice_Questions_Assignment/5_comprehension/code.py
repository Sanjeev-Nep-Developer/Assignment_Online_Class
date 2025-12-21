# Q1) [list comprehension] Given a list of strings, create a new list that contains only the strings with more than 5 characters using list comprehension.

list_strings = ["sanjeev khadka", "sanjeev", "sulav", "sanjay"]
new_list = []
for i in list_strings:
    if (len(i) > 5):
        new_list.append(i)

print(new_list)

# Q2) [list comprehension] Given two lists of integers, create a list that contains the product of each element of the first list with the corresponding element in the second list using list comprehension.

first_list = [10, 20, 30, 40]
second_list = [50, 60, 70, 80]

new_list = []
i = 0
j = len(second_list)
while (i < j):
    output = first_list[i] * second_list[i]
    new_list.append(output)
    i+=1

print(new_list)


# Q3) [list comprehension] Given three lists list1, list2, and list3, each containing integers, write a Python program using list comprehension to generate a new list of unique triplets (x, y, z) where x is from list1, y is from list2, and z is from list3, such that x + y + z = 0.

list1 = [-7, 1, 30, 40, 50, 60]
list2 = [+3, -9, 40, 60, 80, 90]
list3 = [+4, 8, 110, 120, 130, 140]

new_list = [
    (i, j, k)
    for i in list1
    for j in list2
    for k in list3
    if i + j + k == 0
]

print(new_list)


# Q4) [dictionary comprehension] Given two lists - one containing keys and another containing values, create a dictionary using dictionary comprehension.

list1 = ["nme", "age", "class", "current_class"]
list2 = ["Sanjeev Khadka ", "18", "12", "10"]

new_dict = {}
i = 0
length = len(list1)
while (i < length):
    new_dict[list1[i]] = list2[i]
    i += 1

print(new_dict)

# Q5) [dictionary comprehension] Given a dictionary with students' names as keys and their respective scores as values, create a new dictionary that contains only the students who scored more than 80 using dictionary comprehension.

dict_values = {"sanjeev": 98, "sulav": 90,
               "sanjay": 80, "sourav": 100, "sankesh": 70}
new_dict = {}
for i in dict_values:
    if (dict_values[i] > 80):
        new_dict[i] = dict_values[i]

print(new_dict)

# Q6) [dictionary comprehension] Create a dictionary using dictionary comprehension to represent the ASCII values of lowercase alphabets (a-z) where the keys are the alphabets, and the values are their corresponding ASCII values.
new_dict = {}
for i in range(ord('a'), ord('z') + 1):
    new_dict[chr(i)] = i

print(new_dict)

# Q7) [set comprehension] Given a list of numbers, create a set using set comprehension that contains only unique even numbers.

list_numbers = [1, 3, 4, 8, 12, 16, 20, 24, 9]
new_values =set()
for i in list_numbers:
    if (i % 2 == 0):
        new_values.add(i)

print(new_values)


# Q8) [set comprehension] Given a list of words, write a Python program to create a set using set comprehension that contains all the unique characters present in the words.
set_words = set()
list_words = ["sanjeev","apple","sanjay","ball"]
for i in list_words:
    for j in i:
        set_words.add(j)

print(set_words)      


# Q9) [set comprehension] Given two strings, write a Python program to create a set using set comprehension that contains all the characters that are common in both strings.

new_set = set()
string1 = "sanjeev"
string2 = "sanjay"
for i in string1:
    for j in string2:
        if(i == j):
            new_set.add(j)

print(new_set)            