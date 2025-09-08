from tkinter import *

# ฟังก์ชันคำนวณพื้นที่สามเหลี่ยม
def calculate_area():
    try:
        # รับค่าจากช่องกรอกข้อมูล
        base = float(base_entry.get())
        height = float(height_entry.get())
        
        # คำนวณพื้นที่สามเหลี่ยม
        area = 0.5 * base * height
        
        # แสดงผลลัพธ์
        result_label.config(text=f"พื้นที่สามเหลี่ยม: {area:.2f} ตารางหน่วย")
    except ValueError:
        result_label.config(text="กรุณากรอกข้อมูลให้ถูกต้อง")

# สร้างหน้าต่างหลัก
root = Tk()
root.title("โปรแกรมคำนวณพื้นที่สามเหลี่ยม")

# สร้างกรอบ Canvas
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# แสดงชื่อแอพ
app_label = Label(root, text="คำนวณพื้นที่สามเหลี่ยม", font=('Arial', 20, 'bold'))
canvas.create_window(200, 50, window=app_label)

# แสดง Label สำหรับฐาน
base_label = Label(root, text="ฐาน (Base):")
canvas.create_window(100, 100, window=base_label)

# แสดง Label สำหรับความสูง
height_label = Label(root, text="ความสูง (Height):")
canvas.create_window(100, 150, window=height_label)

# สร้างช่องกรอกข้อมูลฐาน
base_entry = Entry(root)
canvas.create_window(200, 100, window=base_entry)

# สร้างช่องกรอกข้อมูลความสูง
height_entry = Entry(root)
canvas.create_window(200, 150, window=height_entry)

# ปุ่มคำนวณพื้นที่
calculate_button = Button(root, text="คำนวณพื้นที่", command=calculate_area)
canvas.create_window(200, 200, window=calculate_button)

# Label สำหรับแสดงผลลัพธ์
result_label = Label(root, text="พื้นที่สามเหลี่ยมจะปรากฏที่นี่", font=('Arial', 12))
canvas.create_window(200, 250, window=result_label)

# เริ่มต้นโปรแกรม
root.mainloop()
