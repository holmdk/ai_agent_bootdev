"""
Unit tests for the render module.

This module contains tests for the render function that formats
calculator expressions and results into text-based displays.
"""

import unittest

from pkg.render import render


class TestRender(unittest.TestCase):
    """Test suite for the render function."""

    def test_render_integer_result(self) -> None:
        """Test that rendering with an integer result works correctly."""
        result = render("2 + 2", 4)
        # Check that the result contains the expression and result
        self.assertIn("2 + 2", result)
        self.assertIn("4", result)
        # Check that the box has the expected format (top, middle, bottom borders)
        self.assertTrue(result.startswith("┌"))
        self.assertIn("│", result)
        self.assertTrue(result.endswith("┘\n") or result.endswith("┘"))

    def test_render_float_result(self) -> None:
        """Test that rendering with a float result works correctly."""
        result = render("10 / 4", 2.5)
        # Check that the result contains the expression and result
        self.assertIn("10 / 4", result)
        self.assertIn("2.5", result)

    def test_render_integer_like_float(self) -> None:
        """Test that float results that are integers are displayed as integers."""
        result = render("10 / 2", 5.0)
        # Check that the result contains the expression and integer result (not 5.0)
        self.assertIn("10 / 2", result)
        self.assertIn("5", result)
        self.assertNotIn("5.0", result)

    def test_render_none_result(self) -> None:
        """Test that rendering with None result works correctly."""
        result = render("", None)
        # Check that the result contains the expression and None
        self.assertIn("", result)
        self.assertIn("None", result)

    def test_render_error_result(self) -> None:
        """Test that rendering with an error message works correctly."""
        error_msg = "Division by zero"
        result = render("10 / 0", error_msg)
        # Check that the result contains the expression and error message
        self.assertIn("10 / 0", result)
        self.assertIn(error_msg, result)


if __name__ == "__main__":
    unittest.main()