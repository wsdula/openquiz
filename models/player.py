from dataclasses import dataclass


@dataclass
class Player:
    name: str
    score: int = 0
