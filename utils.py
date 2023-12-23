# Questions have a prompt and an answer and a value
class Question:
    def __init__(self, prompt, answer, value=5):
        self.id = None  # unique identifier for each Question in database
        self.prompt = prompt
        self.answer = answer
        self.value = value


# Tossup Questions are worth 10 points and have bonus questions if answered correctly
class Tossup(Question):
    def __init__(self, prompt, answer, bonuses: list[Question]):
        super().__init__(prompt, answer)
        self.value = 10
        self.bonus = bonuses

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
    def __init__(self, rounds: dict[int, Round], teams: dict[int, Team]):
        self.rounds = rounds
        self.teams = teams

    def __str__(self):
        return f"Game: {self.rounds}"

    def __repr__(self):
        return f"Game: {self.rounds}"
