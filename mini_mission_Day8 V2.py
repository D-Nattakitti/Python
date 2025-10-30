# โปรแกรมนับจำนวนสินค้าที่ขายได้
products = {}

print("=== ระบบบันทึกยอดขายสินค้า ===")
print("พิมพ์ชื่อสินค้า (พิมพ์ end เพื่อจบการทำงาน)")

while True:
    name = input("ชื่อสินค้า: ")

    if name.lower() == "end":
        break

    # ถ้ามีชื่อสินค้านี้แล้วใน dictionary → บวกเพิ่ม 1
    if name in products:
        products[name] += 1
    # ถ้ายังไม่มี → เพิ่มสินค้าใหม่พร้อมเริ่มนับที่ 1
    else:
        products[name] = 1

# แสดงผลลัพธ์
print("\n=== สรุปรายการสินค้าที่ขายได้ ===")
if not products:
    print("ยังไม่มีข้อมูลสินค้า")
else:
    for item, count in products.items():
        print(f"- {item}: {count} ชิ้น")

    print(f"\nรวมทั้งหมด {sum(products.values())} ชิ้น")
