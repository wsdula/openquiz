from dataclasses import dataclass
from typing import List
from .player import Player


@dataclass
class Team:
    name: str
    members: List[Player]
    score: int = 0

    def __str__(self):
        return f"Team: {self.name}"

    def __repr__(self):
        return f"Team: {self.name}"
