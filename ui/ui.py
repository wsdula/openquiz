import tkinter as tk
from tkinter import ttk

# from format.default.ui import GamePage
import core.utils.game_services as gs
from pathlib import Path

# import utils

MAIN_FONT_CHOICE = ("Helvetica", 16)

FORM_PATH = Path(__file__).parent.parent / "format"


class App(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Quiz Game")
        self.geometry("500x500")
        container = tk.Frame(self)
        container.config(bg="skyblue")

        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, GameSetupPage):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame("StartPage")

    def show_frame(self, page_name):
        """Show a frame for the given page name"""
        frame = self.frames[page_name]
        frame.tkraise()

    def close_out(self):
        self.destroy()


class StartPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Welcome to the Quiz Game!", font=MAIN_FONT_CHOICE)
        label.pack(side="top", fill="x", pady=20)

        button1 = tk.Button(
            self,
            text="Start Game",
            command=lambda: controller.show_frame("GameSetupPage"),
        )

        button4 = tk.Button(self, text="Exit", command=lambda: controller.close_out())
        button1.pack(pady=10)

        button4.pack(pady=10)


class GameSetupPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        label = tk.Label(self, text="Setup your game", font=MAIN_FONT_CHOICE)
        label.pack(side="top", fill="x", pady=20)

        cb = ttk.Combobox(self, values=gs.list_formats(FORM_PATH))
        cb.set("Pick a format")
        cb.pack()

        team_spin_val = tk.IntVar(value=2)  # 2 teams by default
        team_spinbox = tk.Spinbox(
            self,
            from_=1,
            to=10,
            width=5,
            textvariable=team_spin_val,
        )
        team_spinbox.pack(pady=10)

        player_spin_val = tk.IntVar(value=1)  # 2 players by default
        player_spinbox = tk.Spinbox(
            self,
            from_=1,
            to=10,
            width=5,
            textvariable=player_spin_val,
        )
        player_spinbox.pack(pady=10)

        # TODO: Dynamically import gamePage object from chosen format
        # TODO: Create Text Fields/Buttons to get game information
