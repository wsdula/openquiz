from typing import List, Union


# Questions have a prompt and an answer and a value
class Question:
    def __init__(self, prompt, answer, value=10, **kwargs):
        # NOTE: Eventually this will be a unique identifier for each Question in database
        self.id = None
        self.prompt = prompt
        self.answer = answer
        self.value = value
        for k, v in kwargs.items():
            setattr(self, k, v)


class Player:
    # TODO: Redefine this class to be more useful
    def __init__(self, name: str, score: int = 0, **kwargs):
        self.name = name
        self.score = score
        for k, v in kwargs.items():
            setattr(self, k, v)


class Team:
    def __init__(
        self, name: str, members: Union[Player, List[Player]], score: int = 0, **kwargs
    ):
        self.name = name
        self.members = members
        self.score = score
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return f"Team: {self.name}"

    def __repr__(self):
        return f"Team: {self.name}"

    # NOTE: Opportunity for the strategy pattern???
    def UpdateTeamScore(self):
        if isinstance(self.members, list):
            self.score = sum(member.score for member in self.members)
        elif isinstance(self.members, Player):
            self.score = self.members.score
        else:
            raise TypeError("Team members must be a Player or a list of Players")


def get_questions_from_file(filename: str) -> list[Question]:
    """Reads questions from a file and returns a list of Question objects"""
    # NOTE This is a good place to use the strategy pattern
    # NOTE This will eventually be a paired with a database call
    questions = []
    if filename.endswith(".txt"):
        with open(filename, "r") as f:
            # FIXME: This is not the best way to read from a file
            for line in f:
                prompt, answer = line.split(";")
                questions.append(Question(prompt, answer))
    elif filename.endswith(".json"):
        with open(filename, "r") as f:
            import json

            g = json.load(f)
            for q in g["questions"]:
                questions.append(Question(**q))
    return questions


def create_player(name: str) -> Player:
    """Creates a Player object"""
    return Player(name)
