#!/usr/bin/env python3

class Book:
    def __init__(self, title, author, year):
        """Initialize a Book instance with title, author, and year."""
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """Print a message upon object deletion."""
        print(f"Deleting {self.title}")

    def __str__(self):
        """Return a human-readable string representation."""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Return an unambiguous string representation to recreate the instance."""
        return f"Book('{self.title}', '{self.author}', {self.year})"

