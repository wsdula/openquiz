import tkinter as tk


class GamePage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Add game logic here
        game_label = tk.Label(self, text="Game in progress!", font=("Helvetica", 16))
        game_label.pack(pady=20)
        button = tk.Button(
            self,
            text="Go to the start page",
            command=lambda: controller.show_frame("StartPage"),
        )
        button.pack(pady=10, anchor="se")
