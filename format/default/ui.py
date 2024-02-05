import tkinter as tk
import controls


class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # game_label = tk.Label(self, text="Game in progress!", font=("Helvetica", 16))
        # game_label.pack(pady=20)
        # this is where the question will be displayed
        qFrame = tk.Frame(self)
        qText = tk.Label(qFrame, text="Question goes here", font=("Helvetica", 16))
        qText.pack(pady=20)

        scoreFrame = tk.Frame(self)
        scoreText = tk.Label(scoreFrame, text="Score goes here", font=("Helvetica", 16))
        correct_button = tk.Button(scoreFrame, text="Correct")
        wrong_button = tk.Button(scoreFrame, text="Wrong")
        scoreText.pack(pady=20)
        correct_button.pack(pady=10)
        wrong_button.pack(pady=10)

        button = tk.Button(
            self,
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"),
        )
        button.pack(pady=10, anchor="se")

        set_game = controls.setup_game()
        self.gameLoop(set_game)

    def gameLoop(self, game):
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
            GamePage.gameLoop(self, game)
        elif answer == "n":
            print("Thanks for playing!")
