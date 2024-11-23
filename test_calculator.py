import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    # Add() Test Cases
    def test_add_positive_numbers(self):
        # Test adding two positive numbers
        self.assertEqual(self.calc.add(10, 20), 30)

    def test_add_negative_numbers(self):
        # Test adding two negative numbers
        self.assertEqual(self.calc.add(-10, -20), -30)

    # Subtract() Test Cases
    def test_subtract_positive_numbers(self):
        # Test subtracting two positive numbers
        self.assertEqual(self.calc.subtract(50, 30), 20)

    def test_subtract_negative_numbers(self):
        # Test subtracting two negative numbers
        self.assertEqual(self.calc.subtract(-20, -10), -10)

    # Add the following test methods to the TestCalculator class:

    # Multiply() Test Cases
    def test_multiply_positive_numbers(self):
        # Test multiplying two positive numbers
        self.assertEqual(self.calc.multiply(4, 5), 20)

    def test_multiply_negative_and_positive(self):
        # Test multiplying a negative and a positive number
        self.assertEqual(self.calc.multiply(-4, 5), -20)

    # Divide() Test Cases
    def test_divide_positive_numbers(self):
        # Test dividing two positive numbers
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_divide_negative_and_positive(self):
        # Test dividing a negative and a positive number
        self.assertEqual(self.calc.divide(-10, 2), -5)

    # Modulo() Test Cases
    def test_modulo_positive_numbers(self):
        # Test modulo operation with two positive numbers
        self.assertEqual(self.calc.modulo(10, 3), 1)

    def test_modulo_negative_number(self):
        # Test modulo operation with a negative number
        self.assertEqual(self.calc.modulo(-10, 3), -1)

if __name__ == '__main__':
    unittest.main()