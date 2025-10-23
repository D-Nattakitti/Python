def calculate_bmi(weight, height):
    return weight / (height / 100) ** 2

def save_to_file(name, weight, height, bmi):
    with open("health_log.txt", "a") as file:
        file.write(f"Name: {name}, Weight: {weight}, Height: {height}, BMI: {bmi:.2f}\n")
    print("✅ บันทึกข้อมูลเรียบร้อยแล้ว!")

def read_health_log():
    try:
        with open("health_log.txt", "r") as file:
            content = file.read()
            return content
    except FileNotFoundError:
        return "ยังไม่มีข้อมูลเก่าครับ"

def main():
    print("=== HealthyMe V0.4 ===")

    old_data = read_health_log()
    print("📄 ข้อมูลเก่า:")
    print(old_data)
    print("----------------------")

    name = input("ชื่อของคุณ: ")
    weight = float(input("น้ำหนัก (kg): "))
    height = float(input("ส่วนสูง (cm): "))

    bmi = calculate_bmi(weight, height)
    print(f"ค่า BMI ของคุณคือ {bmi:.2f}")

    save_to_file(name, weight, height, bmi)

main()
