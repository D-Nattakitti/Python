import random

# สร้างกระดาน
board = [" " for _ in range(9)]

# แสดงกระดาน
def print_board():
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print("-+-+-")
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print("-+-+-")
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()

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

# ฟังก์ชันคอมเลือกช่อง
def computer_move():
    # 1. เช็คว่าคอมจะชนะไหม
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner("O"):
                print(f"คอมเลือกช่อง {i+1} (ชนะ)")
                return
            board[i] = " "

    # 2. บล็อกเราถ้าเราจะชนะ
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner("X"):
                board[i] = "O"
                print(f"คอมเลือกช่อง {i+1} (บล็อกคุณ)")
                return
            board[i] = " "

    # 3. เลือกช่องสุ่มถ้าไม่มีอะไร
    available = [i for i, spot in enumerate(board) if spot == " "]
    move = random.choice(available)
    board[move] = "O"
    print(f"คอมเลือกช่อง {move+1} (สุ่ม)")

# เล่นเกม
def tic_tac_toe_smart():
    player = "X"
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

        player = "O" if player == "X" else "X"

    print_board()
    print("เสมอ! 😎")

# เริ่มเกม
tic_tac_toe_smart()
