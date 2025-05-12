# 📬 ThuyNgan Group - Email Sender Tool

Một ứng dụng Python đơn giản để gửi email hàng loạt từ danh sách trong Excel, với nội dung được cá nhân hóa, giao diện người dùng dễ sử dụng bằng Tkinter và hỗ trợ lưu log gửi vào SQL Server.

---

## 📌 Mục đích
- Gửi email hàng loạt từ danh sách có sẵn.
- Cá nhân hoá nội dung theo tên người nhận.
- Giao diện người dùng đơn giản.
- Ghi lại lịch sử gửi email vào cơ sở dữ liệu.

---

## 📁 Cấu trúc hệ thống

| Tên tệp           | Mô tả                                                                 |
|-------------------|----------------------------------------------------------------------|
| `gui.py`          | Giao diện người dùng với Tkinter để nhập tiêu đề, nội dung và gửi    |
| `main.py`         | Xử lý gửi email, đọc file Excel, ghi log vào SQL Server              |
| `.env`            | Lưu thông tin bảo mật: email người gửi và mật khẩu ứng dụng          |
| `email_list.xlsx` | Danh sách người nhận (cột: `Name`, `Email`)                          |
| `sendmail.py`     | Tệp không liên quan đến tính năng gửi email chính                    |

---

## ⚙️ Cài đặt

1. Cài Python 3 nếu chưa có.
2. Cài thư viện phụ thuộc:
```bash
pip install pandas openpyxl python-dotenv
```

3. Tạo file `.env` trong cùng thư mục:
```env
EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password
```

4. Đảm bảo có file `email_list.xlsx` với hai cột:
   - `Name`
   - `Email`

---

## 🚀 Sử dụng

### 1. Chạy giao diện người dùng:
```bash
python gui.py
```

### 2. Nhập thông tin:
- **Title**: Tiêu đề email (có thể dùng `{name}` để cá nhân hóa)
- **Content**: Nội dung email (dùng `{name}` để chèn tên người nhận)

📌 *Ví dụ cá nhân hóa:*
```
Tiêu đề: Thông báo dành cho {name}
Nội dung: Xin chào {name}, cảm ơn bạn đã đồng hành cùng ThuyNgan Group!
```

### 3. Nhấn "Send Mail"
- Email sẽ được gửi lần lượt đến từng người trong danh sách.
- Mỗi lần gửi cách nhau 3–6 giây để tránh spam.

---

## 🗂 File Excel cần đặt tại:
```
C:/Users/admin/OneDrive/Documents/python_self/mail/email_list.xlsx
```
> *Có thể thay đổi đường dẫn trong file `gui.py` nếu cần.*

---

## 🧾 Ghi lịch sử gửi

Lưu vào SQL Server với bảng `EmailLog`, gồm:
- Email
- Trạng thái
- Tiêu đề
- Nội dung
- Thời gian gửi

Kết nối cấu hình sẵn trong `main.py`:
```python
Driver={ODBC Driver 17 for SQL Server};
Server=THUYNGAN47\\SQLEXPRESS;
Database=EmailSenderDB;
UID=py102;
PWD=123;
```
> Bạn có thể sửa để phù hợp với cấu hình riêng của bạn.

---

## 🔒 Bảo mật

- KHÔNG chia sẻ file `.env` công khai.
- Sử dụng [App Password của Gmail](https://support.google.com/accounts/answer/185833?hl=vi) thay vì mật khẩu tài khoản chính.

---

## 📮 Liên hệ

Mọi góp ý, hỗ trợ xin gửi về:  
📧 [nguyenthuyngan047@gmail.com](mailto:nguyenthuyngan047@gmail.com)
