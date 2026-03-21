from dataclasses import dataclass, field
from typing import Optional


@dataclass
class Player:
    name: str
    score: int = 0


@dataclass(frozen=True)
class Question:
    prompt: str
    answer: str
    value: int = 10
    category: Optional[str] = None
    wrong_answers: Optional[list[str]] = None


@dataclass
class Round:
    questions: list[Question] = field(default_factory=list)


@dataclass
class Team:
    name: str
    members: list[Player]
    score: int = 0

    def __str__(self):
        return f"Team: {self.name}"

    def __repr__(self):
        return f"Team: {self.name}"


class Game:
    def __init__(self, teams: list[Team], rounds: list[Round], **kwargs):
        self.teams = teams
        self.rounds = rounds
        for k, v in kwargs.items():
            setattr(self, k, v)
