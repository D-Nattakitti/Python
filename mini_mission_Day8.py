students = []

print("=== ระบบบันทึกข้อมูลนักเรียน ===")

while True:
    name = input("ป้อนชื่อ (พิมพ์ end เพื่อจบ): ")
    if name.lower() == "end":
        break
    
    age = input("อายุ: ")
    score = input("คะแนน: ")

    student = {
        "name": name,
        "age": age,
        "score": score
    }

    students.append(student)

print("\nรายชื่อนักเรียนทั้งหมด:")
for i, s in enumerate(students, start=1):
    print(f"{i}. {s['name']} | อายุ: {s['age']} | คะแนน: {s['score']}")

print(f"\nจำนวนนักเรียนทั้งหมด: {len(students)} คน")
