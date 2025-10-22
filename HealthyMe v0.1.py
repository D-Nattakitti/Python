def bmi_calculator(weight, height):
    return weight / (height / 100) ** 2

def greet(name):
    print(f"สวัสดีครับ คุณ {name}")

def bmi_status(bmi):
    if bmi < 18.5:
        return "น้ำหนักน้อยกว่ามาตรฐาน"
    elif bmi < 25:
        return "น้ำหนักปกติ"
    elif bmi < 30:
        return "น้ำหนักเกิน"
    else:
        return "อ้วน"

def age_status(age):
    if age < 0:
        return "ข้อมูลไม่ถูกต้อง"
    elif age < 13:
        return "เด็ก"
    elif age < 19:
        return "วัยรุ่น"
    elif age < 60:
        return "ผู้ใหญ่"
    else:
        return "ผู้สูงวัย"

# ---- Main Program ----
try:
    name = input("กรอกชื่อของคุณ: ")
    age = int(input("กรุณาใส่อายุของคุณ: "))
    weight = float(input("กรุณาใส่น้ำหนักของคุณ (กก.): "))
    height = float(input("กรุณาใส่ส่วนสูงของคุณ (ซม.): "))

    bmi = bmi_calculator(weight, height)
    age_group = age_status(age)

    greet(name)
    print(f"ตอนนี้คุณอายุ {age} ปี อยู่ในวัย {age_group}")
    print(f"ค่า BMI ของคุณคือ {bmi:.2f} ซึ่งอยู่ในเกณฑ์ {bmi_status(bmi)}")

except ValueError:
    print("⚠️ กรุณากรอกข้อมูลให้ถูกต้องนะครับ 🙏")
