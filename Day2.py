# แปลงค่า int to str
num = 10
num_str = str(num)
print(num)


# Miniproject
name = input("กรุณากรอกชื่อของคุณ: ")
weight = input("กรุณากรอกน้ำหนักของคุณ: ")
height = input("กรุณากรอกส่วนสูงของคุณ: ")

weight_float = float(weight)
height_float = float(height)

BMI = weight_float/(height_float/100)**2

print(f"สวัสดีคุณ {name} น้ำหนักของคุณก็คือ {weight} ส่วนสูงชองคุณคือ {height} \nBMI ของคุณก็คือ {BMI:.2f}")