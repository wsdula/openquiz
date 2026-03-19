# this file contains the functions that control the game
from models.player import Player
from models.team import Team
from models.game import Game
from models.round import Round
from models.question import Question
from typing import List

test_questions = "../tests/test.json"
test_player = ["VillagerA", "VillagerB"]


def _build_player(name: str) -> Player:
    """Builds a Player object"""
    return Player(name)


def build_team(members: List[str], name: str | None) -> Team:
    """Builds a Team object"""
    players = [_build_player(p) for p in members]
    if name is None:
        name = members[0]
    return Team(members=players, name=name)


def build_game(teams: List[Team], rounds: List[Round], **kwargs) -> Game:
    """
    This function builds a Game object from provided Team and Round objects.
    """
    return Game(teams=teams, rounds=rounds, **kwargs)


def update_player_score(p: Player, v: int) -> Player:
    p.score += v
    return p


def update_team_score(t: Team) -> Team:
    t.score = sum(m.score for m in t.members)
    return t


def get_questions_from_file(filename: str) -> List[Question]:
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
    if filename.endswith(".json"):
        with open(filename, "r") as f:
            import json

            g = json.load(f)
            for q in g["questions"]:
                questions.append(q)

    result = [Question(q["prompt"], q["answer"]) for q in questions]
    return result


def wrong_answer():
    """
    This function is called when the user chooses the wrong answer
    Default behavior is to do nothing
    """
    pass


def correct_answer(team: Team, player: Player, question: Question):
    """
    This function is called when the user chooses the correct answer
    """
    update_player_score(player, question.value)
    update_team_score(team)


def save_game():
    """
    This function saves the game
    """
    pass


def change_score():
    """
    This function changes the score
    """
    pass
