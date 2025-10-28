# โปรแกรมบันทึกรายชื่อสินค้าในตะกร้า
product = []

print("ยินดีต้อนรับสู่ร้านค้าของเรา!!")
print("คุณสามารถพิมพ์ชื่อสินค้า (พิมพ์ done เพื่อจบ)")

while True:
    product_name = input("ชื่อสินค้า: ")
    if product_name.lower() == 'done':
        break
    product.append(product_name)

total_product = len(product)
name_product = sorted(product)

if not product:
    print("ไม่มีข้อมูลสินค้าในรายการ")
else:
    print(f"\nสินค้าทั้งหมด: {total_product} ชิ้น")
    print(f"รายการสินค้าของคุณมี: {name_product}")
    print(f"สินค้าชิ้นแรกคือ {name_product[0]}")
    print(f"สินค้าชิ้นสุดท้ายคือ {name_product[-1]}")

# ----------------------------------------------------

# โปรแกรมรวมคะแนนสอบ
score = []
print("\n--- โปรแกรมรวมคะแนนสอบ ---")
print("พิมพ์คะแนนของคุณ (พิมพ์ end เพื่อจบการทำงาน)")

while True:
    score_input = input("กรอกคะแนนของคุณ: ")

    if score_input.lower() == 'end':
        break
    
    try:
        score_value = float(score_input)  # ✅ เผื่อคะแนนมีทศนิยม

        if score_value < 0:
            print("❌ คะแนนต้องไม่ติดลบ")
            continue

        score.append(score_value)

    except ValueError:
        print(f"⚠️ ค่าที่ใส่ ({score_input}) ไม่ถูกต้อง ต้องเป็นตัวเลขเท่านั้น")

# ✅ ย้ายการคำนวณออกมานอก while
if score:
    sum_score = sum(score)
    len_score = len(score)
    average = sum_score / len_score

    print(f"\nคะแนนทั้งหมดของคุณคือ: {score}")
    print(f"คะแนนรวมทั้งหมด: {sum_score}")
    print(f"ค่าเฉลี่ย: {average:.2f}")
    print(f"คะแนนสูงสุด: {max(score)}")
    print(f"คะแนนต่ำสุด: {min(score)}")
else:
    print("ยังไม่มีคะแนนที่ถูกกรอกเข้ามา")

# ----------------------------------------------------

# โปรแกรมเก็บชื่อเพื่อน (Tuple Version)
friends = []

print("\n--- โปรแกรมเก็บชื่อเพื่อน ---")
for i in range(5):
    friend_input = input(f"กรอกชื่อเพื่อนคนที่ {i+1}: ")
    friends.append(friend_input)

friends = tuple(friends)  # ✅ แปลงเป็น Tuple
print(f"\nรายชื่อเพื่อนทั้งหมด: {friends}")
print(f"เพื่อนคนแรกของคุณคือ: {friends[0]}")
print(f"เพื่อนคนสุดท้ายของคุณคือ: {friends[-1]}")
