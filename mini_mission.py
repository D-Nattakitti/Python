def age_status(age):
    if age < 0:
        return "ข้อมูลไม่ถูกต้อง"
    elif age < 13:
        return "เด็ก"
    elif age <= 20:
        return "วัยรุ่น"
    elif age < 60:
        return "ผู้ใหญ่"
    elif age > 150:
        return "ข้อมูลไม่ถูกต้อง"
    else:
        return "ผู้สูงอายุ"
    

try:
    age = int(input("กรุณาใส่อายุของคุณ: "))
    print(f"อายุของคุณคือ {age} ปี อยู่ในสถานะ {age_status(age)}")
except ValueError:
    print("⚠️ กรุณากรอกเป็นตัวเลขเท่านั้นนะครับ 🙏")