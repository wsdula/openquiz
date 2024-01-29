# Questions have a prompt and an answer and a value
class Question:
    def __init__(self, prompt, answer, value=10, **kwargs):
        self.id = None  # unique identifier for each Question in database
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
    # TODO: Change to make use of Player class
    def __init__(self, name: str, members: list[Player], score: int = 0, **kwargs):
        self.name = name
        self.members = members
        self.score = score
        for k, v in kwargs.items():
            setattr(self, k, v)

    def __str__(self):
        return f"Team: {self.name}"

    def __repr__(self):
        return f"Team: {self.name}"

    def UpdateTeamScore(self):
        self.score = sum(member.score for member in self.members)


def get_questions_from_file(filename: str) -> list[Question]:
    """Reads questions from a file and returns a list of Question objects"""
    questions = []
    with open(filename, "r") as f:
        # FIXME: This is not the best way to read from a file
        for line in f:
            prompt, answer = line.split(";")
            questions.append(Question(prompt, answer))
    return questions


def create_player(name: str) -> Player:
    """Creates a Player object"""
    return Player(name)
