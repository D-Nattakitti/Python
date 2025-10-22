# ****** BMI ******
def bmi_calculator(weight, height):
    """คำนวณค่า BMI จากน้ำหนัก (kg) และส่วนสูง (cm)"""
    return weight / (height / 100) ** 2

def greet(name):
    print(f"สวัสดี {name} ขอให้วันนี้เป็นวันที่ดี")

def bmi_status(bmi):
    # แสดงผลลัพธ์แบบข้อความ 
    if bmi < 18.5:
        return "น้ำหนักน้อยกว่ามาตรฐาน"
    elif bmi < 25:
        return "น้ำหนักปกติ"
    elif bmi < 30:
        return "น้ำหนักเกิน"
    else:
        return "อ้วน"
    

#   ********* Main Program *********

try:
    name = input("กรุณาใส่ชื่อของคุณ: ")
    weight = float(input("กรุณาใส่น้ำหนักคุณ (กก.): "))
    height = float(input("กรุณาใส่ส่วนสูงของคุณ (ซม.): "))

    bmi = bmi_calculator(weight, height)
    greet(name)
    print(f"ค่า BMI ของคุณคือ {bmi:.2f}")
    print(f"อยู๋ในเกณฑ์: {bmi_status(bmi)}")

except ValueError:
    print("กรุณาใส่ค่าให้ถูกต้อง")
