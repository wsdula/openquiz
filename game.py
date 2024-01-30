import controls

#Below is the main game loop, it is called when the program is run
#It is also called when the user chooses to play again
#The game prints out questions and takes a yes or no to denote whether the player was correct
def gameLoop(game):
    while game.flag:
        for question in game.rounds.questions:
            print(question.prompt)
            answer = input("Was the answer correct? (y/n): ")
            if answer == "y":
                controls.correct_answer()
            elif answer == "n":
                controls.wrong_answer()
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
