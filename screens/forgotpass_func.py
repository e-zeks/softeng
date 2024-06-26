from email.mime.text import MIMEText
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.forgotpassUI import Ui_MainWindow
import re
import random
import smtplib
import mysql.connector  # Added to import mysql.connector


class ForgotPassWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    sendOTP_button = QtCore.pyqtSignal(str, str)

    def __init__(self, conn):
        super(ForgotPassWindow, self).__init__()
        self.setupUi(self)
        self.back.clicked.connect(self.button_clicked)
        self.sendOTP.clicked.connect(self.handle_sendOTP)
        self.otp = ""
        self.conn = conn

    # otp generator
    def generate_otp(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])

    # Check if email is registered
    def is_email_registered(self, email):
        try:
            cursor = self.conn.cursor()
            # Check in employees table
            cursor.execute("SELECT COUNT(*) FROM employees WHERE email = %s", (email,))
            employee_result = cursor.fetchone()

            # Check in clients table
            cursor.execute("SELECT COUNT(*) FROM clients WHERE email = %s", (email,))
            client_result = cursor.fetchone()

            return employee_result[0] > 0 or client_result[0] > 0
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return False

    # send OTP button function
    def handle_sendOTP(self):
        email = self.registeredemail.text()
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):  # validate email
            if self.is_email_registered(email):  # Check if email is registered
                print("Sending OTP...")  # Debugging statement
                sender_email = "thenoskalos@gmail.com"
                sender_password = "zdih vuqe dzsl asxj"

                self.otp = self.generate_otp()
                subject = "Password Reset OTP"
                body = f"Your OTP for password reset is: {self.otp}"

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

                    self.registeredemail.clear()
                    self.sendOTP_button.emit(self.otp, email)  # Function to switch screen here

                except Exception as e:
                    print(f"Failed to send OTP: {str(e)}")  # Debugging statement
                    QMessageBox.critical(None, "Error", f"Failed to send OTP: {str(e)}")
            else:
                QMessageBox.warning(self, "Email Not Registered", "The email address is not registered.")
        else:
            print("Invalid email address")

    def button_clicked(self):
        self.registeredemail.clear()
        self.back_button.emit()