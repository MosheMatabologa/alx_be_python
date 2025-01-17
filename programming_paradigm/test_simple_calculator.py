#!/usr/bin/env python3

import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculatorTest(unittest.TestCase):
    def setUp(self):
        """Set up an instance of SimpleCalculator for testing."""
        self.calculator = SimpleCalculator()

    # Addition tests
    def test_addition(self):
        """Test addition of two positive numbers."""
        self.assertEqual(self.calculator.add(2, 2), 4)

    def test_add_positive(self):
        self.assertEqual(self.calculator.add(3, 7), 10)

    def test_add_negative(self):
        self.assertEqual(self.calculator.add(-5, -8), -13)

    def test_add_zero(self):
        self.assertEqual(self.calculator.add(0, 0), 0)

    # Subtraction tests
    def test_subtraction(self):
        """Test subtraction of two positive numbers."""
        self.assertEqual(self.calculator.subtract(10, 4), 6)

    def test_subtract_positive(self):
        self.assertEqual(self.calculator.subtract(5, 2), 3)

    def test_subtract_negative(self):
        self.assertEqual(self.calculator.subtract(-4, -6), 2)

    # Multiplication tests
    def test_multiplication(self):
        """Test multiplication of two positive numbers."""
        self.assertEqual(self.calculator.multiply(3, 4), 12)

    def test_multiplication_positive(self):
        self.assertEqual(self.calculator.multiply(5, 6), 30)

    def test_multiplication_positive_and_negative(self):
        self.assertEqual(self.calculator.multiply(5, -3), -15)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiply(-7, -2), 14)

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiply(8, 0), 0)

    # Division tests
    def test_division(self):
        """Test division of two positive numbers."""
        self.assertEqual(self.calculator.divide(8, 2), 4)

    def test_division_positive(self):
        self.assertEqual(self.calculator.divide(10, 5), 2)

    def test_division_negative(self):
        self.assertEqual(self.calculator.divide(-15, -3), 5)

    def test_division_negative_positive(self):
        self.assertEqual(self.calculator.divide(-9, 3), -3)

    def test_division_by_zero(self):
        self.assertIsNone(self.calculator.divide(10, 0))


if __name__ == '__main__':
    unittest.main()

