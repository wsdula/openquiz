from typing import List, Union, Optional
from dataclasses import dataclass, field


@dataclass
class Player:
    name: str
    score: int = 0


@dataclass
class Team:
    name: str
    members: List[Player]
    score: int = 0

    def __str__(self):
        return f"Team: {self.name}"

    def __repr__(self):
        return f"Team: {self.name}"

    # NOTE: Opportunity for the strategy pattern???
    # TODO: Add Update Score function elsewhere


# Questions have a prompt and an answer and a value
@dataclass(frozen=True)
class Question:
    prompt: str
    answer: str
    value: int
    category: Optional[str] = None
    wrong_answers: Optional[List[str]] = None


@dataclass
class Round:
    questions: List[Question] = field(default_factory=list)


class Game:
    def __init__(self, teams: List[Team], rounds: Union[Round, List[Round]], **kwargs):
        self.teams = teams
        self.rounds = rounds
        for k, v in kwargs.items():
            setattr(self, k, v)


def build_player(name: str) -> Player:
    """Builds a Player object"""
    return Player(name)


def build_team(members: List[str], name: str | None) -> Team:
    """Builds a Team object"""
    players = [build_player(p) for p in members]
    if name is None:
        name = members[0]
    return Team(members=players, name=name)


def get_questions_from_file(filename: str) -> List[dict]:
    """Reads questions from a file and returns a list of questions formatted in a dict"""
    # NOTE This is a good place to use the strategy pattern
    # NOTE The actual question object should be created in the format!!!
    questions = []
    if filename.endswith(".txt"):
        with open(filename, "r") as f:
            # FIXME: This is not the best way to read from a file
            for line in f:
                prompt, answer = line.split(";")
                questions.append({prompt: prompt, answer: answer})
    elif filename.endswith(".json"):
        with open(filename, "r") as f:
            import json

            g = json.load(f)
            for q in g["questions"]:
                questions.append(q)
    return questions
