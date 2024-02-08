import tkinter as tk
import controls


class GamePage(tk.Frame):
    qVar = tk.StringVar()
    scoreVar = tk.StringVar()

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # game_label = tk.Label(self, text="Game in progress!", font=("Helvetica", 16))
        # game_label.pack(pady=20)
        # this is where the question will be displayed
        qFrame = tk.Frame(self, bg="blue")
        self.qVar.set("Question goes here")
        qText = tk.Label(qFrame, textvariable=self.qVar, font=("Helvetica", 16))
        qFrame.pack(pady=20)
        qText.pack(pady=20)

        scoreFrame = tk.Frame(self, bg="green")
        self.scoreVar.set("Score goes here")
        scoreText = tk.Label(
            scoreFrame, textvariable=self.scoreVar, font=("Helvetica", 16)
        )
        correct_button = tk.Button(scoreFrame, text="Correct")
        wrong_button = tk.Button(scoreFrame, text="Wrong")
        scoreFrame.pack(pady=20)
        scoreText.pack(pady=20)
        correct_button.pack(pady=10)
        wrong_button.pack(pady=10)

        button = tk.Button(
            self,
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"),
        )
        button.pack(pady=10, anchor="se")

        self.gameLoop(controls.setup_game())

    def gameLoop(self, game):
        while game.flag:
            for question in game.rounds.questions:
                self.qVar.set(question.prompt)
                # get result from correct_button or wrong_button and proceed accordingly
                # if correct_button: controls.correct_answer(), which updates the player and team score, then self.qVar.set(game.questions.next.prompt)
                # if wrong_button: controls.wrong_answer() then self.qVar.set(game.questions.next.prompt)
                # requires making a listener for each button, should not be housed in controls.py

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
