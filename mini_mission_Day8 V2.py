products = []

print("=== ระบบนับจำนวนสินค้าขายได้ ===")

while True:
    name = input("ป้อนชื่อสินค้า (พิมพ์ end เพื่อจบ): ")
    if name.lower() == "end":
        break

    products = {
        "name": name,
    }

    products.append(products)

print("\nรายชื่อจำนวนสินค้าขายได้:")
for i, s in enumerate(products, start=1):
    print(f"{i}. {s['name']}")

print(f"\nจำนวนนักเรียนทั้งหมด: {len(products)} คน")
