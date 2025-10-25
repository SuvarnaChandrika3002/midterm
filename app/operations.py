from typing import Callable, Dict
from .exceptions import DivisionByZeroError

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return a / b

def power(a: float, b: float) -> float:
    return a ** b

def root(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Cannot take 0-th root.")
    return a ** (1.0 / b)

def modulus(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Cannot modulus by zero.")
    return a % b

def int_divide(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return a // b

def percent(a: float, b: float) -> float:
    if b == 0:
        raise DivisionByZeroError("Cannot divide by zero.")
    return (a / b) * 100.0

def abs_diff(a: float, b: float) -> float:
    return abs(a - b)

OPERATIONS: Dict[str, Callable[[float, float], float]] = {
    "add": add,
    "subtract": subtract,
    "multiply": multiply,
    "divide": divide,
    "power": power,
    "root": root,
    "modulus": modulus,
    "int_divide": int_divide,
    "percent": percent,
    "abs_diff": abs_diff,
}