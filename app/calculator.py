from typing import Optional
from app.operations import OPERATIONS
from app.history import History
from app.calculation import Calculation
from app.input_validators import ensure_number, ensure_nonzero
from app.exceptions import CalculatorError
from app.logger import log
from app.calculator_config import PROMPT
from app.logging_observer import LoggingObserver
from app.autosave_observer import AutoSaveObserver


class Calculator:
    def __init__(self, history: Optional[History] = None):
        self.history = history or History()
        self.observers = []
        # Register built-in observers
        self.register_observer(LoggingObserver())
        self.register_observer(AutoSaveObserver(self.history))

    def register_observer(self, observer):
        self.observers.append(observer)

    def notify_observers(self, calculation: Calculation):
        for observer in self.observers:
            observer.update(calculation)

    def compute(self, op: str, a: float, b: float) -> float:
        if op not in OPERATIONS:
            raise CalculatorError(f"Unknown operation: {op}")

        if op in {"divide", "modulus", "int_divide", "percent"}:
            ensure_nonzero(b)

        result = OPERATIONS[op](a, b)
        calc_obj = Calculation(op, a, b, result)
        self.history.add(calc_obj)

        # NEW: notify all observers about the new calculation
        self.notify_observers(calc_obj)

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

            elif raw == "help":
                print(help_text)

            elif raw == "history":
                print(calc.list_history())

            elif raw == "clear":
                calc.history.clear()
                print("History cleared.")

            elif raw == "undo":
                print(calc.undo())

            elif raw == "redo":
                print(calc.redo())

            elif raw == "save":
                calc.save()
                print("Saved.")

            elif raw == "load":
                calc.load()
                print("Loaded.")

            elif raw in OPERATIONS:
                a = ensure_number(input("a = "))
                b = ensure_number(input("b = "))
                if raw in {"divide", "modulus", "int_divide", "percent"}:
                    ensure_nonzero(b)
                print(calc.compute(raw, a, b))

            else:
                print("Unknown command. Type 'help'.")

        except CalculatorError as e:
            log.error(str(e))
            print(f"Error: {e}")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    run_repl()