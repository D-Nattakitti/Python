# เงื่อนไข
# age = int(input("กรุณาใส่อายุ: "))

# if age >= 18:
#     print(f"คุณเป็นผู้ใหญ่แล้ว")
# else:
#     print(f"คุณยังเป็นเด็กน้อย")

# หลายเงื่อนไข
# score = int(input("กรุณาใส่คะแนนของคุณ: "))

# if score >= 80:
#     print(f"เกรด A")
# elif score >= 70:
#     print(f"เกรด B")
# elif score >= 60:
#     print(f"เกรด C")
# else:
#     print(f"เกรด F")

# Mini Project
name = input("กรุณาใส่ชื่อของคุณ: ")
age = int(input("กรุณากรอกอายุ: "))
score = int(input("กรุณาใส่คะแนน"))

print(f"สวัสดี {name}")
if age >= 18:
    print(f"ตอนนี้คุณเป็นผู้ใหญ่แล้ว")
elif age >= 13:
    print(f"ตอนนี้คุณเป็นวัยรุ่นแล้ว")
else:
    print(f"ตอนนี้คุณเป็นเด็ก")

if score >= 80:
    print(f"คะแนนของคุณที่ได้คือ เกรด A")
elif score >= 70:
    print(f"คะแนนของคุณที่ได้คือ เกรด B")
elif score >= 60:
    print(f"คะแนนของคุณที่ได้คือ เกรด C")
else:
    print(f"คะแนนของคุณที่ได้คือ เกรด F")