#เช็คว่าใส่เมนูเกินหรือไม่
def numlen(order):
    number_order = len(order)
    if number_order > 1:
        print(f"คุณใส่เมนูเกินที่กำหนด ไม่ถูกต้อง")
    elif number_order <= 0:
        print(f"คุณไม่ได้ใส่อะไรเลย")
    else:
        pass
    
#เช็คกรณีใส่เมนูมั่ว
def checkmenu(order, menu_list):
    chmenu = order.upper()
    if chmenu == 'A':
        print(f"คุณเลือก กาแฟ")
    elif chmenu == 'B':
        print(f"คุณเลือก ชาเย็น")
    elif chmenu == 'C':
        print(f"คุณเลือก ขนมปัง")
    elif chmenu == 'Q':
        relyn = input("คุณจะจบรายการ ใช่(Y) หรือ ไม่(N)?: ").upper()
        if relyn == 'Y':
            print(f"ที่คุณใส่คือ {relyn} คำสั่งซื้อเสร็จสิ้น")
        elif relyn == 'N':
            print(f"ที่คุณใส่คือ {relyn} ดำเนินการสั่งซื้อต่อ")
        else:
            print(f"ที่คุณใส่คือ {relyn} คุณใส่ไม่ถูกต้อง")
    else:
        print(f"คุณใส่เมนูไม่ถูกต้อง คำแนะนำให้ใส่แค่ A , B , C , หรือจบรายการด้วย Q เท่านั้น")
        

print(f"สวัสดีคุณลูกค้า!! ยินดีต้อนรับสู่ร้านคาเฟ่เล็กๆของเรา สนใจรับสินค้าอะไรดีครับ? \nกาแฟ 50฿(A) \nชาเย็น 40฿(B) \nขนมปัง 25฿(C) \nวิธีใช้งาน ให้พิมเมนูที่ต้องการ A,B,C หรือพิม Q เพื่อสั่งสินค้า ")

menu_list = []

order = input("เมนูที่ลูกค้าเลือกคือ: ")
numlen(order)
checkmenu(order, menu_list)