import os
from typing import List, Tuple, Optional
import pandas as pd

from .calculation import Calculation
from .calculator_config import HISTORY_FILE

class History:

    def __init__(self, filename: Optional[str] = None) -> None:
        self.filename = filename or HISTORY_FILE
        self._df = pd.DataFrame(columns=["operation", "a", "b", "result"])
        self._redo_stack: List[Tuple[str, float, float, float]] = []
        self._load_if_exists()

    def _load_if_exists(self) -> None:
        if os.path.exists(self.filename):
            self._df = pd.read_csv(self.filename)

    def save(self) -> None:
        parent = os.path.dirname(self.filename)
        if parent:
            os.makedirs(parent, exist_ok=True)
        self._df.to_csv(self.filename, index=False)

    def load(self) -> None:
        self._load_if_exists()

    def add(self, calc: Calculation) -> None:
        self._df = pd.concat(
            [
                self._df,
                pd.DataFrame(
                    [{
                        "operation": calc.operation,
                        "a": calc.a,
                        "b": calc.b,
                        "result": calc.result,
                    }]
                ),
            ],
            ignore_index=True,
        )
        self._redo_stack.clear()

    def clear(self) -> None:
        self._df = pd.DataFrame(columns=["operation", "a", "b", "result"])
        self._redo_stack.clear()

    def list(self) -> pd.DataFrame:
        return self._df.copy()

    def undo(self) -> str:
        if self._df.empty:
            return "Nothing to undo"
        last = self._df.iloc[-1]
        self._redo_stack.append((last["operation"], last["a"], last["b"], last["result"]))
        self._df = self._df.iloc[:-1].reset_index(drop=True)
        return "Undo successful"

    def redo(self) -> str:
        if not self._redo_stack:
            return "Nothing to redo"
        op, a, b, r = self._redo_stack.pop()
        self._df = pd.concat(
            [self._df, pd.DataFrame([{"operation": op, "a": a, "b": b, "result": r}])],
            ignore_index=True,
        )
        return "Redo successful"