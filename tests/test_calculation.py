from app.calculation import Calculation

def test_repr():
    c = Calculation("add", 2, 3, 5)
    assert repr(c) == "add(2, 3) = 5"


