print("Helllo Python!!")

name = "Dome"
age = 28
height = 166.8

print(name, age, height)

print(f"#ตัวแปรที่ 2")
#ดูชนิดข้อมูลของตัวแปร
print(type(name))
print(type(age))
print(type(height))

#แปลงชนิดข้อมูล
print(f"#ตัวแปรที่ 3")
age_str = str(age)
height_int = int(height)
print(type(age_str))
print(type(height_int))

#รับข้อมูลจากผู้ใช้
print(f"#ตัวแปรที่ 4")
user_name = input("Enter your name: ")
user_age = input("Enter your age: ")
print(f"Hello {user_name}, you are {user_age} years old.")
