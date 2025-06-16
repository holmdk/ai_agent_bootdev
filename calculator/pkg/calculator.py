from typing import Callable, Dict, List, Optional


class Calculator:
    """
    A calculator that evaluates mathematical expressions using infix notation.

    Supports basic arithmetic operations (+, -, *, /) with proper operator precedence.
    """

    def __init__(self) -> None:
        """Initialize the calculator with supported operators and their precedence."""
        # Dictionary mapping operators to their implementation functions
        self.operators: Dict[str, Callable[[float, float], float]] = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }

        # Dictionary defining operator precedence (higher number = higher precedence)
        self.precedence: Dict[str, int] = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    def evaluate(self, expression: str) -> Optional[float]:
        """
        Evaluate a mathematical expression and return the result.

        Args:
            expression: A string containing a mathematical expression in infix notation.
                        Example: "3 + 4 * 2"

        Returns:
            The result of the expression as a float, or None if the expression is empty.

        Raises:
            ValueError: If the expression contains invalid tokens or is malformed.
        """
        # Handle empty expressions
        if not expression or expression.isspace():
            return None

        # Split the expression into tokens
        tokens = expression.strip().split()

        # Evaluate the infix expression
        return self._evaluate_infix(tokens)

    def _evaluate_infix(self, tokens: List[str]) -> float:
        """
        Evaluate an infix expression using the shunting-yard algorithm.

        Args:
            tokens: A list of tokens (numbers and operators) from the expression.

        Returns:
            The result of evaluating the expression.

        Raises:
            ValueError: If the expression is invalid or contains unsupported tokens.
        """
        values: List[float] = []
        operators: List[str] = []

        for token in tokens:
            if token == '(':
                operators.append(token)
            elif token == ')':
                while operators and operators[-1] != '(':
                    self._apply_operator(operators, values)
                if not operators:
                    raise ValueError("Unmatched ')'")
                operators.pop()  # Remove the '('
            elif token in self.operators:
                # Process operators according to precedence
                while (
                    operators
                    and operators[-1] != '('
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            else:
                # Try to convert token to a number
                try:
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        # Process any remaining operators
        while operators:
            if operators[-1] == '(':
                raise ValueError("Unmatched '('")
            self._apply_operator(operators, values)

        # If we don't have exactly one value left, the expression was invalid
        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    def _apply_operator(self, operators: List[str], values: List[float]) -> None:
        """
        Apply an operator to the top values in the values stack.

        Args:
            operators: Stack of operators.
            values: Stack of values.

        Raises:
            ValueError: If there are not enough operands for the operator.
        """
        if not operators:
            return

        # Get the operator to apply
        operator = operators.pop()

        # Check if we have enough operands
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        # Pop the operands (in reverse order)
        b = values.pop()
        a = values.pop()

        # Apply the operator and push the result back onto the values stack
        values.append(self.operators[operator](a, b))
