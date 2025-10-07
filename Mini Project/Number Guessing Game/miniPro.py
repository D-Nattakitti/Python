import random

secrt_number = random.randint(1, 100)
guess = None
attempts = 0

while guess != secrt_number:
    guess = int(input("ลองทายเลข (1-100): "))
    attempts += 1
    print(f"คุณทายไปแล้ว {attempts} รอบ")
    if guess < secrt_number:
        print(f"คุณทายเลข {guess} น้อยเกินไป!")
    elif guess > secrt_number:
        print(f"คุณทายเลข {guess} มากเกินไป!!")
    else:
        print(f"คุณทายเลข {guess} คำตอบถูกต้องงง!! \nโหต้องทายตั้ง {attempts} รอบถึงจะถูก!")
    
# Debut
print(f"********** DEBUG นะจ๊ะ **********\nคุณทายเลข {guess}")
print(f"คำตอบที่ถูกคือ {secrt_number}")