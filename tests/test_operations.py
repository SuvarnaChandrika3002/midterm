import math
from app.operations import (
    add, subtract, multiply, divide, power, root, modulus, int_divide, percent, abs_diff
)
import pytest
from app.exceptions import DivisionByZeroError

def test_add():        assert add(2, 3) == 5
def test_subtract():   assert subtract(5, 2) == 3
def test_multiply():   assert multiply(4, 3) == 12
def test_divide():     assert divide(10, 2) == 5
def test_divide_zero():
    with pytest.raises(DivisionByZeroError):
        divide(1, 0)

def test_power():      assert power(2, 5) == 32
def test_root():       assert root(25, 2) == 5
def test_modulus():    assert modulus(10, 3) == 1
def test_int_divide(): assert int_divide(9, 4) == 2
def test_percent():    assert percent(2, 8) == 25
def test_abs_diff():   assert abs_diff(10, 3) == 7