# main.py

from book import Book
from author import Author
from library import Library

# Create authors
author1 = Author(1, "J.K. Rowling", "British")
author2 = Author(2, "George Orwell", "British")

# Create books
book1 = Book(101, "Harry Potter and the Sorcerer's Stone", author1, "Fantasy")
book2 = Book(102, "1984", author2, "Dystopian Fiction")

# Create a library
library = Library()

# Add books and authors to the library
library.add_book(book1)
library.add_book(book2)
library.add_author(author1)
library.add_author(author2)

# Display books and authors in the library
library.display_books()
library.display_authors()
