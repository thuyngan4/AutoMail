import smtplib
import pandas as pd
from email.message import EmailMessage
from dotenv import load_dotenv
import os
import time
import random
from datetime import datetime
import pyodbc

load_dotenv()
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

# connect sql
conn_str = (
    "Driver={ODBC Driver 17 for SQL Server};"
    "Server=THUYNGAN47\\SQLEXPRESS;"  
    "Database=EmailSenderDB;"        
    "UID=py102;"                      
    "PWD=123;"                       
)

# đọc excel
def get_excel_file_from_folder(folder_path):
    excel_file = "email_list.xlsx" 
    file_path = os.path.join(folder_path, excel_file)
    return file_path

def generate_html_body(name, subject, body):
    # nội dung mail
    html_content = f"""
    <html>
        <head>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    color: #333;
                    background-color: #f4f4f4;
                    margin: 0;
                    padding: 0;
                }}
                .container {{
                    max-width: 600px;
                    margin: auto;
                    padding: 20px;
                    background-color: white;
                    border-radius: 8px;
                }}
                h1 {{
                    color: #4CAF50;
                }}
                p {{
                    font-size: 14px;
                    line-height: 1.6;
                }}
                .footer {{
                    font-size: 12px;
                    color: #777;
                    margin-top: 20px;
                }}
                a {{
                    color: #4CAF50;
                    text-decoration: none;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>Hello, {name}!</h1>
                <p></b> {subject}</p>
                <p>{body}</p>
                <p class="footer">
                    If you have any questions,please contact us at <a href="mailto:nguyenthuyngan047@gmail.com">nguyenthuyngan047@gmail.com</a>.
                </p>
            </div>
        </body>
    </html>
    """
    return html_content

def send_email_via_smtp(name, email, subject, body):
    try:
        # connect SMTP
        session = smtplib.SMTP("smtp.gmail.com", 587)
        session.starttls()
        session.login(EMAIL_SENDER, EMAIL_PASSWORD)

        # create email
        msg = EmailMessage()
        msg["From"] = EMAIL_SENDER
        msg["To"] = email
        msg["Subject"] = subject
        
        # Create HTML content for email
        html_body = generate_html_body(name, subject, body)
        
        # content email
        msg.set_content(body)
        
        # chèn nội dung HTML vào email
        msg.add_alternative(html_body, subtype='html')

        session.send_message(msg)
        session.quit()
        return "Thành công"
    except Exception as e:
        return f"Lỗi"

def send_bulk_emails(folder_path, subject_template, body_template):
    file_path = get_excel_file_from_folder(folder_path) 
    try:
        # đọc file Excel
        df = pd.read_excel(file_path)
        if "Name" not in df.columns or "Email" not in df.columns:
            raise Exception("Excel file must contain the columns 'Name' and 'Email'")
    except Exception as e:
        return f" Error Reading Excel File"

    results = []

    for index, row in df.iterrows():
        name = str(row["Name"]).strip()
        email = str(row["Email"]).strip()
        subject = subject_template.replace("{name}", name)
        body = body_template.replace("{name}", name)

        # Gửi email 
        status = send_email_via_smtp(name, email, subject, body)
        
        # ghi lại lsu vào database
        results.append((email, status, subject, body))
        time.sleep(random.randint(3, 6)) 

    # lưu vào sql
    try:
        conn = pyodbc.connect(conn_str)
        cursor = conn.cursor()
        for email, status, subject, body in results:
            cursor.execute(
                "INSERT INTO EmailLog (Email, Status, SentAt, Subject, Body) VALUES (?, ?, ?, ?, ?)",
                email, status, datetime.now(), subject, body
            )
        conn.commit()
        conn.close()
    except Exception as e:
        return "SQL Server Log Error"

    return "Email sending process completed!"
