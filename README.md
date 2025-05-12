# ✉️ ThuyNgan Group - Email Sender Tool

## 📌 Mục đích
Công cụ này giúp gửi email hàng loạt đến danh sách người nhận từ file Excel. Nội dung email có thể **cá nhân hóa theo tên từng người**. Giao diện đơn giản, dễ dùng và có khả năng **ghi lịch sử gửi** vào cơ sở dữ liệu SQL Server.

---

## 🛠 Thành phần hệ thống

| Tên tệp        | Vai trò                                                                 |
|----------------|-------------------------------------------------------------------------|
| `gui.py`       | Giao diện người dùng (Tkinter) để nhập tiêu đề và nội dung email       |
| `main.py`      | Xử lý gửi email, đọc Excel, ghi log vào database                        |
| `.env`         | Lưu email người gửi và mật khẩu ứng dụng (không public file này)        |
| `email_list.xlsx` | Danh sách người nhận gồm 2 cột: `Name`, `Email`                      |
| `sendmail.py`  | Tệp phụ, không tham gia vào quy trình gửi email                         |

---

## 🚀 Hướng dẫn sử dụng

### 1. Chuẩn bị

- Tạo file `.env`:
```env
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
