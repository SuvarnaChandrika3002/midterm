from dataclasses import dataclass
from typing import Any

@dataclass(frozen=True)
class Memento:
    state: Any