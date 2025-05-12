Email Sender Tool

Mục đích

Công cụ này giúp gửi email hàng loạt đến danh sách người nhận từ file Excel, nội dung có thể cá nhân hóa bằng tên từng người. Giao diện đơn giản, dễ dùng với khả năng lưu lịch sử gửi vào cơ sở dữ liệu SQL Server.

Thành phần hệ thống

gui.py: Giao diện người dùng bằng Tkinter để nhập tiêu đề và nội dung email.

main.py: Xử lý logic gửi email, kết nối SMTP, đọc file Excel, ghi log vào database.

.env: Lưu thông tin bảo mật như email người gửi và mật khẩu ứng dụng.

email_list.xlsx: Danh sách người nhận email (gồm cột "Name" và "Email").

sendmail.py: Không liên quan đến tính năng gửi email chính.

Hướng dẫn sử dụng

1. Chuẩn bị

Tạo file .env:

EMAIL_SENDER=your_email@gmail.com
EMAIL_PASSWORD=your_app_password

Chuẩn bị file email_list.xlsx với hai cột: Name và Email.

Đảm bảo máy tính đã cài Python và các thư viện sau:

pip install pandas python-dotenv openpyxl

2. Chạy ứng dụng

python gui.py

3. Giao diện sử dụng

Nhập Title (tiêu đề email).

Nhập Content (nội dung email). Có thể dùng {name} để cá nhân hoá.

Nhấn nút Send Mail để gửi.

Ví dụ:

Title: Hello {name}!

Content: Chúng tôi xin gửi tới bạn, {name}, thông báo mới nhất từ ThuyNgan Group.

4. Ghi log

Thông tin gửi sẽ được lưu vào bảng EmailLog trong database SQL Server EmailSenderDB.
