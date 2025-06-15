"""
Rendering module for calculator results.

This module provides functions to format calculator expressions and results
into visually appealing text-based displays.
"""

from typing import Any, List


def render(expression: str, result: Any) -> str:
    """
    Render an expression and its result in a decorative box.

    Args:
        expression: The mathematical expression that was evaluated.
        result: The result of evaluating the expression.

    Returns:
        A string containing a box drawing with the expression and result.
    """
    # Convert integer-like floats to integers for cleaner display
    if isinstance(result, float) and result.is_integer():
        result_str = str(int(result))
    else:
        result_str = str(result)

    # Calculate box width based on the longest string plus padding
    box_width = max(len(expression), len(result_str)) + 4

    # Build the box line by line
    box: List[str] = []

    # Top border
    box.append("┌" + "─" * box_width + "┐")

    # Expression line
    box.append(
        "│" + " " * 2 + expression + " " * (box_width - len(expression) - 2) + "│"
    )

    # Empty line
    box.append("│" + " " * box_width + "│")

    # Equals sign line
    box.append("│" + " " * 2 + "=" + " " * (box_width - 3) + "│")

    # Empty line
    box.append("│" + " " * box_width + "│")

    # Result line
    box.append(
        "│" + " " * 2 + result_str + " " * (box_width - len(result_str) - 2) + "│"
    )

    # Bottom border
    box.append("└" + "─" * box_width + "┘")

    # Join all lines with newlines and return
    return "\n".join(box)
