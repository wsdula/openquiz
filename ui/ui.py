import tkinter as tk
from tkinter import ttk

import core.utils.game_services as gs
from pathlib import Path
import importlib

MAIN_FONT_CHOICE = ("Helvetica", 16)

FORM_PATH = Path(__file__).parent.parent / "format"


class LabeledSpinbox(tk.Frame):
    def __init__(self, parent, label_text, **kwargs):
        super().__init__(parent)

        # Create and pack the label
        self.label = tk.Label(self, text=label_text)
        self.label.pack(side=tk.LEFT, padx=5)

        # Create and pack the spinbox
        self.spinbox = tk.Spinbox(self, **kwargs)
        self.spinbox.pack(side=tk.LEFT)

    def get(self):
        return self.spinbox.get()


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

        self.team_spinbox = LabeledSpinbox(
            self,
            label_text="# of teams:",
            from_=1,
            to=10,
            command=self.generate_textboxes,
        )
        self.team_spinbox.pack(pady=10)

        self.player_spinbox = LabeledSpinbox(
            self,
            label_text="# of players:",
            from_=1,
            to=10,
            command=self.generate_textboxes,
        )
        self.player_spinbox.pack(pady=10)

        self.playername_frame = ttk.Frame(self)
        self.playername_frame.pack(pady=10)

        self.combo_text = tk.StringVar()
        self.cb = ttk.Combobox(
            self, textvariable=self.combo_text, values=gs.list_formats(FORM_PATH)
        )
        self.cb.set("Pick a format")
        self.cb.pack()

        self.cb.bind("<<ComboboxSelected>>", self.on_format_change)

        self.format_options_container = tk.Frame(self)
        self.format_options_container.pack(pady=10)

    def on_format_change(self, event):
        format_name = self.combo_text.get()
        self.load_format_setup(format_name)

    def load_format_setup(self, format_name):
        # Destroy old frame
        if self.format_options_container is not None:
            self.format_options_container.destroy()

        module = importlib.import_module(f"format.{format_name}.ui")

        setup_class = getattr(module, "SetupFrame")

        self.format_options_container = setup_class(self)
        self.format_options_container.pack(pady=10)

    def generate_textboxes(self) -> None:
        try:
            team_count = int(self.team_spinbox.get())
            player_count = int(self.player_spinbox.get())
        except ValueError:
            team_count = 2
            player_count = 1

        for widget in self.playername_frame.winfo_children():
            widget.destroy()

        for i in range(team_count):
            for j in range(player_count):
                label = tk.Label(
                    self.playername_frame, text=f"Team {i+1}, Player {j+1}:"
                )
                label.pack(side="top", anchor="w")
                entry = tk.Entry(self.playername_frame)
                entry.pack(side="top", fill="x", pady=2)

        # TODO: Dynamically import gamePage object from chosen format
