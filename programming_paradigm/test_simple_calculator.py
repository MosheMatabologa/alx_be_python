#!/usr/bin/env python3

import unittest
from simple_calculator import SimpleCalculator

class SimpleCalculatorTest(unittest.TestCase):
    def setUp(self):
        """Set up an instance of SimpleCalculator for testing."""
        self.calculator = SimpleCalculator()

    # Addition tests
    def test_add_positive(self):
        self.assertEqual(self.calculator.add(2, 2), 4)

    def test_add_negative(self):
        self.assertEqual(self.calculator.add(-2, -2), -4)

    def test_add_zero(self):
        self.assertEqual(self.calculator.add(0, 0), 0)

    # Subtraction tests
    def test_subtract_positive(self):
        self.assertEqual(self.calculator.subtract(2, 2), 0)

    def test_subtract_negative(self):
        self.assertEqual(self.calculator.subtract(-2, -2), 0)

    # Multiplication tests
    def test_multiplication_positive(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)

    def test_multiplication_positive_and_negative(self):
        self.assertEqual(self.calculator.multiply(2, -2), -4)

    def test_multiplication_negative(self):
        self.assertEqual(self.calculator.multiply(-2, -2), 4)

    def test_multiplication_zero(self):
        self.assertEqual(self.calculator.multiply(0, 2), 0)

    # Division tests
    def test_division_positive(self):
        self.assertEqual(self.calculator.divide(2, 2), 1)

    def test_division_negative(self):
        self.assertEqual(self.calculator.divide(-2, -2), 1)

    def test_division_negative_positive(self):
        self.assertEqual(self.calculator.divide(-2, 2), -1)

    def test_division_by_zero(self):
        self.assertIsNone(self.calculator.divide(2, 0))


if __name__ == '__main__':
    unittest.main()
