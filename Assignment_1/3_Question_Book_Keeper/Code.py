# A list of tuples, where each tuple contains information about a book: (title, genre, year_published, times_borrowed).

books = [
    ("The Alchemist", "Fiction", 1988, 250),
    ("The Da Vinci Code", "Mystery", 2003, 300),
    ("A Brief History of Time", "Science", 1988, 150),
    ("The Theory of Everything", "Science", 2002, 100),
    ("Pride and Prejudice", "Fiction", 1813, 200),
    ("To Kill a Mockingbird", "Fiction", 1960, 180),
    ("The Catcher in the Rye", "Fiction", 1991, 220),
    ("Angels & Demons", "Mystery", 2000, 210),
    ("The Grand Design", "Science", 2010, 90),
    ("1984", "Fiction", 1949, 190)
]


# Task 01: Create a Book Filtering Function

def filter_book(genre, year):
    list_books = []
    for book in books:
        if(book[1] == genre and book[2] >= year):
            list_books.append(book[0])
    
    return list_books;

result = filter_book("Fiction", 1980)        
print(result)

# Task 02 : Write a Python program that uses a lambda expression to sort this list by publication year in ascending order. Print the sorted list of books.


sorted_books = sorted(books,key=lambda item:item[2])
print(sorted_books)