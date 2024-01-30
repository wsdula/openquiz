import controls

# import utils


# Below is the main game loop, it is called when the program is run
# It is also called when the user chooses to play again
# The game prints out questions and takes a yes or no to denote whether the player was correct
def gameLoop(game):
    while game.flag:
        for question in game.rounds.questions:
            print(question.prompt)
            while True:
                _ = input("Which team answered? (enter number): ")
                try:
                    team = game.teams[int(_) - 1]
                    player = controls.pick_player(team)
                    break
                except (IndexError, ValueError, TypeError):
                    print("Please enter a number that corresponds to a team")

            while True:
                answer = input("Was the answer correct? (y/n): ")
                if answer == "y":
                    controls.correct_answer(team, player, question)
                    break
                elif answer == "n":
                    controls.wrong_answer()
                    break
                else:
                    print("Please enter a valid input")

        game.flag = False

    print(f"The final score was {game.teams[0].score} to {game.teams[1].score}")
    answer = input("Play again? (y/n): ")
    if answer == "y":
        gameLoop(game)
    elif answer == "n":
        print("Thanks for playing!")
        exit()


if __name__ == "__main__":
    gameLoop(controls.setup_game())
