"""
Unit tests for the Calculator class.

This module contains tests for basic arithmetic operations and error handling
in the Calculator class.
"""

import unittest

from pkg.calculator import Calculator


class TestCalculator(unittest.TestCase):
    """Test suite for the Calculator class."""

    def setUp(self) -> None:
        """Initialize a Calculator instance before each test."""
        self.calculator = Calculator()

    def test_addition(self) -> None:
        """Test that addition works correctly."""
        result = self.calculator.evaluate("3 + 5")
        self.assertEqual(result, 8)

    def test_subtraction(self) -> None:
        """Test that subtraction works correctly."""
        result = self.calculator.evaluate("10 - 4")
        self.assertEqual(result, 6)

    def test_multiplication(self) -> None:
        """Test that multiplication works correctly."""
        result = self.calculator.evaluate("3 * 4")
        self.assertEqual(result, 12)

    def test_division(self) -> None:
        """Test that division works correctly."""
        result = self.calculator.evaluate("10 / 2")
        self.assertEqual(result, 5)

    def test_nested_expression(self) -> None:
        """Test that nested expressions are evaluated with correct precedence."""
        result = self.calculator.evaluate("3 * 4 + 5")
        self.assertEqual(result, 17)

    def test_complex_expression(self) -> None:
        """Test that complex expressions with multiple operations work correctly."""
        result = self.calculator.evaluate("2 * 3 - 8 / 2 + 5")
        self.assertEqual(result, 7)

    def test_empty_expression(self) -> None:
        """Test that empty expressions return None."""
        result = self.calculator.evaluate("")
        self.assertIsNone(result)

    def test_invalid_operator(self) -> None:
        """Test that invalid operators raise a ValueError."""
        with self.assertRaises(ValueError):
            self.calculator.evaluate("$ 3 5")

    def test_not_enough_operands(self) -> None:
        """Test that expressions with insufficient operands raise a ValueError."""
        with self.assertRaises(ValueError):
            self.calculator.evaluate("+ 3")

    def test_parentheses(self) -> None:
        """Test that expressions with parentheses are evaluated correctly."""
        result = self.calculator.evaluate("(3 + 4) * 2")
        self.assertEqual(result, 14)

    def test_nested_parentheses(self) -> None:
        """Test that expressions with nested parentheses are evaluated correctly."""
        result = self.calculator.evaluate("(2 * (3 + 4)) - 5")
        self.assertEqual(result, 9)

    def test_unmatched_opening_parenthesis(self) -> None:
        """Test that expressions with unmatched opening parenthesis raise a ValueError."""
        with self.assertRaises(ValueError):
            self.calculator.evaluate("(3 + 4 * 2")

    def test_unmatched_closing_parenthesis(self) -> None:
        """Test that expressions with unmatched closing parenthesis raise a ValueError."""
        with self.assertRaises(ValueError):
            self.calculator.evaluate("3 + 4) * 2")


if __name__ == "__main__":
    unittest.main()
