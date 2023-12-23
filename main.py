# This application is a quiz game, where the user can choose a category and answer the questions.
# Each question has 1 correct answer.
# Each question is worth 10 points

# Importing the necessary modules
import tkinter as tk
import os
import sys
import time
import utils

window = tk.Tk()
greeting = tk.Label(text="Welcome to the Quiz Game!")
greeting.pack()

window.title("Quiz Game")
window.geometry("500x500")
window.mainloop()
