# This application is a quiz game, where the user can choose a category and answer the questions.
# Each question has 1 correct answer.
# Each question is worth 10 points

# Importing the necessary modules
import tkinter as tk
# import utils

# root = tk.Tk()
# root.title("Quiz Game")
# root.geometry("500x500")
# # root.config(bg="skyblue")
#
# greeting = tk.Label(text="Welcome to the Quiz Game!")
# greeting.pack()
#
# root.mainloop()

def start_game():
  game_window = tk.Toplevel(root)
  game_window.title("Game Window")
  
  # Add your game logic here
  game_label = tk.Label(game_window, text="Game in progress!", font=("Helvetica", 16))
  game_label.pack(pady=20)

def exit_game():
  root.destroy()

# Create the main window
root = tk.Tk()
root.title("Welcome to the Game")

# Create a label for the welcome message
welcome_label = tk.Label(root, text="Welcome to the Game!", font=("Helvetica", 16))
welcome_label.pack(pady=20)

# Create a button to start the game
start_button = tk.Button(root, text="Start Game", command=start_game)
start_button.pack(pady=10)

# Create a button to exit the game
exit_button = tk.Button(root, text="Exit", command=exit_game)
exit_button.pack(pady=10)

# Run the main loop
root.mainloop()
