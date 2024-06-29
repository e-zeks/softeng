import re
import hashlib
import random
import mysql.connector  # MySQL connector
import smtplib
from PyQt5 import QtCore
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from mysql.connector import Error

from screens.registerempUI import Ui_MainWindow

class RegisterWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    register_button = QtCore.pyqtSignal(str, tuple)

    def __init__(self, conn):
        super(RegisterWindow, self).__init__()
        self.conn = conn
        self.setupUi(self)

        # Button connections
        self.back.clicked.connect(self.button_clicked)
        self.register_2.clicked.connect(self.handle_register)

    def button_clicked(self):
        self.back_button.emit()

    def generate_otp(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])

    def handle_register(self):
        lname = self.lname.text().strip()
        fname = self.fname.text().strip()
        email = self.emailadd.text().strip()
        contactnum = self.contactno.text().strip()
        username = self.username.text().strip()
        password = self.password.text().strip()
        confirm_password = self.confirmpassword.text().strip()

        if not self.validate_password():
            QMessageBox.warning(self, "Input Error", "Password must: \n- Have at least 8 characters\n- Contain at least one uppercase letter\n- Contain at least one lowercase letter\n- Contain at least one digit\n- Not contain any special characters")
            print("Password does not meet requirements.")
            return

        if password != confirm_password:
            QMessageBox.warning(self, "Input Error", "Passwords do not match.")
            print("Passwords do not match.")
            return

        if self.is_username_taken():
            QMessageBox.warning(self, "Input Error", "Username is already taken.")
            print("Username is already taken.")
            return

        if re.match(r"[^@]+@[^@]+\.[^@]+", email):  # validate email
            if not self.is_email_registered(email):  # Check if email is registered
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

                    # Hash the password using SHA-256
                    hashed_password = hashlib.sha256(password.encode('utf-8')).hexdigest()

                    # Prepare data tuple to emit
                    data_tuple = (lname, fname, email, contactnum, username, hashed_password)

                    # Emit the register_button signal with data_tuple
                    self.register_button.emit(self.otp, data_tuple)

                except Exception as e:
                    print(f"Failed to send OTP: {str(e)}")  # Debugging statement
                    QMessageBox.critical(None, "Error", f"Failed to send OTP: {str(e)}")
            else:
                QMessageBox.warning(self, "Input Error", "Email is already registered.")
        else:
            QMessageBox.warning(self, "Input Error", "Invalid email format.")

    def is_email_registered(self, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM clients WHERE Email = %s", (email,))
            result = cursor.fetchone()
            return result[0] > 0
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return True

    def is_username_taken(self):
        username = self.username.text().strip()
        try:
            cursor = self.conn.cursor()
            query = "SELECT COUNT(*) FROM employees WHERE Username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            return result[0] > 0
        except Error as e:
            QMessageBox.critical(self, "Database Error", f"Error: {e}")
            print(f"Error: {e}")
            return True

    def validate_password(self):
        password = self.password.text().strip()
        if len(password) < 8:
            return False
        if not re.search("[A-Z]", password):
            return False
        if not re.search("[a-z]", password):
            return False
        if not re.search("[0-9]", password):
            return False
        if re.search("[^A-Za-z0-9]", password):
            return False
        return True

    def clear_fields(self):
        self.lname.clear()
        self.fname.clear()
        self.emailadd.clear()
        self.contactno.clear()
        self.username.clear()
        self.password.clear()
        self.confirmpassword.clear()
