class CalculatorError(Exception):
    """Base calculator exception."""

class DivisionByZeroError(CalculatorError):
    """Raised when dividing by zero."""

class InvalidInputError(CalculatorError):
    """Raised on invalid user input."""