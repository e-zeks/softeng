import re
import random
import smtplib
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QMessageBox

# otp generator
def generate_otp():
    return ''.join([str(random.randint(0, 9)) for _ in range(6)])

# send OTP button function
def handle_sendOTP(email, MainWindow):
    if re.match(r"[^@]+@[^@]+\.[^@]+", email): #validate email
        print("Sending OTP...")  # Debugging statement
        sender_email = "thenoskalos@gmail.com"
        sender_password = "zdih vuqe dzsl asxj"

        otp = generate_otp()
        subject = "Password Reset OTP"
        body = f"Your OTP for password reset is: {otp}"

        message = MIMEText(body)
        message["Subject"] = subject
        message["From"] = sender_email
        message["To"] = email

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender_email, sender_password)
                server.sendmail(sender_email, [email], message.as_string())
            print("OTP sent successfully")  # Debugging statement
            QMessageBox.information(None, "OTP Sent", "OTP has been sent to your email address.")
        except Exception as e:
            print(f"Failed to send OTP: {str(e)}")  # Debugging statement
            QMessageBox.critical(None, "Error", f"Failed to send OTP: {str(e)}")
    else:
        print("Invalid email address")

def handle_back(current_window, login_window):
    current_window.close()
    login_window.show()