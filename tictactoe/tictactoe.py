import tkinter as tk
import random

BACKGROUND_COLOR = "#264653"
BUTTON_COLOR = "#264653"
BUTTON_TEXT_COLOR = "#ffffff"
LABEL_COLOR = "#ffffff"
WINNER_COLOR = "#2a9d8f"
TIE_COLOR = "#ffcc00"

def next_turn(row, column):
    global player

    if buttons[row][column]['text'] == "" and check_winner() is False:
        if player == players[0]:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[1]
                label.config(text=(players[1]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[0]+" wins"), fg=WINNER_COLOR)
            elif check_winner() == "Tie":
                label.config(text="Tie!", fg=TIE_COLOR)
        else:
            buttons[row][column]['text'] = player
            if check_winner() is False:
                player = players[0]
                label.config(text=(players[0]+" turn"))
            elif check_winner() is True:
                label.config(text=(players[1]+" wins"), fg=WINNER_COLOR)
            elif check_winner() == "Tie":
                label.config(text="Tie!", fg=TIE_COLOR)

def check_winner():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            highlight_winner([buttons[row][0], buttons[row][1], buttons[row][2]])
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            highlight_winner([buttons[0][column], buttons[1][column], buttons[2][column]])
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        highlight_winner([buttons[0][0], buttons[1][1], buttons[2][2]])
        return True
    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        highlight_winner([buttons[0][2], buttons[1][1], buttons[2][0]])
        return True
    elif not empty_spaces():
        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg=TIE_COLOR)
        return "Tie"
    else:
        return False

def empty_spaces():
    for row in range(3):
        for column in range(3):
            if buttons[row][column]['text'] == "":
                return True
    return False

def new_game():
    global player
    player = random.choice(players)
    label.config(text=player + " turn", fg=LABEL_COLOR)
    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)

def highlight_winner(cells):
    for cell in cells:
        cell.config(bg=WINNER_COLOR)

window = tk.Tk()
window.title("Tic-Tac-Toe")
players = ["X", "O"]
player = random.choice(players)
buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

window.configure(bg=BACKGROUND_COLOR)

label = tk.Label(text=player + " turn", font=('Helvetica', 20), fg=LABEL_COLOR, bg=BACKGROUND_COLOR)
label.pack(side="top", pady=10)

reset_button = tk.Button(text="Restart", font=('Helvetica', 12), command=new_game, bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
reset_button.pack(side="top", pady=10)

frame = tk.Frame(window, bg=BACKGROUND_COLOR)
frame.pack()

for row in range(3):
    for column in range(3):
        buttons[row][column] = tk.Button(frame, text="", font=('Helvetica', 24), width=5, height=2,
                                         command=lambda row=row, column=column: next_turn(row, column),
                                         bg=BUTTON_COLOR, fg=BUTTON_TEXT_COLOR)
        buttons[row][column].grid(row=row, column=column)

window.mainloop()
