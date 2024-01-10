# library.py

from book import Book
from author import Author

class Library:
    def __init__(self):
        self.books = []
        self.authors = []

    def add_book(self, book):
        self.books.append(book)

    def add_author(self, author):
        self.authors.append(author)

    def display_books(self):
        print("All Books:")
        for book in self.books:
            book.display()

    def display_authors(self):
        print("All Authors:")
        for author in self.authors:
            author.display()
