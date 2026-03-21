import tkinter as tk

from core.utils.models import Game
import core.utils.game_services as gs

FONT_CHOICE = ("Helvetica", 16)


class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.qVar = tk.StringVar()
        self.scoreVar = tk.StringVar()
        self.createWidgets()

    def createWidgets(self):
        controller = self.controller

        # Question Frame Definition
        self.qFrame = tk.Frame(self, bg="blue")
        self.qVar.set("Question goes here")
        self.qText = tk.Label(self.qFrame, textvariable=self.qVar, font=FONT_CHOICE)
        self.qFrame.pack(pady=20)
        self.qText.pack(pady=20)

        # Score Frame Definition
        self.scoreFrame = tk.Frame(self, bg="green")
        self.scoreVar.set("Score goes here")
        self.scoreText = tk.Label(
            self.scoreFrame, textvariable=self.scoreVar, font=FONT_CHOICE
        )
        self.correct_button = tk.Button(self.scoreFrame, text="Correct")
        self.wrong_button = tk.Button(self.scoreFrame, text="Wrong")
        self.scoreFrame.pack(pady=20)
        self.scoreText.pack(pady=20)
        self.correct_button.pack(pady=10)
        self.wrong_button.pack(pady=10)

        # Exit Button
        exitbutton = tk.Button(
            self,
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"),
        )
        exitbutton.pack(pady=11, anchor="se")


def gameLoop(page: GamePage, game: Game):
    while True:
        team_count = len(game.teams)
        for rd in game.rounds:
            for i, q in enumerate(rd.questions):
                okVar = tk.IntVar()
                page.qVar.set(q.prompt)

                # Alternate between teams
                team = game.teams[i % team_count]

                # Alternate between players
                player = team.members[i % len(team.members)]
                page.correct_button.configure(
                    command=lambda: [
                        gs.correct_answer(team, player, q),
                        okVar.set(1),
                    ]
                )
                page.wrong_button.configure(
                    command=lambda: [gs.wrong_answer(), okVar.set(1)]
                )
                page.correct_button.wait_variable(okVar)

        break
