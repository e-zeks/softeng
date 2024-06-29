import re
import hashlib
import random
import mysql.connector  # MySQL connector
import smtplib
from PyQt5 import QtCore
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QMainWindow, QMessageBox
from screens.bookingUI import Ui_MainWindow


class ClientRegWindow(QMainWindow, Ui_MainWindow):
    back_button = QtCore.pyqtSignal()
    register_button = QtCore.pyqtSignal(str, tuple)

    def __init__(self, conn):
        super(ClientRegWindow, self).__init__()
        self.conn = conn
        self.setupUi(self)

        # Connect the buttons to their respective handlers
        self.back.clicked.connect(self.button_clicked)
        self.register_2.clicked.connect(self.handle_register)

    def button_clicked(self):
        # Emit the back_button signal when the back button is clicked
        self.back_button.emit()

    def generate_otp(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])

    def is_username_taken(self):
        username = self.username.text().strip()
        try:
            cursor = self.conn.cursor()
            query = "SELECT COUNT(*) FROM clients WHERE Username = %s"
            cursor.execute(query, (username,))
            result = cursor.fetchone()
            return result[0] > 0
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return True

    def validate_password(self):
        password = self.password.text()
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

    def is_email_registered(self, email):
        try:
            cursor = self.conn.cursor()
            cursor.execute("SELECT COUNT(*) FROM clients WHERE Email = %s", (email,))
            result = cursor.fetchone()
            return result[0] > 0
        except mysql.connector.Error as e:
            print(f"Database error: {e}")
            return True

    def handle_register(self):
        # Get the input values from the form fields and strip any leading/trailing whitespace
        last_name = self.lname.text().strip()
        first_name = self.fname.text().strip()
        address = self.address.text().strip()
        birthday = self.dateEdit.date().toString('yyyy-MM-dd')
        contact_number = self.contact_number.text().strip()
        email = self.emailaddress.text().strip()
        username = self.username.text().strip()
        password = self.password.text().strip()
        program_plan = self.programplan.currentText().strip()
        conditions = self.medical_conditions.text().strip()

        # Check if the username is already taken
        if self.is_username_taken():
            QMessageBox.warning(self, "Input Error", "Username is already taken.")
            return

        # Validate the password
        if not self.validate_password():
            QMessageBox.warning(self, "Input Error",
                                "Password must: \n- Have at least 8 characters\n- Contain at least one uppercase letter\n- Contain at least one lowercase letter\n- Contain at least one digit\n- Not contain any special characters")
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
                    data_tuple = (
                    last_name, first_name, address, birthday, contact_number, email, username, hashed_password,
                    program_plan, conditions)

                    # Emit the register_button signal with data_tuple
                    self.register_button.emit(self.otp, data_tuple)

                    #self.sendOTP_button.emit(self.otp, email)  # Function to switch screen here

                except Exception as e:
                    print(f"Failed to send OTP: {str(e)}")  # Debugging statement
                    QMessageBox.critical(None, "Error", f"Failed to send OTP: {str(e)}")
            else:
                QMessageBox.warning(self, "Input Error", "Email is already registered.")
        else:
            QMessageBox.warning(self, "Input Error", "Invalid email format.")

    def clear_fields(self):
        self.lname.clear()
        self.fname.clear()
        self.address.clear()
        self.contact_number.clear()
        self.emailaddress.clear()
        self.username.clear()
        self.password.clear()
        self.programplan.setCurrentIndex(0)
        self.medical_conditions.clear()
        self.dateEdit.setDate(QtCore.QDate.currentDate())