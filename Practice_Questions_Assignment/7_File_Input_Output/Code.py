# Q1) Implement a program that reads a CSV file named "data.csv," containing columns "Name" and "Age." Create a new CSV file called "adults.csv" with only the rows of individuals who are 18 years or older.

import pandas as pd
import json


df = pd.read_csv("data.csv")
adults = df[df["Age"] >= 18]
adults.to_csv("adults.csv", index=False)


# Q2)  Create a function add_to_json that takes a filename and a dictionary as input. The function should read the JSON data from the file, add the new dictionary to it, and write the updated data back to the same file.

def add_to_json(file_name, new_data):
    with open(file_name, "r") as f:
        data = json.load(f)

    data.append(new_data)

    with open(file_name, "w") as f:
        json.dump(data, f, indent=4)


new_person = {"name": "Hari", "age": 25}

add_to_json("file.json", new_person)


# Q3)  Create a function search_log that takes a log file and a search keyword as input. The function should find and display all lines containing the search keyword.

def search_log(filename, keyword):
    try:
        with open(filename, "r") as f:
            lines = f.readlines()

        found = False

        for line in lines:
            if keyword in line:
                print(line.strip())
                found = True

        if not found:
            print(f"No Lines Found containing {keyword} .. ")

    except FileNotFoundError:
        print(f"The file {filename} does not exist.. ")

