import random

secrt_number = random.randint(1, 100)
attempts = 0
max_attempts = 7 # โอกาสทาย 7 ครั้ง

print("====== เกมทายตัวเลข ======")
print(f"แน่จริงก็ลองทายตัวเลขจาก 1-100 ให้เจอสิ!! \nแต่พลาดได้แค่ {max_attempts} ครั้งเท่านั้น!!!")

# <<< แก้ไขตรงนี้: เปลี่ยน <= เป็น < เพื่อให้ลูปทำงาน 7 ครั้ง (attempts 0 ถึง 6)
while attempts < max_attempts: 
    guess = int(input(f"ครั้งที่ {attempts + 1}: "))
    attempts += 1

    if guess < secrt_number:
        print(f"น้อยไปหน่อยนะ")
    elif guess > secrt_number:
        print(f"มากไปหน่อยนะ")
    else:
        # จะบอกว่าเป็นรอบที่ 'attempts' เพราะ attempts เพิ่งถูกเพิ่มค่าไปแล้ว
        print(f"เก่งมาก!! ในรอบที่ {attempts} คุณก็ทายถูกซักที!") 
        break

    # ตอนนี้ attempts จะเท่ากับ max_attempts (คือ 7) เมื่อทายครบ 7 ครั้งแล้ว
    if attempts == max_attempts and guess != secrt_number:
        print(f"หมดโอกาสแล้วเจ้าหนู!! คำตอบที่ถูกก็คือ ~ {secrt_number}")
    
# Debut
print(f"********** DEBUG นะจ๊ะ **********\nคุณทายเลข {guess} \nรอบที่ {attempts}")
print(f"คำตอบที่ถูกคือ {secrt_number}")