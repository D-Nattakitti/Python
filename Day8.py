student = {}

student["name"] = input("ป้อนชื่อของคุณ: ")
student["age"] = input("ป้อนอายุของคุณ: ")
student["score"] = input("ป้อนคะแนนของคุณ: ")

print("\nข้อมูลนักเรียน")
print("----------------")
for key, value in student.items():
    print(f"{key}: {value}")
