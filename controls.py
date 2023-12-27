# this file contains the functions that control the game
# it also describes the data structure that keeps track of the game state

import utils
import json
import numpy as np


def make_game(input_file) -> utils.Game:
    """
    This function takes questions and turns them into a game object
    """
    with open(input_file) as f:
        questions = []
        data = json.load(f)

        for i in data["questions"]:
            q = utils.Question(i["prompt"], i["answer"])
            questions.append(q)

        f.close()

    t = [
        utils.Tossup(faceoff=x[0], bonuses=x[1:]) for x in np.array_split(questions, 3)
    ]
    r = {i: utils.Round(tossups=[t[i]]) for i in range(len(t))}
    g = utils.Game(r)

    return g


def start_game():
    """
    This function starts the game
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
