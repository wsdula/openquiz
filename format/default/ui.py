import tkinter as tk

import controls


class GamePage(tk.Frame):
    def __init__(self, parent: tk.Frame, controller: tk.Frame) -> None:
        tk.Frame.__init__(self, parent)
        self._controller = controller
        self.qVar = tk.StringVar()
        self.scoreVar = tk.StringVar()
        self.createWidgets()
        self.gameLoop(controls.setup_game())

    def createWidgets(self):
        controller = self._controller
        self.qFrame = tk.Frame(self, bg="blue")
        self.qVar.set("Question goes here")
        self.qText = tk.Label(
            self.qFrame, textvariable=self.qVar, font=("Helvetica", 16)
        )
        self.qFrame.pack(pady=20)
        self.qText.pack(pady=20)
        self.scoreFrame = tk.Frame(self, bg="green")
        self.scoreVar.set("Score goes here")
        self.scoreText = tk.Label(
            self.scoreFrame, textvariable=self.scoreVar, font=("Helvetica", 16)
        )
        self.correct_button = tk.Button(self.scoreFrame, text="Correct")
        self.wrong_button = tk.Button(self.scoreFrame, text="Wrong")
        self.scoreFrame.pack(pady=20)
        self.scoreText.pack(pady=20)
        self.correct_button.pack(pady=10)
        self.wrong_button.pack(pady=10)
        button = tk.Button(
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"),
        )
        button.pack(pady=10, anchor="se")

    def gameLoop(self, game):
        while game.flag:
            team_count = len(game.teams)
            for question in game.rounds.questions:
                okVar = tk.IntVar()
                self.qVar.set(question.prompt)
                # alternate between teams
                team = game.teams[game.rounds.questions.index(question) % team_count]
                # alternate between players
                player = team.players[
                    game.rounds.questions.index(question) % len(team.players)
                ]
                self.correct_button.configure(
                    command=lambda: [
                        controls.correct_answer(game, player, team),
                        okVar.set(1),
                    ]
                )
                self.wrong_button.configure(
                    command=lambda: [controls.wrong_answer(), okVar.set(1)]
                )
                self.correct_button.wait_variable(okVar)

            game.flag = False
