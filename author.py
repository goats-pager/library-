# author.py

class Author:
    def __init__(self, author_id, name, nationality):
        self.author_id = author_id
        self.name = name
        self.nationality = nationality

    def display(self):
        print(f"Author ID: {self.author_id}, Name: {self.name}, Nationality: {self.nationality}")
