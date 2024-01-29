# Questions have a prompt and an answer and a value
class Question:
    def __init__(self, prompt, answer, value=10):
        self.id = None  # unique identifier for each Question in database
        self.prompt = prompt
        self.answer = answer
        self.value = value


class Player:
    # TODO: Redefine this class to be more useful
    def __init__(self, name: str, team: str):
        self.name = name
        self.team = team


class Team:
    # TODO: Change to make use of Player class
    def __init__(self, name: str, players: list[str]):
        self.name = name
        self.players = players

    def __str__(self):
        return f"Team: {self.name}"

    def __repr__(self):
        return f"Team: {self.name}"


def get_questions_from_file(filename: str) -> list[Question]:
    """Reads questions from a file and returns a list of Question objects"""
    questions = []
    with open(filename, "r") as f:
        for line in f:
            prompt, answer = line.split(";")
            questions.append(Question(prompt, answer))
    return questions


