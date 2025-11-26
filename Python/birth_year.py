age_inpput = int(input("ป้อนอายุของคุณ: "))
if age_inpput < 0:
    print("อายุไม่สามารถเป็นค่าลบได้")
else:
    print("อายุของคุณคือ:", age_inpput)
currnt_year = 2025
brith_year = currnt_year - age_inpput
print("ปีเกิดของคุณคือ:", brith_year)