# this file contains the functions that control the game

import utils

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


def get_questions_from_file(filename: str) -> List[dict]:
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
    return questions


def setup_game(filename: str = test_questions, players: list[str] = test_player):
    """
    This function sets up the game using the utils.py functions
    """
    questions = utils.get_questions_from_file(filename)
    members = [utils.build_player(name) for name in players]
    teamList = [utils.Team("Team 1", [members[0]]), utils.Team("Team 2", [members[1]])]
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
            except (IndexError, ValueError, TypeError):
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
