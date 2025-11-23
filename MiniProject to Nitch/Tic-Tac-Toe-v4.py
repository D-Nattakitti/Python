import tkinter as tk
import math

# -------------------
# Setup
# -------------------
root = tk.Tk()
root.title("Tic-Tac-Toe AI (Smart)")

# กระดาน 3x3
board = [" " for _ in range(9)]

# สถิติ
score = {"คุณ":0, "คอม":0, "เสมอ":0}

# -------------------
# ฟังก์ชันเช็คผู้ชนะ
# -------------------
def check_winner(player):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],
        [0,3,6],[1,4,7],[2,5,8],
        [0,4,8],[2,4,6]
    ]
    for combo in combos:
        if all(board[i] == player for i in combo):
            return True
    return False

def game_over():
    return " " not in board or check_winner("X") or check_winner("O")

# -------------------
# Minimax AI
# -------------------
def minimax(board_state, is_max):
    if check_winner("O"):
        return 1
    if check_winner("X"):
        return -1
    if " " not in board_state:
        return 0

    if is_max:
        best_score = -math.inf
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "O"
                score_val = minimax(board_state, False)
                board_state[i] = " "
                best_score = max(score_val, best_score)
        return best_score
    else:
        best_score = math.inf
        for i in range(9):
            if board_state[i] == " ":
                board_state[i] = "X"
                score_val = minimax(board_state, True)
                board_state[i] = " "
                best_score = min(score_val, best_score)
        return best_score

def best_move():
    best_score_val = -math.inf
    move = -1
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score_val = minimax(board, False)
            board[i] = " "
            if score_val > best_score_val:
                best_score_val = score_val
                move = i
    board[move] = "O"
    buttons[move]["text"] = "O"

# -------------------
# ฟังก์ชันคลิกปุ่ม
# -------------------
def click(i):
    if board[i] == " " and not game_over():
        board[i] = "X"
        buttons[i]["text"] = "X"
        check_game_status()
        if not game_over():
            best_move()
            check_game_status()

# -------------------
# ฟังก์ชันเช็คสถานะเกม
# -------------------
def check_game_status():
    if check_winner("X"):
        label["text"] = "คุณชนะ! 🎉"
        score["คุณ"] += 1
        disable_buttons()
        update_score()
    elif check_winner("O"):
        label["text"] = "คอมชนะ 😢"
        score["คอม"] += 1
        disable_buttons()
        update_score()
    elif " " not in board:
        label["text"] = "เสมอ! 😎"
        score["เสมอ"] += 1
        update_score()

def disable_buttons():
    for b in buttons:
        b.config(state="disabled")

def reset_game():
    global board
    board = [" " for _ in range(9)]
    for b in buttons:
        b.config(text=" ", state="normal")
    label["text"] = "เล่นเลย!"
    
def update_score():
    score_label["text"] = f"คุณ: {score['คุณ']}  คอม: {score['คอม']}  เสมอ: {score['เสมอ']}"

# -------------------
# สร้างปุ่ม GUI
# -------------------
buttons = []
for i in range(9):
    b = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2, command=lambda i=i: click(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

label = tk.Label(root, text="เล่นเลย!", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)

score_label = tk.Label(root, text="คุณ: 0  คอม: 0  เสมอ: 0", font=("Arial", 14))
score_label.grid(row=4, column=0, columnspan=3)

reset_button = tk.Button(root, text="เริ่มใหม่", font=("Arial", 14), command=reset_game)
reset_button.grid(row=5, column=0, columnspan=3)

root.mainloop()
