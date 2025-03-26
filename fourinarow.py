import tkinter as tk
from tkinter import messagebox
import random

def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(4):
        if all(board[row][col] == player for row in range(4)):
            return True

    if all(board[i][i] == player for i in range(4)): # top-left to bottom-right
        return True
    if all(board[i][3-i] == player for i in range(4)): #top-right to bottom-left
        return True

    return False # false if no win

def is_full(board): # A full board means the game ends in a draw if no winner is found.
    return all(cell != ' ' for row in board for cell in row)

def bot_move():
    available_moves = [(row, col) for row in range(4) for col in range(4) if board[row][col] == ' ']
    if available_moves:
        row, col = random.choice(available_moves)
        board[row][col] = 'O'
        buttons[row][col].config(text='O', fg='black', font=('normal', 40, 'bold'))

        if check_winner(board, 'O'):
            popup("Bot wins!")
        elif is_full(board):
            popup("The game is a draw!")

def on_click(row, col):
    global current_player

    if board[row][col] == ' ':
        board[row][col] = current_player
        color = 'red' if current_player == 'X' else 'black'
        buttons[row][col].config(text=current_player, fg=color, font=('normal', 40, 'bold'))

        if check_winner(board, current_player):
            popup(f"Player {current_player} wins!")
        elif is_full(board):
            popup("The game is a draw!")
        else:
            current_player = 'O' if current_player == 'X' else 'X'
            if current_player == 'O':
                window.after(1000, bot_move) # time taken by the bot
                current_player = 'X' # switch to x

def popup(message):
    global popup
    popup = tk.Toplevel()
    popup.title("Game Over")
    label = tk.Label(popup, text=message, font=("Arial", 20), padx=20, pady=20)
    label.pack(side="top", fill="x")
    button = tk.Button(popup, text="Restart Game", font=("Arial", 15), command=restart_game, padx=10, pady=10)
    button.pack(pady=10)
    popup.grab_set()
    popup.transient(window)
    popup.geometry("300x150")
    popup.mainloop()

def restart_game():
    global current_player, board, popup
    popup.destroy()  # Close the popup window
    current_player = 'X'
    board = [[' ' for _ in range(4)] for _ in range(4)]
    for row in range(4):
        for col in range(4):
            buttons[row][col].config(text=' ', state=tk.NORMAL)

def create_board():
    for row in range(4):
        window.grid_rowconfigure(row, weight=1)
        for col in range(4):
            window.grid_columnconfigure(col, weight=1)
            button = tk.Button(window, text=" ", font=('normal', 40), width=5, height=2,
                               command=lambda row=row, col=col: on_click(row, col))
            button.grid(row=row, column=col, sticky="nsew")
            buttons[row][col] = button

window = tk.Tk()
window.title("Connect 4 in a Row")

current_player = 'X'
board = [[' ' for _ in range(4)] for _ in range(4)]
buttons = [[None for _ in range(4)] for _ in range(4)]

create_board()
window.mainloop()
