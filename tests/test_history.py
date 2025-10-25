import pandas as pd
from app.history import History
from app.calculation import Calculation

def test_add_and_list(tmp_path):
    path = tmp_path / "hist.csv"
    h = History(filename=str(path))
    h.add(Calculation("add", 2, 3, 5))
    df = h.list()
    assert len(df) == 1
    assert df.iloc[0]["operation"] == "add"

def test_save_and_load(tmp_path):
    path = tmp_path / "hist.csv"
    h = History(filename=str(path))
    h.add(Calculation("mul", 2, 4, 8))
    h.save()

    h2 = History(filename=str(path))
    h2.load()
    df = h2.list()
    assert len(df) == 1
    assert float(df.iloc[0]["result"]) == 8

def test_undo_redo(tmp_path):
    path = tmp_path / "hist.csv"
    h = History(filename=str(path))
    h.add(Calculation("add", 1, 1, 2))
    assert h.undo() == "Undo successful"
    assert len(h.list()) == 0
    assert h.redo() == "Redo successful"
    assert len(h.list()) == 1

def test_clear(tmp_path):
    path = tmp_path / "hist.csv"
    h = History(filename=str(path))
    h.add(Calculation("add", 1, 1, 2))
    h.clear()
    assert len(h.list()) == 0