from dataclasses import dataclass, field
from typing import List
from .question import Question


@dataclass
class Round:
    questions: List[Question] = field(default_factory=list)
