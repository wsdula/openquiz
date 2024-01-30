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
    teamList = [utils.Team("Team 1", members[0]), utils.Team("Team 2", members[1])]
    return utils.Game(teams=teamList, rounds=utils.Round(questions), flag=True)


def wrong_answer():
    """
    This function is called when the user chooses the wrong answer
    Default behavior is to do nothing
    """
    pass


def correct_answer(team: utils.Team, player: utils.Player, question: utils.Question):
    """
    This function is called when the user chooses the correct answer
    """
    player.score += question.value
    team.UpdateTeamScore()


def pick_player(team):
    if isinstance(team.members, list):
        while True:
            try:
                _ = input("Which player answered? (enter number): ")
                player = team.members[int(_) - 1]
                break
            except (IndexError,ValueError,TypeError):
                print("Please enter a number that corresponds to a player")

    else:
        player = team.members
    return player

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
