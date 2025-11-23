import random

# สร้างกระดาน 3x3
board = [" " for _ in range(9)]

# ฟังก์ชันแสดงกระดาน
def print_board():
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

# ฟังก์ชันเช็คผู้ชนะ
def check_winner(player):
    combos = [
        [0,1,2],[3,4,5],[6,7,8],  # แถว
        [0,3,6],[1,4,7],[2,5,8],  # คอลัมน์
        [0,4,8],[2,4,6]           # แนวทแยง
    ]
    for combo in combos:
        if all(board[i] == player for i in combo):
            return True
    return False

# ฟังก์ชันให้คอมสุ่มเล่น
def computer_move():
    available = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(available)
    board[move] = "O"
    print(f"คอมเลือกช่อง {move+1}")

# ฟังก์ชันหลักเล่นเกม
def tic_tac_toe_vs_computer():
    player = "X"  # คนเล่นเป็น X
    for turn in range(9):
        print_board()
        if player == "X":
            try:
                move = int(input("เลือกช่อง 1-9: ")) - 1
            except ValueError:
                print("กรอกตัวเลข 1-9 เท่านั้น")
                continue
            if move < 0 or move > 8:
                print("กรอกตัวเลข 1-9 เท่านั้น")
                continue
            if board[move] != " ":
                print("ช่องนี้มีคนเล่นแล้ว! เลือกใหม่")
                continue
            board[move] = player
        else:
            computer_move()
        
        if check_winner(player):
            print_board()
            if player == "X":
                print("คุณชนะ! 🎉")
            else:
                print("คอมชนะ 😢")
            return
        
        # สลับผู้เล่น
        player = "O" if player == "X" else "X"
    
    print_board()
    print("เสมอ! 😎")

# เริ่มเกม
tic_tac_toe_vs_computer()
