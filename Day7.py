# โปรแกรมเก็บชื่อผลไม้ 5 ชนิด แล้วแสดงผลทั้งหมด
fruits = []  # สร้าง list ว่างไว้เก็บชื่อผลไม้

for i in range(5):
    fruit = input(f"กรอกชื่อผลไม้ชนิดที่ {i+1}: ")
    fruits.append(fruit)  # เพิ่มชื่อผลไม้ลงใน list

print("\n=== รายชื่อผลไม้ทั้งหมด ===")
for f in fruits:
    print(f"- {f}")

