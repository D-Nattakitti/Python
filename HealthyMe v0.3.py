def calculate_bmi(weight, height):
    bmi = weight / (height/100)**2
    return bmi

def save_to_file(name, weight, height, bmi):
    file = open("health_log.txt", "a")
    file.write(f"Name: {name}, Wegiht: {weight}, Height: {height}, BMI: {bmi:.2f}")
    file.close()
    print("✅ บันทึกข้อมูลเรียบร้อยแล้ว!")

def main():
    print("=== HealthyMe V0.3 ===")
    name = input("ชื่อของคุณ: ")
    weight = float(input("น้ำหนัก (kg): "))
    height = float(input("ส่วนสูง (cm): "))

    bmi = calculate_bmi(weight, height)
    print(f"ค่า BMI ของคุณคือ {bmi:.2f}")

    save_to_file(name, weight, height, bmi)
    
main()