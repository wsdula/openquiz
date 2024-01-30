# this file contains the functions that control the game

import utils

test_questions = "test.json"
test_player = ["VillagerA", "VillagerB"]


def setup_game(filename: str = test_questions, players: list[str] = test_player):
    """
    This function sets up the game using the utils.py functions
    """
    questions = utils.get_questions_from_file(filename)
    members = [utils.build_player(name) for name in players]
    teams = [utils.Team("Team 1", members[0]), utils.Team("Team 2", members[1])]
    return utils.Game(teams, Round(questions))

def next_round():
    """
    This function takes the game to the next round
    """
    pass


def end_game():
    """
    This function ends the game
    """
    pass


def save_game():
    """
    This function saves the game
    """
    pass


def update_score():
    """
    This function updates the score
    """
    pass


def change_score():
    """
    This function changes the score
    """
    pass


def wrong_answer():
    """
    This function is called when the user chooses the wrong answer
    """
    pass


def correct_answer():
    """
    This function is called when the user chooses the correct answer
    """
    pass
