# Write a Program that Uses Functions write_to_file and read_from_file:
# Note , i have not done the error handling for the .. read_from_file function when the file is not present..


def write_to_file(filename, content):
    with open(filename, "w") as f:
        f.write(content)


def read_from_file(filename):
    with open(filename, "r") as f:
        print(f.read())



