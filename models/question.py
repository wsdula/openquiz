from dataclasses import dataclass
from typing import List, Optional


@dataclass(frozen=True)
class Question:
    prompt: str
    answer: str
    value: int
    category: Optional[str] = None
    wrong_answers: Optional[List[str]] = None
