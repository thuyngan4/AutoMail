# gui.py
from tkinter import *
from tkinter import messagebox
import main  # Gọi hàm từ main.py

root = Tk()
root.title("ThuyNgan Group - Official Notice!")
root.geometry("600x400")
root.config(bg="#f4f4f4")  # Màu nền giao diện nhẹ nhàng

# Hàm xử lý gửi email và tắt giao diện sau khi thành công
def handle_send():
    subject = subject_entry.get()
    body = body_text.get("1.0", END).strip()

    if not subject or not body:
        messagebox.showwarning("Error!", "Please enter all the required information below..")
        return

    folder_path = "C:/Users/admin/OneDrive/Documents/python_self/mail"  # Thư mục chứa file Excel
    result = main.send_bulk_emails(folder_path, subject, body)
    messagebox.showinfo("Kết quả", result)

    # Đóng cửa sổ Tkinter sau khi gửi email thành công
    root.destroy()

# Tiêu đề chính
title_label = Label(root, text="ThuyNgan Group Thông Báo!", font=("Helvetica", 16, "bold"), bg="#f4f4f4", fg="#333")
title_label.pack(pady=20)

# Khung tiêu đề email
Label(root, text="Title:", font=("Arial", 12), bg="#f4f4f4", fg="#333").pack(pady=5)
subject_entry = Entry(root, width=60, font=("Arial", 12))
subject_entry.pack(pady=5)

# Khung nội dung email
Label(root, text="Content:", font=("Arial", 12), bg="#f4f4f4", fg="#333").pack(pady=5)
body_text = Text(root, height=8, width=70, font=("Arial", 12), wrap=WORD)
body_text.pack(pady=5)

# Nút gửi email
Button(root, text="Send Mail", bg="#4CAF50", fg="white", font=("Arial", 12, "bold"), command=handle_send, relief=RAISED, padx=20, pady=10).pack(pady=20)

root.mainloop()
