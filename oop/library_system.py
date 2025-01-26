#!/usr/bin/env python3

class Book:
    def __init__(self, title, author):
        """Initialize a Book with title and author."""
        self.title = title
        self.author = author

    def __str__(self):
        """Return a string representation of a Book."""
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    def __init__(self, title, author, file_size):
        """Initialize an EBook with title, author, and file size."""
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """Return a string representation of an EBook."""
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        """Initialize a PrintBook with title, author, and page count."""
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """Return a string representation of a PrintBook."""
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    def __init__(self):
        """Initialize a Library with an empty list of books."""
        self.books = []

    def add_book(self, book):
        """Add a book to the library."""
        if isinstance(book, Book):
            self.books.append(book)
        else:
            raise ValueError("Only instances of Book, EBook, or PrintBook can be added.")

    def list_books(self):
        """List all books in the library."""
        for book in self.books:
            print(book)

