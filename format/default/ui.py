import tkinter as tk
from tkinter import filedialog

import controls


class viewWindow:
    def __init__(self, qVar, scoreVar):
        top = tk.Toplevel()
        self.frame = tk.Frame(top)
        self.frame.pack()
        self.qVar = qVar
        self.scoreVar = scoreVar
        # question frame
        self.qFrame = tk.Frame(self.frame, bg="blue")
        self.qVar.set("Question goes here")
        self.qText = tk.Label(
            self.qFrame,
            textvariable=self.qVar,
            font=("Helvetica", 24),
            wraplength=1000,
            justify="center",
        )
        self.qFrame.pack(pady=20)
        self.qText.pack(pady=20)
        # score frame
        self.scoreFrame = tk.Frame(self.frame, bg="green")
        self.scoreVar.set("Score goes here")
        self.scoreText = tk.Label(
            self.scoreFrame, textvariable=self.scoreVar, font=("Helvetica", 24)
        ).grid(row=0, column=1)
        self.scoreFrame.pack(pady=20)


class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        self.parent = parent
        tk.Frame.__init__(self, self.parent)
        self.controller = controller
        self.qVar = tk.StringVar()
        self.scoreVar = tk.StringVar()
        self.file = ""
        self.createWidgets()

    def openView(self, qVar, scoreVar):
        self.view = viewWindow(qVar, scoreVar)

    def createWidgets(self):
        # game page frame
        self.startButton = tk.Button(
            self,
            text="Start Game",
            command=lambda: self.gameLoop(controls.setup_game(self.file)),
        )
        self.startButton.pack(pady=5, anchor="ne")
        # command for end game button is set in gameLoop
        self.endButton = tk.Button(self, text="End Game")
        self.endButton.pack(pady=5, anchor="ne")

        def uploadGame():
            self.file = filedialog.askopenfilename(
                initialdir="./",
                title="Select a game file",
                filetypes=[("JSON files", "*.json"), ("All files", "*.*")],
            )

        self.uploadButton = tk.Button(self, text="Upload Game", command=uploadGame)
        self.uploadButton.pack(pady=5, anchor="ne")
        exitbutton = tk.Button(
            self,
            text="Go to the start page",
            command=lambda: self.controller.show_frame("StartPage"),
        )
        exitbutton.pack(side=tk.BOTTOM, pady=11, anchor="e")

        # question frame
        self.qFrame = tk.Frame(self, bg="blue")
        self.qVar.set("Question goes here")
        self.qText = tk.Label(
            self.qFrame,
            textvariable=self.qVar,
            font=("Helvetica", 24),
            wraplength=1000,
            justify="center",
        )
        self.qFrame.pack(pady=20)
        self.qText.pack(pady=20)

        # score frame
        self.scoreFrame = tk.Frame(self, bg="green")
        self.scoreVar.set("Score goes here")
        self.scoreText = tk.Label(
            self.scoreFrame, textvariable=self.scoreVar, font=("Helvetica", 24)
        ).grid(row=0, column=1)
        self.left_correct_button = tk.Button(self.scoreFrame, text="Correct")
        self.left_correct_button.grid(row=1, column=0, pady=10)
        self.left_wrong_button = tk.Button(self.scoreFrame, text="Wrong")
        self.left_wrong_button.grid(row=2, column=0)
        self.right_correct_button = tk.Button(self.scoreFrame, text="Correct")
        self.right_correct_button.grid(row=1, column=2, pady=10)
        self.right_wrong_button = tk.Button(self.scoreFrame, text="Wrong")
        self.right_wrong_button.grid(row=2, column=2)
        self.scoreFrame.pack(pady=20)

    def gameLoop(self, game):
        while game.flag:
            team_count = len(game.teams)
            okVar = tk.IntVar()
            self.openView(qVar=self.qVar, scoreVar=self.scoreVar)

            def endGame():
                game.flag = False
                okVar.set(2)

            self.endButton.configure(command=lambda: endGame())
            for question in game.rounds.questions:
                self.left_correct_button.configure(
                    command=lambda: [
                        controls.correct_answer(
                            game.teams[0], game.teams[0].members[0], question
                        ),
                        okVar.set(1),
                    ]
                )
                self.left_wrong_button.configure(
                    command=lambda: [controls.wrong_answer(), okVar.set(1)]
                )
                self.right_correct_button.configure(
                    command=lambda: [
                        controls.correct_answer(
                            game.teams[1], game.teams[1].members[0], question
                        ),
                        okVar.set(1),
                    ]
                )
                self.right_wrong_button.configure(
                    command=lambda: [controls.wrong_answer(), okVar.set(1)]
                )
                self.qVar.set(question.prompt)
                # alternate between teams
                team = game.teams[game.rounds.questions.index(question) % team_count]
                # alternate between players
                player = team.members[
                    game.rounds.questions.index(question) % len(team.members)
                ]
                if game.rounds.questions.index(question) % team_count == 0:
                    self.scoreVar.set(
                        f"LEFT TEAM: {game.teams[0].score}  Right Team: {game.teams[1].score}"
                    )
                if game.rounds.questions.index(question) % team_count == 1:
                    self.scoreVar.set(
                        f"Left Team: {game.teams[0].score}  RIGHT TEAM: {game.teams[1].score}"
                    )
                self.left_wrong_button.wait_variable(okVar)
            self.scoreVar.set(
                f"Final Score \n Left Team: {game.teams[0].score}  Right Team: {game.teams[1].score}"
            )

            game.flag = False
