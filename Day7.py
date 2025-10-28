# โปรแกรมเก็บชื่อผลไม้ จนกว่าผู้ใช้จะพิมพ์ end
fruits = []  # สร้าง list ว่างไว้เก็บชื่อผลไม้

print("พิมพ์ชื่อผลไม้ (พิมพ์ end เพื่อจบ)")

while True:
    fruit_name = input("ชื่อผลไม้: ")
    if fruit_name.lower() == 'end':
        break
    fruits.append(fruit_name)

total_fruits = len(fruits)
name_fruits = sorted(fruits)

print(f"\nคุณกรอกผลไม้ทั้งหมด {total_fruits} ชนิด:")
print(fruits)

print("\nผลไม้เรียงตามตัวอักษร:")
print(name_fruits)
