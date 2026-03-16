# this file contains the functions that control the game
from models.player import Player
from models.team import Team
from models.game import Game
from models.round import Round
from models.question import Question
from typing import List

test_questions = "test.json"
test_player = ["VillagerA", "VillagerB"]


def build_player(name: str) -> Player:
    """Builds a Player object"""
    return Player(name)


def build_team(members: List[str], name: str | None) -> Team:
    """Builds a Team object"""
    players = [build_player(p) for p in members]
    if name is None:
        name = members[0]
    return Team(members=players, name=name)


def update_player_score(p: Player, v: int) -> None:
    p.score += v


def update_team_score(t: Team) -> None:
    t.score = sum(m.score for m in t.members)


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
    elif filename.endswith(".json"):
        with open(filename, "r") as f:
            import json

            g = json.load(f)
            for q in g["questions"]:
                questions.append(q)

    result = [Question(q["prompt"], q["answer"]) for q in questions]
    return result


def setup_game(filename: str = test_questions, players: list[str] = test_player):
    """
    This function sets up the game using the py functions
    """
    questions = get_questions_from_file(filename)
    members = [build_player(name) for name in players]
    teamList = [Team("Team 1", [members[0]]), Team("Team 2", [members[1]])]
    return Game(teams=teamList, rounds=Round(questions), flag=True)


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
