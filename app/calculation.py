from dataclasses import dataclass

@dataclass(frozen=True)
class Calculation:
    operation: str
    a: float
    b: float
    result: float

    def __repr__(self) -> str:
        return f"{self.operation}({self.a}, {self.b}) = {self.result}"