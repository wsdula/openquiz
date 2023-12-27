# Questions have a prompt and an answer and a value
class Question:
    def __init__(self, prompt, answer, value=5):
        self.id = None  # unique identifier for each Question in database
        self.prompt = prompt
        self.answer = answer
        self.value = value


# Tossup Questions are worth 10 points and have bonus questions if answered correctly
class Tossup:
    def __init__(self, faceoff: Question, bonuses: list[Question]):
        self.faceoff = faceoff
        self.bonus = bonuses
        self.value = (
            10  # FIXME: Faceoff has multiple values but there should only be one
        )

        tv = self.value
        for b in self.bonus:
            tv += b.value
            if tv > 30:
                raise ValueError(
                    "Total value of Tossup and bonuses cannot exceed 30 points"
                )


# rounds contain tossups and bonuses
class Round:
    def __init__(self, tossups: list[Tossup]):
        self.tossups = tossups
        self.bonuses = []
        for t in self.tossups:
            self.bonuses.extend(t.bonus)

    def __str__(self):
        return f"Round: {self.tossups}"

    def __repr__(self):
        return f"Round: {self.tossups}"


class Team:
    def __init__(self, name: str, players: list[str]):
        self.name = name
        self.players = players

    def __str__(self):
        return f"Team: {self.name}"

    def __repr__(self):
        return f"Team: {self.name}"


# Games contain rounds and are played by teams
class Game:
    """
    This class represents a game. It contains rounds and teams.
    """

    def __init__(self, rounds: dict[int, Round]):
        self.rounds = rounds

    def __str__(self):
        return f"Game: {self.rounds}"

    def __repr__(self):
        return f"Game: {self.rounds}"
