from typing import List, Union


# Questions have a prompt and an answer and a value
class Question:
    def __init__(self, prompt, answer, value: int = 10, **kwargs):
        # NOTE: Eventually this will be a unique identifier for each Question in database
        self.id = None
        self.prompt = prompt
        self.answer = answer
        self.value = value
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        if value < 0:
            raise ValueError("Value cannot be less than 0")
        self._value = value


class Player:
    # TODO: Redefine this class to be more useful
    def __init__(self, name: str, score: int = 0, **kwargs):
        self.name = name
        self.score = score
        for k, v in kwargs.items():
            setattr(self, k, v)

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score < 0:
            raise ValueError("Score cannot be less than 0")
        self._score = score


class Team:
    def __init__(self, name: str, members: List[Player], score: int = 0, **kwargs):
        self.name = name
        self.members = members
        self.score = score
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return f"Team: {self.name}"

    def __repr__(self):
        return f"Team: {self.name}"

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score < 0:
            raise ValueError("Score cannot be less than 0")
        self._score = score

    # NOTE: Opportunity for the strategy pattern???
    def UpdateTeamScore(self):
        self.score = sum(member.score for member in self.members)


class Round:
    def __init__(self, questions: List[Question], **kwargs):
        self.questions = questions
        for k, v in kwargs.items():
            setattr(self, k, v)


class Game:
    def __init__(self, teams: List[Team], rounds: Union[Round, List[Round]], **kwargs):
        self.teams = teams
        self.rounds = rounds
        for k, v in kwargs.items():
            setattr(self, k, v)


def get_questions_from_file(filename: str) -> list[Question]:
    """Reads questions from a file and returns a list of Question objects"""
    # NOTE This is a good place to use the strategy pattern
    # NOTE This will eventually be a paired with a database call
    questions = []
    if filename.endswith(".txt"):
        questions = _questions_from_txt(filename)
    elif filename.endswith(".xlsx"):
        questions = _questions_from_xlsx(filename)
    elif filename.endswith(".json"):
        questions = _questions_from_json(filename)
    return questions


def _questions_from_txt(filename: str) -> list[Question]:
    with open(filename, "r") as f:
        # FIXME: This is not the best way to read from a file
        questions = []
        for line in f:
            prompt, answer = line.split(";")
            questions.append(Question(prompt, answer))
        return questions


def _questions_from_xlsx(filename: str) -> list[Question]:
    import pandas as pd

    questions = []
    df = pd.read_excel(filename)
    for _, row in df.iterrows():
        questions.append(Question(row["prompt"], row["answer"], row["value"]))
    return questions


def _questions_from_json(filename: str) -> list[Question]:
    with open(filename, "r") as f:
        import json

        questions = []
        g = json.load(f)
        for q in g["questions"]:
            questions.append(Question(**q))
        return questions


def build_player(name: str) -> Player:
    """Builds a Player object"""
    return Player(name)
