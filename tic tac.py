import tkinter as tk
from tkinter import messagebox

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != '':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != '':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != '':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != '':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell == '':
                return False
    return True

def on_click(row, col):
    global current_player

    if board[row][col] == '':
        board[row][col] = current_player
        buttons[row][col].config(text=current_player)

        winner = check_winner(board)
        if winner:
            messagebox.showinfo("Tic Tac Toe", f"Player {winner} wins!")
            reset_board()
        elif is_board_full(board):
            messagebox.showinfo("Tic Tac Toe", "It's a tie!")
            reset_board()
        else:
            current_player = 'O' if current_player == 'X' else 'X'

def reset_board():
    global current_player
    global board

    board = [['' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    for i in range(3):
        for j in range(3):
            buttons[i][j].config(text='', state=tk.NORMAL)

root = tk.Tk()
root.title("Tic Tac Toe")

buttons = [[None]*3 for _ in range(3)]
board = [['' for _ in range(3)] for _ in range(3)]
current_player = 'X'

for i in range(3):
    for j in range(3):
        buttons[i][j] = tk.Button(root, text='', font=('Arial', 20), width=5, height=2,
                                   command=lambda row=i, col=j: on_click(row, col))
        buttons[i][j].grid(row=i, column=j)

reset_button = tk.Button(root, text='Reset', font=('Arial', 14), command=reset_board)
reset_button.grid(row=3, columnspan=3, sticky='WE')

root.mainloop()
