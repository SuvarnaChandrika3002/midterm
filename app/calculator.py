from typing import Optional
from app.operations import OPERATIONS
from app.history import History
from app.calculation import Calculation
from app.input_validators import ensure_number, ensure_nonzero
from app.exceptions import CalculatorError
from app.logger import log
from app.calculator_config import PROMPT


class Calculator:
    def __init__(self, history: Optional[History] = None):
        self.history = history or History()

    def compute(self, op: str, a: float, b: float) -> float:
        if op not in OPERATIONS:
            raise CalculatorError(f"Unknown operation: {op}")

        if op in {"divide", "modulus", "int_divide", "percent"}:
            ensure_nonzero(b)

        result = OPERATIONS[op](a, b)
        self.history.add(Calculation(op, a, b, result))
        return result

    def undo(self) -> str:
        return self.history.undo()

    def redo(self) -> str:
        return self.history.redo()

    def save(self) -> None:
        self.history.save()

    def load(self) -> None:
        self.history.load()

    def list_history(self):
        return self.history.list()


def run_repl() -> None:
    calc = Calculator()

    help_text = (
        "\nAvailable Commands:\n"
        "  add | subtract | multiply | divide | power | root\n"
        "  modulus | int_divide | percent | abs_diff\n"
        "  history    → show history\n"
        "  clear      → clear history\n"
        "  undo / redo\n"
        "  save / load\n"
        "  help       → show this help\n"
        "  exit       → quit\n"
    )
    print(help_text)

    while True:
        try:
            raw = input(PROMPT).strip().lower()

            if raw in {"exit", "quit"}:
                print("Goodbye!")
                break

            match raw:
                case "help":
                    print(help_text)
                case "history":
                    print(calc.list_history())
                case "clear":
                    calc.history.clear()
                    print("History cleared.")
                case "undo":
                    print(calc.undo())
                case "redo":
                    print(calc.redo())
                case "save":
                    calc.save()
                    print("Saved.")
                case "load":
                    calc.load()
                    print("Loaded.")
                case op if op in OPERATIONS:
                    a = ensure_number(input("a = "))
                    b = ensure_number(input("b = "))
                    if op in {"divide", "modulus", "int_divide", "percent"}:
                        ensure_nonzero(b)
                    print(calc.compute(op, a, b))
                case _:
                    print("Unknown command. Type 'help'.")

        except CalculatorError as e:
            log.error(str(e))
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    run_repl()