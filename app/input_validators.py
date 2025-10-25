from .exceptions import InvalidInputError

def ensure_number(value: str) -> float:
    try:
        return float(value)
    except Exception as exc:
        raise InvalidInputError("Input must be a number.") from exc

def ensure_nonzero(value: float) -> float:
    if value == 0:
        from .exceptions import DivisionByZeroError
        raise DivisionByZeroError("Cannot divide by zero.")
    return value


