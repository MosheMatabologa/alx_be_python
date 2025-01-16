class Book:
    def __init__(self, title, author):
        self.title = title  # Public attribute
        self.author = author  # Public attribute
        self._is_checked_out = False  # Private attribute

    def check_out(self):
        if self._is_checked_out:
            print(f"'{self.title}' is already checked out.")
        else:
            self._is_checked_out = True
            print(f"You have checked out '{self.title}'.")

    def return_book(self):
        if not self._is_checked_out:
            print(f"'{self.title}' is not currently checked out.")
        else:
            self._is_checked_out = False
            print(f"'{self.title}' has been returned.")

    def is_available(self):
        return not self._is_checked_out  # Returns True if the book is available


class Library:
    def __init__(self):
        self._books = []  # Private list to store Book objects

    def add_book(self, book):
        self._books.append(book)
        print(f"Added '{book.title}' by {book.author} to the library.")

    def check_out_book(self, title):
        for book in self._books:
            if book.title == title:
                book.check_out()
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        for book in self._books:
            if book.title == title:
                book.return_book()
                return
        print(f"Book titled '{title}' not found in the library.")

    def list_available_books(self):
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are currently available.")
