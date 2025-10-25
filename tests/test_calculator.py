import pytest
from app.calculator import Calculator
from app.exceptions import DivisionByZeroError
from app.history import History

def test_compute_add(tmp_path):
    h = History(filename=str(tmp_path / "h.csv"))
    c = Calculator(history=h)
    out = c.compute("add", 2, 3)
    assert out == 5
    assert len(c.list_history()) == 1

def test_compute_divide_by_zero(tmp_path):
    h = History(filename=str(tmp_path / "h.csv"))
    c = Calculator(history=h)
    with pytest.raises(DivisionByZeroError):
        c.compute("divide", 1, 0)

def test_undo_redo(tmp_path):
    h = History(filename=str(tmp_path / "h.csv"))
    c = Calculator(history=h)
    c.compute("multiply", 2, 5)
    assert c.undo() == "Undo successful"
    assert c.redo() == "Redo successful"