import random


print("====== เกมทายตัวเลข ======")
name = input("ชื่อของคุณคือ: ")
print(f"ยินดีต้อนรับนะ {name}! มาเริ่มเล่นกันเลย!")
total_score = 0


while True: 
    secret_number = random.randint(1, 100) 
    attempts = 0
    max_attempts = 7

    print(f"แน่จริงก็ลองทายตัวเลขจาก 1-100 ให้เจอสิ!! \nแต่พลาดได้แค่ {max_attempts} ครั้งเท่านั้น!!!")

# ลูปทำงาน 7 ครั้ง (attempts 0 ถึง 6)
    while attempts < max_attempts: 
        guess = int(input(f"ครั้งที่ {attempts + 1}: "))
        print("กรุณาใส่ตัวเลขที่เป็นจำนวนเต็มเท่านั้น!")
        attempts += 1 

        if guess < secret_number: 
            print(f"น้อยไปหน่อยนะ")
        elif guess > secret_number: 
            print(f"มากไปหน่อยนะ")
        else:
            print(f"ถูกต้องแล้ว! 🎉 คุณทายทั้งหมด {attempts} ครั้ง")

            # ✅ ให้คะแนนตามจำนวนครั้ง
            if attempts <= 3:
                score = 3
            elif attempts <= 5:
                score = 2
            else:
                score = 1

            total_score += score
            print(f"คะแนนที่ได้: {score} คะแนน 🏆")
            break # 💥 ออกจากลูปเมื่อทายถูก

    if attempts == max_attempts and guess != secret_number: # ✅ แก้ไขการสะกด
        print(f"หมดโอกาสแล้วเจ้าหนู{name}!! คำตอบที่ถูกก็คือ ~ {secret_number}")

    play_again = input("\nอยากเล่นอีกไหม? (y/n): ").lower()
    if play_again != "y":
        print(f"คะแนนรวมสุดท้ายของ{name}คือ: {total_score} คะแนน ขอบคุณที่เล่นนะ!")
        print(f"ไว้เจอกันใหม่นะคุณ {name}")
        break  # ออกจากลูปใหญ่