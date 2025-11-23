import tkinter as tk
import random

# สร้างหน้าต่าง
root = tk.Tk()
root.title("Tic-Tac-Toe AI")

# กระดาน 3x3
board = [" " for _ in range(9)]

# เช็คผู้ชนะ
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

# ฟังก์ชัน AI
def computer_move():
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                buttons[i]["text"] = "O"
                return
            board[i] = " "
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                buttons[i]["text"] = "O"
                return
            board[i] = " "
    available = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(available)
    board[move] = "O"
    buttons[move]["text"] = "O"

# ฟังก์ชันคลิกปุ่ม
def click(i):
    if board[i] == " ":
        board[i] = "X"
        buttons[i]["text"] = "X"
        if check_winner("X"):
            label["text"] = "คุณชนะ! 🎉"
            disable_buttons()
            return
        computer_move()
        if check_winner("O"):
            label["text"] = "คอมชนะ 😢"
            disable_buttons()
            return
        if " " not in board:
            label["text"] = "เสมอ! 😎"

# ปิดการกดปุ่มทั้งหมด
def disable_buttons():
    for b in buttons:
        b.config(state="disabled")

# สร้างปุ่ม
buttons = []
for i in range(9):
    b = tk.Button(root, text=" ", font=("Arial", 20), width=5, height=2, command=lambda i=i: click(i))
    b.grid(row=i//3, column=i%3)
    buttons.append(b)

# Label แสดงผล
label = tk.Label(root, text="", font=("Arial", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
