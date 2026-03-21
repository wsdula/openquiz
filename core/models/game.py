from typing import List, Union
from .round import Round
from .team import Team


class Game:
    def __init__(self, teams: List[Team], rounds: List[Round], **kwargs):
        self.teams = teams
        self.rounds = rounds
        for k, v in kwargs.items():
            setattr(self, k, v)
