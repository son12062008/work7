import tkinter as tk

# ฟังก์ชันเพื่อทำการนับถอยหลัง
def countdown(count):
    # แสดงผลเวลา
    label_timer.config(text=str(count))

    # ถ้านับถอยหลังจนถึง 0 ให้แสดงข้อมูล
    if count > 0:
        # เรียกฟังก์ชัน countdown อีกครั้งหลังจาก 1 วินาที
        window.after(1000, countdown, count - 1)
    else:
        # เมื่อเวลาถึง 0 แสดงข้อมูล
        show_info()

# ฟังก์ชันเพื่อแสดงข้อมูล
def show_info():
    label_result.config(text="ชื่อ: สมชาย\nนามสกุล: สมศักดิ์\nชื่อเล่น: สม\nห้องเรียน: ม.4/1\nแผนการเรียน: วิทย์-คณิต\nอยากเรียนคณะ: วิศวกรรมศาสตร์")

# สร้างหน้าต่างหลัก
window = tk.Tk()
window.title("โปรแกรมนับถอยหลัง")

# สร้าง Label สำหรับแสดงเวลา
label_timer = tk.Label(window, font=("Arial", 20))
label_timer.pack(pady=20)

# ปุ่มเริ่มต้นการนับถอยหลัง
button_start = tk.Button(window, text="เริ่มนับถอยหลัง", font=("Arial", 12), command=lambda: countdown(10))
button_start.pack(pady=10)

# Label สำหรับแสดงผลข้อมูลหลังจากนับถอยหลัง
label_result = tk.Label(window, text="", font=("Arial", 12))
label_result.pack(pady=20)

# เริ่มต้นโปรแกรม
window.mainloop()
