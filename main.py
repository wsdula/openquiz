# This application is a quiz game, where the user can choose a category and answer the questions.
# Each question has 1 correct answer.
# Each question is worth 10 points

# Importing the necessary modules
import tkinter as tk
import os
import sys
import time


window = tk.Tk()
greeting = tk.Label(text="Welcome to the Quiz Game!")
greeting.pack()

window.title("Quiz Game")
window.geometry("500x500")
window.mainloop()


# Questions have a prompt and an answer and a value
class question:
    def __init__(self, prompt, answer, value=5):
        self.id = None  # unique identifier for each question in database
        self.prompt = prompt
        self.answer = answer
        self.value = value


# Tossup questions are worth 10 points and have bonus questions if answered correctly
class tossup(question):
    def __init__(self, prompt, answer, bonuses: list[question]):
        super().__init__(prompt, answer)
        self.value = 10
        self.bonus = bonuses

        tv = self.value
        for b in self.bonus:
            tv += b.value
            if tv > 30:
                raise ValueError(
                    "Total value of tossup and bonuses cannot exceed 30 points"
                )
