"""
Command-line interface for the Calculator application.

This module provides a simple CLI for evaluating mathematical expressions
using the Calculator class and rendering the results.
"""

import sys

from pkg.calculator import Calculator
from pkg.render import render


def main() -> None:
    """
    Parse command-line arguments and evaluate the given expression.

    If no expression is provided, display usage instructions.
    """
    calculator = Calculator()

    # Check if any arguments were provided
    if len(sys.argv) <= 1:
        print("Calculator App")
        print('Usage: python main.py "<expression>"')
        print('Example: python main.py "3 + 5"')
        return

    # Join all arguments into a single expression string
    expression = " ".join(sys.argv[1:])

    try:
        # Evaluate the expression and render the result
        result = calculator.evaluate(expression)
        to_print = render(expression, result)
        print(to_print)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
