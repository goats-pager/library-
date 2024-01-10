# book.py

class Book:
    def __init__(self, book_id, title, author, genre):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.genre = genre

    def display(self):
        print(f"Book ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Genre: {self.genre}")
