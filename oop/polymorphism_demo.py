#!/usr/bin/env python3

import math

class Shape:
    """Base class for all shapes."""
    def area(self):
        """Calculate the area of the shape. Must be overridden in derived classes."""
        raise NotImplementedError("The area method must be overridden in subclasses.")

class Rectangle(Shape):
    """Derived class representing a rectangle."""
    def __init__(self, length, width):
        """Initialize a rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Calculate the area of the rectangle."""
        return self.length * self.width

class Circle(Shape):
    """Derived class representing a circle."""
    def __init__(self, radius):
        """Initialize a circle with a radius."""
        self.radius = radius

    def area(self):
        """Calculate the area of the circle."""
        return math.pi * (self.radius ** 2)
